# HIL-TestBench-Over-Linux-OS-using-RaspberryPi4
## Objective:

	- Implementing a hardware in the loop (HIL) platform to automate the testing of complex embedded applications. 
	- A test system is used to emulate the environment, inputs and outputs that the unit under test is expected to under-go during its operation,
	- Such emulation is realized through automated test cases or direct application of specified inputs.	

## Modules:
	- Raspberry Pi: The test system (Golden ECU).
	- Communication Frame: An agreed upon format of the communicated message.
	- GUI: A user friendly GUI to facilitate the user entries to the system whether it is a test bench code or direct application.
	- Server and Client to Coordinate the communication between the PC application and the raspberry pi via two modes of operation:
			1) Direct Mode (utilizes UDP for data exchange).
			2) Automated Test Cases Mode (utilizes TCP/IP for data exchange).
