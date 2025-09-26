#!/usr/bin/env python3 
import infosecmachines as info 
import asyncio

async def main():
    
    # Example with context manager 
    print("This is the first example, and i will use an context manager...\nPlease, wait 5 seconds\n\n")

    await asyncio.sleep(delay=5)

    async with info.ClientAsync() as client:
        
        machine = await client.search_machine('Aragog')

        print("Extracting all techniques of Aragog machine")

        await asyncio.sleep(2)

        print(machine[0]['techniques'])

        print("\n\nExample with multipke tasks...\n")

        await asyncio.sleep(delay=2)

        # Example with multipke tasks 

        machines = await asyncio.gather(
                client.search_machine(machine='Tentacle'),
                client.search_machine(machine='Nocturnal'),
                client.search_machine(machine='PC'),
                )

        print(machines[0][0]['name']) # Tentacle 
        print(machines[0][0]['os']) # Linux 

        await asyncio.sleep(delay=2)

        print("\n\nThis is the real result...\n")
        print(machines)

if __name__ == "__main__":
    asyncio.run(main=main())

