<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center"></h1>
</p>
<p align="center">
    <em><code>Booking Rush - fastapi Backend</code></em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=default&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=default&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/Celery-37814A.svg?style=default&logo=Celery&logoColor=white" alt="Celery">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=default&logo=Pytest&logoColor=white" alt="Pytest">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=default&logo=FastAPI&logoColor=white" alt="FastAPI">
   <img src="https://img.shields.io/badge/SQLAlchemy-AB47BC.svg?style=default&logo=SQLAlchemy&logoColor=white" alt="SQLAlchemy">
   <img src="https://img.shields.io/badge/Redis-DC382D.svg?style=default&logo=Redis&logoColor=white" alt="Redis">
   <img src="https://img.shields.io/badge/Pydantic-FFC107.svg?style=default&logo=Pydantic&logoColor=white" alt="Pydantic">
   <img src="https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=default&logo=PostgreSQL&logoColor=white" alt="PostgreSQL">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

<code>This is a feature-rich backend for a mock hotel booking service.</code>

---

##  Features

<code>► Fully custom authentication and authorization with JWT-tokens. <br>
► Backround tasks working as co-processes on separated CPU threads such as: email notification service, image optimisation service. <br>
► Every value, every input and output is validated to prevent value errors. <br>
► MVC architecture, easy to manage and scale. <br>
► Most frequent requests are automatically cached by Redis. <br>
► Database states are saved and tracked by alembic to allow quick migrations.
► A separate endpoint for quick data previewing with a simple frontend.</code>

---

##  Repository Structure

