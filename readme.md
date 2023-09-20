# Project 4

- **Project Name:** Favorite Athlete Holder
- **Project By:** Michael Delvecchio
- [**LINK TO DEPLOYED SITE**]
- **List of Technologies used:** Python, Django, Django Rest Framework, Psycopg2 Binary, Postgres(Neon)

## Description

The backend for this project is going to be created using Django connected to Neon. Neon will serve as the database and hold the model for the athletes the user would like to add to their collection. The model will consist of the athletes name, age, sport, position, team, and year drafted/recruited/started playing. Said user will then be able to view individual athletes and update any information on them that they'd like.

## List of Backend Endpoints

|  Endpoint  | Method |         Purpose          |
| ---------- | ------ | ------------------------ |
| " "        | GET    | Display list of Athletes |
| create     | POST   | Create a new Athlete     |
| delete/:id | DELETE | Delete an Athlete        |
| update/:id | PUT    | Update an Athlete        |
| post/:id   | GET    | Show a single Athlete    |

## ERD (Entity Relationship Diagram)

```mermaid
erDiagram
    INDEX || --O{ SHOW : showAthlete
    SHOW{
        string name
        number age
        string sport
        string position
        string team
        number year
    }

    INDEX || --o{ CREATE : createAthlete
    CREATE {
        string name
        number age
        string sport
        string position
        string team
        number year
    }
    SHOW || --o{ DELETE : deleteAthlete
    DELETE {

    }
    SHOW || --o{ EDIT : editAthlete
    EDIT {
        string name
        number age
        string sport
        string position
        string team
        number year
    }
