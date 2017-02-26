Simple Pipeline in Python
=========================

## Installation

```
pip install git+https://github.com/nhat2008/python-simple-pipeline.git
```

## Usage
```
from pipeline import Pipeline
# Load all functions in a python file
import functions as functions

list_str_function = ['get_information_from_persion', 'get_address', 'get_street']

pipeline = Pipeline(functions=functions)
        
result = pipeline(list_str_function, person)
        

```

## Licence
```
This software is licensed under the Apache License, version 2 ("ALv2"), quoted below.

Copyright 2017 Nhat2008

Licensed under the Apache License, Version 2.0 (the "License"); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations under
the License.
```