```sh
└── /
    ├── LICENSE
    ├── README.md
    ├── alembic.ini
    ├── app
    │   ├── bookings
    │   ├── dao
    │   ├── hotels
    │   ├── images
    │   ├── main.py
    │   ├── migrations
    │   ├── pages
    │   ├── static
    │   ├── tasks
    │   ├── templates
    │   └── users
    │   ├── config.py
    │   ├── database.py
    │   ├── exceptions.py
    ├── requirements-dev.txt
    ├── requirements.txt
    └── test_data_db.sql
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                             | Summary                         |
| ---                                                                              | ---                             |
| [requirements-dev.txt](requirements-dev.txt)                                     | <code>► Dev and testing dependencies: mypy type checker, pytest and such.</code> |
| [requirements.txt](requirements.txt)                                             | <code>► Essential dependencies to run the app.</code> |
| [test_data_db.sql](test_data_db.sql)                                             | <code>► Some test data from travel.yandex.ru to feed into the database.</code> |

</details>

<details closed><summary>app</summary>

| File                               | Summary                         |
| ---                                | ---                             |
| [config.py](app/config.py)         | <code>► Adds all necessary values from the .env file (Paste your own values!)</code> |
| [database.py](app/database.py)     | <code>► All the database logic</code> |
| [exceptions.py](app/exceptions.py) | <code>► A list of custom comprehensible exceptions that server returns if something goes wrong.</code> |
| [main.py](app/main.py)             | <code>► A file to start the app from! (Not recommended yet)</code> |

</details>

<details closed><summary>app.bookings</summary>

| File                                  | Summary                         |
| ---                                   | ---                             |
| [dao.py](app/bookings/dao.py)         | <code>► Database Access Object for the model.</code> |
| [models.py](app/bookings/models.py)   | <code>► SQLAlchemy ORM Model.</code> |
| [router.py](app/bookings/router.py)   | <code>► A list of endpoints.</code> |
| [schemas.py](app/bookings/schemas.py) | <code>► Pydantic schemas to validate everything bookings-related.</code> |

</details>

<details closed><summary>app.dao</summary>

| File                       | Summary                         |
| ---                        | ---                             |
| [base.py](app/dao/base.py) | <code>► Base Database Access Object parent class.</code> |

</details>

<details closed><summary>app.hotels</summary>

| File                                | Summary                         |
| ---                                 | ---                             |
| [dao.py](app/hotels/dao.py)         | <code>► Database Access Object for the model.</code> |
| [models.py](app/hotels/models.py)   | <code>► SQLAlchemy ORM Model. </code> |
| [router.py](app/hotels/router.py)   | <code>► A list of endpoints.</code> |
| [schemas.py](app/hotels/schemas.py) | <code>► Pydantic schemas to validate everything hotels-related.</code> |

</details>

<details closed><summary>app.images</summary>

| File                              | Summary                         |
| ---                               | ---                             |
| [router.py](app/images/router.py) | <code>► A list of endpoints for uploading images. All images are then optimized by a background celery worker.</code> |

</details>

<details closed><summary>app.migrations</summary>

| File                                            | Summary                         |
| ---                                             | ---                             |
| [env.py](app/migrations/env.py)                 | <code>► Settings file for alembic</code> |
| [script.py.mako](app/migrations/script.py.mako) | <code>► Another alembic-related file. Do not touch this.</code> |

</details>

<details closed><summary>app.pages</summary>

| File                             | Summary                         |
| ---                              | ---                             |
| [router.py](app/pages/router.py) | <code>► A simple frontend endpoint to preview all data in a GET request.</code> |

</details>

<details closed><summary>app.tasks</summary>

| File                                               | Summary                         |
| ---                                                | ---                             |
| [celery.py](app/tasks/celery.py)                   | <code>► This is a main celery file, you should run celery from here.</code> |
| [email_templates.py](app/tasks/email_templates.py) | <code>► A template builder for the booking confirmation email.</code> |
| [tasks.py](app/tasks/tasks.py)                     | <code>► All celery tasks, that are grabbed and run by endpoints.</code> |

</details>

<details closed><summary>app.templates</summary>

| File                                     | Summary                         |
| ---                                      | ---                             |
| [hotels.html](app/templates/hotels.html) | <code>► HTML-template for frontend built dynamically with jinja.</code> |

</details>

<details closed><summary>app.users</summary>

| File                                         | Summary                         |
| ---                                          | ---                             |
| [auth.py](app/users/auth.py)                 | <code>► A separate file for the authentication business logic.</code> |
| [dao.py](app/users/dao.py)                   | <code>► Database Access object for the model.</code> |
| [dependencies.py](app/users/dependencies.py) | <code>► A separate file for the FastAPI dependencies system (auth-related)</code> |
| [models.py](app/users/models.py)             | <code>► SQLAlchemy ORM Model.</code> |
| [router.py](app/users/router.py)             | <code>► A list of endpoints.</code> |
| [schemas.py](app/users/schemas.py)           | <code>► Pydantic schemas to validate everything users-related.</code> |

</details>

<details closed><summary>app.hotels.rooms</summary>

| File                                      | Summary                         |
| ---                                       | ---                             |
| [dao.py](app/hotels/rooms/dao.py)         | <code>► IDatabase Access object for the model.</code> |
| [models.py](app/hotels/rooms/models.py)   | <code>► SQLAlchemy ORM Model.</code> |
| [router.py](app/hotels/rooms/router.py)   | <code>► A list of endpoints.</code> |
| [schemas.py](app/hotels/rooms/schemas.py) | <code>► Pydantic schemas to validate everything rooms-related.</code> |

</details>

<details closed><summary>app.migrations.versions</summary>

| File                                                                                       | Summary                         |
| ---                                                                                        | ---                             |
| [374e04a9dc03_.py](app/migrations/versions/374e04a9dc03_.py)                               | <code>► Your second alembic migration will be here.</code> |
| [ab7be87f4325_first_migration.py](app/migrations/versions/ab7be87f4325_first_migration.py) | <code>► First migration to reference from. Do not touch this.</code> |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the  repository:
>
> ```console
> $ git clone ../
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run  using the command below:
> ```console
> $ uvicorn app.main:app --reload
> $ celery app.tasks.celery:celery worker --loglevel=INFO
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

##  Project Roadmap

- [X] `► Implement basic functionality`
- [ ] `► Admin panel`
- [ ] `► Automatic tests integration with pytest`
- [ ] `► Further code style and SOLID checks (just in case)`
- [ ] `► Logging implementation`
- [ ] `► Easy data monitoring with Grafana`
- [ ] `► Deployment`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://local/FastAPI_service/issues)**: Submit bugs found or log feature requests for the `` project.
- **[Submit Pull Requests](https://local/FastAPI_service/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://local/FastAPI_service/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your local account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone ../
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to local**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://local{/FastAPI_service/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=FastAPI_service">
   </a>
</p>
</details>

---

##  License

This project is protected under the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/) License. For more details, refer to the [LICENSE](LICENSE) file.

---

##  Acknowledgments

- Amazing FastAPI introduction tutorials by [Artem Shumeiko](https://www.youtube.com/@artemshumeiko)
- Brilliant Harward [CS50](https://www.youtube.com/@cs50) Computer Science course.

[**Return**](#-overview)

---
