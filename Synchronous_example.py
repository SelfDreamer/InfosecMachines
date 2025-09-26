#!/usr/bin/env python3 
from time import sleep
import infosecmachines as info 

def main() -> None:
    # Using a normal client without context manager 
    print("\nWe will see this library without context manager...\n")
    sleep(2)

    client = info.Client()
    client.initial_request()

    machine = client.search_machine('Aragog')

    print(machine[0]['techniques'])
    del client, machine

    # Using a normal client with context manager
    print("\nWe will see this library with context manager...\n")
    sleep(2)

    with info.Client() as client:
        
        machine = client.search_machine('Multimaster')

    print(machine[0]['techniques'])


if __name__ == "__main__":
    main()
