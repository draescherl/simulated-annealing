# simulated-annealing
My attempt at solving the Travelling Salesman Problem using the Simulated Annealing method.

## Installation
Get the sources :
```
git clone git@github.com:draescherl/simulated-annealing.git
cd simulated-annealing
```

Create a virtual environment :
```
virtualenv venv
```

Activate the environment :
```
. venv/bin/activate
```

Install dependencies :
```
pip install -r requirements.txt
```

## Non pip depencies
For generating the GIFs, the program uses ImageMagick which can be found in most Linux package managers.

## Usage
There are 3 arguments available for this program :

|     Argument          |                          Description                           |
|:---------------------:|:--------------------------------------------------------------:|
|  `--generate-gif`     | Ask the program to generate a gif of the research process.     |
|  `--show-result`      | Ask the program to show you the final solution.                |
|  `--file=<filename>`  | Specify a custom file, see the `inputs/` folder for templates. |

These can all be combined. By default, the program will output the essential information to the terminal and use the `inputs/default.json` file. <br>

Here is an example GIF :
![searching](https://github.com/draescherl/simulated-annealing/blob/master/example.gif)