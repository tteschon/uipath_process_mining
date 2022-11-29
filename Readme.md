# Process Mining Activities - Library

## Short Description of the process
Automation library that eases the use of the PM4Py Process Mining Python Package.
## Master Project Details
Item | Details
--- | ---
Master Project Name & Version | Process Mining
Robot Type <br> *(Attenended/Unattended/Mixed)* | Unattended
Is Orchestrator used? *(Yes/No)* | No
Scalable? <br> *(Can process be run by multiple bots in parallel?)* | Yes

## Runtime Guide
### List of Packages
Package Name | High-Level Description
--- | ---
[UIPath System Activities](https://docs.uipath.com/activities/docs/about-the-system-activities-pack) | Core activities which enable the robots to manipulate data tables and collections, work with files and folders, communicate with Orchestrator. Package also contains workflow operators, dialog forms, debugging and invoking methods.
[UIPath Python Activities](https://docs.uipath.com/activities/docs/about-the-python-activities-pack) | Package contains activities which enable the use of Python.
[UIPath UIAutomation Activities](https://docs.uipath.com/activities/docs/about-the-ui-automation-activities-pack) | Package contains core activities which enable the automation of desktop applications, browsers, and virtual machines.
### Master Project Runtime Details
Item | Details
--- | ---
Production Environment Details | ***Link***
Prerequisites to run | Bot has access to Python and PM4PY, and Graphviz python packages
Input Data | Process Mining event data
Expected Output (output data) | Process Mining output data 

### **Project Details**
This section describes all the projects that compose the automated process. 
For each project, the workflow(s) are described in the logical order that they are called in.<br>

## Project: Library
Item | Details
--- | ---
Environment used for development <br> *Name, location, configuration details etc* | 
Environment prerequisites <br> *OS details, libraries, required apps* | [Hardware & Software Requirements for UIPath](https://docs.uipath.com/installation-and-upgrade/docs/robot-hardware-and-software-requirements) <br> [Python 3.9.7](https://www.python.org/downloads/release/python-397/) installed and added to Path. <br> [PM4PY python package]() installed. (Package was installed using [Pip 21.2.3](https://pip.pypa.io/))
Logging level | Execution Logs are stored at 'C:\users\\***username***\AppData\Local\UIPath\Logs' and are also sent to Orchestrator and displayed in the Logs section of the Jobs or Robots pages.
Details about automation <br> *if the apps were automated using UI Automation, Image & Text* | Automation leverages process mining python scripts to access an array of process mining functions.
Repository for project <br> *where the developed project is stored* |
List of reused components | 
Custom logs defined in the workflows <br> *where Throw Activity was used or custom log message was defined* | N/A
Frequent errors found in the development phase | 
Workarounds used in the automation phase | 
Configuration method <br> *assets, excel file, Json file* | 
Configuration details <br> *path for input files, configuration Orchestrator assets used* |

### Workflow(s) specific to the Project 
*All the workflow files (.xaml files) used in the project, with the Input and Output data.*

Workflow File Name | Description | Agruments | Comments
--- | --- | --- | ---

## **Glossary**

- **Master project** - the overall output of the development, containing one or multiple projects that together cover the scope of the robotic process automation.
 - **Project** - a UiPath Studio project containing one or multiple workflow files. A project can be converted to a package and run independently, covering a particular scope within the master project. The project is used when defining the development and support phase of the automation.
 - **Package** - the output of compiling a project. A package can be deployed on the robot machine and be executed by the robot service. Only one package can be executed at a given time by a robot. The package is used when defining the running phase of the automation
- **Workflow** - a component of the package, the workflow encapsulates a part of the project logic. The workflow can be of type: sequence, flowchart or state machine. a workflow is saved as an .xaml file inside the project folder. A workflow file can be invoked from another workflow and by default there is an initial workflow file that will run when executing the package.
- **Activity** - an action that the robot executes.
- **Sequence** - a workflow where activities are executed one after another, in a sequential order
- **Flowchart** - a workflow where activities are connected by arrows and the logic of the workflow can be easily followed in a visual manner. The flowchart can also be exported as an image from UiPath studio
- **State machine** - a more advanced way of organizing a workflow, similar to a flowchart.
- **BOR** - Back office robot 
- **FOR** – Front office robot
- **Orchestrator** – Enterprise architecture server platform supporting: release management, centralized logging, reporting, auditing and monitoring tools, remote control, centralized scheduling, queue/robot workload management, assets management.
