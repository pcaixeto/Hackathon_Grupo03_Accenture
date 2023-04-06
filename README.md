# Introduction
This project is part of the Accenture-Mackenzie Hackathon event, held during the Technology Trends Workshop of the Mackenzie Presbyterian University's Faculty of Computing and Informatics, in April 2023. The challenge was to propose a solution that uses Computer Vision resources in the context of the University.
The objective here is to implement the Event Factory component of Accenture's AIV tool, which is responsible for evaluating the context of a processed frame's video received with all previous frames and deciding when an event should be triggered, as well as which entities should be displayed. In the use case of the project, the system can process a live video stream, detect and identify if there are people with suspicious objects in any given frame, provinding a tool that can be used for security purposes in schools and universities.
# Getting Started
To get started, you will need to have a video to simulate a stream source. You will also need internet access to access the platform website and to connect to the development virtual machine. You should have an IDE installed, such as VSCode, with the Remote - SSH extension.

1. Build your code and run
* Access the development virtual machine via terminal, using your username and password.
* Insert a new video in .mkv format using the command: `scp <FILE_NAME.MKV> <VM_USERNAME>@<VM_IP>:/home/localedgeuser/samples/input`.
* Using VSCode connected to the virtual machine, modify the "Event Factory" component using the path /home/azureuser/repos/event-factory. Replace the "business_logic.py", "class_filter.py", and "pipeline.py" files.
* Access the platform <https://aivqa.liquidstudiobr.com/> with your username and password, and create a new analysis using the video previously uploaded.
* Via terminal, run the Detection Factory component using the commands `docker ps` to list all running components, followed by `docker exec -it <CONTAINER_ID> bash` and `python3 -um yolov5`.
* Run the Event Factory component using the commands `docker exec -it <CONTAINER_ID> bash` and `python3 -um roi`.
* For more information, please access the documentation at: <https://github.com/pcaixeto/Hackathon_Grupo03_Accenture/Documuntacao_AIV_e_Mackenzie_-_v28.03.2_1.pdf>

2.	Software dependencies
* VSCode
* Remote - SSH extension.
Install VSCode from the official website: <https://code.visualstudio.com/download>

3.	Latest releases
* The latest release of the code can be found on the GitHub repository: <https://github.com/pcaixeto/Hackathon_Grupo03_Accenture>

# Contribute
If you would like to contribute to the project, you can do so by submitting pull requests on the GitHub repository. Contributions can include bug fixes, new features, and improvements to the codebase.

# Code designed by:
- Gabriel - 
- Pedro - 
- [Silvania Goularte Correia - 1º sem | ADS](https://github.com/silvaniacorreia)

# Acknowledgements

                                                       %%%    %%%
                                                  %%%              %%%

                                              %%%     ____    ____     %%%
                                                     |_   \  /   _|
                                             %%%       |   \/   |       %%%
                                                       | |\  /| |
                                              %%%     _| |_\/_| |_     %%%
                                                     |_____||_____|
                                                %%%                  %%%

                                                       %%%    %%%
                                    __  __            _                  _
                                   |  \/  |          | |                (_)
                                   | \  / | __ _  ___| | _____ _ __  _____  ___
                                   | |\/| |/ _` |/ __| |/ / _ \ '_ \|_  / |/ _ \
                                   | |  | | (_| | (__|   <  __/ | | |/ /| |  __/
                                   |_|  |_|\__,_|\___|_|\_\___|_| |_/___|_|\___|


                                                            __
                                                            \_ \
                                                              \ \
                                                             _/ /
                                                            /__/
                                     __ _  ___ ___ ___ _ __ | |_ _   _ _ __ ___
                                    / _` |/ __/ __/ _ \ '_ \| __| | | | '__/ _ \
                                   | (_| | (_| (_|  __/ | | | |_| |_| | | |  __/
                                    \__,_|\___\___\___|_| |_|\__|\__,_|_|  \___|
