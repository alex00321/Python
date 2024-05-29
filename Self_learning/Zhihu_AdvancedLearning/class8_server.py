import sys
import time
import socket
import select
import logging
from queue import Queue
import queue

g_select_timeout = 10

class Server(object):
    def __init__(self,host="0.0.0.0",port = 3333,timeout = 2, client_nums = 10) -> None:
        self.__host = host
        self.__port = port
        self.__timeout = timeout
        self.__client_nums = client_nums
        self.__buffer_size = 1024

        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.setblocking(False)
        self.server.settimeout(self.__timeout)
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_KEEPALIVE,1)
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        server_host = (self.__host,self.__port)
        try:
            self.server.bind(server_host)
            self.server.listen(self.__client_nums)
        except:
            raise
        
        self.inputs = [self.server]
        self.outputs = []
        self.message_queues = {}
        self.client_info = {}
    
    def run(self):
        while True:
            readable,writable,exceptional = select.select(self.inputs,self.outputs,self.inputs,g_select_timeout)
            if not (readable or writable or exceptional):
                continue

            for s in readable:
                if s is self.server:
                    connection, client_address = s.accept()
                    print("{} connect".format(str(client_address)))
                    connection.setblocking(0)
                    self.inputs.append(connection)
                    self.client_info[connection] = str(client_address)
                    self.message_queues[connection] = Queue()
                else:
                    try:
                        data = s.recv(self.__buffer_size)
                    except:
                        err_msg = "Client Error!"
                        logging.error(err_msg)
                    if data:
                        data = "{} {} say: {}".format(time.strftime("%Y-%m-%d %H:%M:%S"),self.client_info[s],data)
                        self.message_queues[s].put(data)

                        if s not in self.outputs:
                            self.outputs.append(s)
                    else:
                        print("Client: {} Close.".format(self.client_info[s]))
                        if s in self.outputs:
                            self.outputs.remove(s)
                        self.inputs.remove(s)
                        s.close()
                        del self.message_queues[s]
                        del self.client_info[s]
            
            for s in writable:
                try:
                    next_msg = self.message_queues[s].get_nowait()
                except queue.Empty:
                    err_msg = "Output Queue is Empty!"
                    self.outputs.remove(s)
                except Exception as e:
                    err_msg = "Send Data Error! Errmsg: {}".format(str(e))
                    logging.error(err_msg)
                    if s in self.outputs:
                        self.outputs.remove(s)
                else:
                    for cli in self.client_info:
                        if cli is not s:
                            try:
                                cli.sendall(next_msg.encode("utf8"))
                            except Exception as e:
                                err_msg = "Send data to {} Error! Err_msg: {}".format(str(self.client_info[cli]),str(e))
                                logging.error(err_msg)
                                print("Client: {} Close error.".format(str(self.client_info[cli])))
                                if cli in self.inputs:
                                    self.inputs.remove(cli)
                                    cli.close()
                                if cli in self.outputs:
                                    self.outputs.remove(s)
                                if cli in self.message_queues:
                                    del self.message_queues[s]
                                del self.client_info[cli]
            
            for s in exceptional:
                logging.error("Client: {} Close Error.".format(str(self.client_info[cli])))
                if s in self.inputs:
                    self.inputs.remove(s)
                    s.close()
                if s in self.outputs:
                    self.outputs.remove(s)
                if s in self.message_queues:
                    del self.message_queues[s]
                del self.client_info[s]

if __name__ == "__main__":
    Server().run()