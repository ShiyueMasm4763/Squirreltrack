![image](https://github.com/ShiyueMasm4763/Squirreltrack/blob/master/mysite/raw/master/image_folder/squirrel.jpg)
# Tools For Analytics Final Project
# Squirreltracker: a visulization web-application tracking squirrels in Central Park

> **Group Number**:Project Group 72, Section 2

> **Group Member**:Zelang Jia, Shiyue Ma

> **Member's Uni**:UNIs: [zj2273, sm4763]


## Introduction

> Our project accomplishes the goals of adding, modifying and viewing datas of squirrels via Django framework, based on the dataset 2018 Central Park Squirrel Census. The web-application enables us to figure out the distribution of squirrels in Central Park and also enables everyone to manage and update the database we have.


## Dataset

> Our project is based on [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/data), published by [**Squirrel Census Community**](https://www.thesquirrelcensus.com/). The dataset contains 3,023 sighting, and incoporates features like fur color, age, movement of the squirrel encountered.

## Management Commands 

> **Import**: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command.

```bash
$ python manage.py import_squirrel_data /path/to/file.csv
```

> **Export**: A command that can be used to export the data from the 2018 cencus file in CSV format. The file path should be specified at the command line after the name of the management command. 

```bash
$ python manage.py export_squirrel_data /path/to/file.csv
```

## Views

> **Map**:  An App that shows a map that displays the location of the squirrel sightings on an OpenStreets map.

> Located at: /map

> **Sightings**: An App that lists all squirrel sightings with links to edit each

> Located at: /sightings

> **Modify**: A view to update a particular sighting

> Located at: /sightings/<unique-squirrel-id>

> **Add**: A view to create a new sighting

> Located at: /sightings/add

> **Stats**: A view with general stats about the sightings

> Located at: /sightings/stats

## Server Link

> To see our codes or more details, please check
 [https://goodlooking-253822.appspot.com](https://goodlooking-253822.appspot.com)

## Contibutors

> Group: 72

> Zelang Jia, zj2273 & Shiyue Ma, sm4763

> UNIs: [zj2273, sm4763]
