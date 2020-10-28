###########################################################################################
## @file makefile                                                                        ##
## @authors (May Alaa - Hazem Mekawy - Ahmed Zoher - Ahmed Refaat - Waleed Adel)         ##
## @brief PC Client GNU Makefile                                                         ##
##	                                                                                     ##
##	Sequence:                                                                            ##
##		## Clearing the command window.                                                  ##
##		## Generating the shared object file in addition to linking the Winsock library. ##
###########################################################################################

make:
	cls
	gcc -fPIC -shared -o ../GUI/client.so client.c -l "ws2_32"