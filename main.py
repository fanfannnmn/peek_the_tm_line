from json import loads
from os import popen
from os.path import basename
from glob import glob
from time import sleep


def compost_req(cmd_file: str) -> str:
    with open(cmd_file, "r") as f:
        x = f.readlines()

    return " ".join(x)


def ticket_info(name: str, cmd: str):
    stream = popen(cmd).read()
    outputs = loads(stream)
    if 'ticket' in outputs:
        ticket = outputs['ticket']
    else:
        return

    print(f">>> {basename(name)}")
    # add more parameters here
    para = ['usersInLineAheadOfYou', 'queueNumber', 'expectedServiceTime', 'queuePaused']
    for i in para:
        print(f"{i}: {ticket[i]}")


if __name__ == '__main__':
    while True:
        cmds = glob("commands/*")
        for loc in cmds:
            command = compost_req(loc)
            ticket_info(loc, command)

        # change it to adjust the query frequency
        sleep(20)
        print("-" * 100)
