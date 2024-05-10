<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center"></h1>
</p>
<p align="center">
    <em><code>► INSERT-TEXT-HERE</code></em>
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

<code>► This is a fully functional mock backend for a hotel booking service made with FastAPI and PostgreSQL</code>

---

##  Features

<code>► Custom authorisation and authentication with JWT tokens, simple native redoc and swagger documentation, background tasks such as email confirmation sender and .webp image optimiser</code>

---

##  Repository Structure

```sh
└── /
    ├── LICENSE
    ├── README.md
    ├── alembic.ini
    ├── app
    │   ├── bookings
    │   ├── config.py
    │   ├── dao
    │   ├── database.py
    │   ├── exceptions.py
    │   ├── hotels
    │   ├── images
    │   ├── main.py
    │   ├── migrations
    │   ├── pages
    │   ├── static
    │   ├── tasks
    │   ├── templates
    │   └── users
    ├── requirements-dev.txt
    ├── requirements.txt
    └── test_data_db.sql
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                             | Summary                         |
| ---                                                                              | ---                             |
| [requirements-dev.txt](requirements-dev.txt)                                     | <code>► INSERT-TEXT-HERE</code> |
| [requirements.txt](requirements.txt)                                             | <code>► INSERT-TEXT-HERE</code> |
| [test_data_db.sql](test_data_db.sql)                                             | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>app</summary>

| File                               | Summary                         |
| ---                                | ---                             |
| [config.py](app/config.py)         | <code>► INSERT-TEXT-HERE</code> |
| [database.py](app/database.py)     | <code>► INSERT-TEXT-HERE</code> |
| [exceptions.py](app/exceptions.py) | <code>► INSERT-TEXT-HERE</code> |
| [main.py](app/main.py)             | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>dependencies</summary>

| File                                              | Summary                         |
| ---                                               | ---                             |
| [dependencies.txt](dependencies/dependencies.txt) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>app.bookings</summary>

| File                                  | Summary                         |
| ---                                   | ---                             |
| [dao.py](app/bookings/dao.py)         | <code>► INSERT-TEXT-HERE</code> |
| [models.py](app/bookings/models.py)   | <code>► INSERT-TEXT-HERE</code> |
| [router.py](app/bookings/router.py)   | <code>► INSERT-TEXT-HERE</code> |
| [schemas.py](app/bookings/schemas.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>app.dao</summary>

| File                       | Summary                         |
| ---                        | ---                             |
| [base.py](app/dao/base.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>app.hotels</summary>

| File                                | Summary                         |
| ---                                 | ---                             |
| [dao.py](app/hotels/dao.py)         | <code>► INSERT-TEXT-HERE</code> |
| [models.py](app/hotels/models.py)   | <code>► INSERT-TEXT-HERE</code> |
| [router.py](app/hotels/router.py)   | <code>► INSERT-TEXT-HERE</code> |
| [schemas.py](app/hotels/schemas.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>app.images</summary>

| File                              | Summary                         |
| ---                               | ---                             |
| [router.py](app/images/router.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>app.migrations</summary>

| File                                            | Summary                         |
| ---                                             | ---                             |
| [env.py](app/migrations/env.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [script.py.mako](app/migrations/script.py.mako) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>app.pages</summary>

| File                             | Summary                         |
| ---                              | ---                             |
| [router.py](app/pages/router.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>app.tasks</summary>

| File                                               | Summary                         |
| ---                                                | ---                             |
| [celery.py](app/tasks/celery.py)                   | <code>► INSERT-TEXT-HERE</code> |
| [email_templates.py](app/tasks/email_templates.py) | <code>► INSERT-TEXT-HERE</code> |
| [tasks.py](app/tasks/tasks.py)                     | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>app.templates</summary>

| File                                     | Summary                         |
| ---                                      | ---                             |
| [hotels.html](app/templates/hotels.html) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>app.users</summary>

| File                                         | Summary                         |
| ---                                          | ---                             |
| [auth.py](app/users/auth.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [dao.py](app/users/dao.py)                   | <code>► INSERT-TEXT-HERE</code> |
| [dependencies.py](app/users/dependencies.py) | <code>► INSERT-TEXT-HERE</code> |
| [models.py](app/users/models.py)             | <code>► INSERT-TEXT-HERE</code> |
| [router.py](app/users/router.py)             | <code>► INSERT-TEXT-HERE</code> |
| [schemas.py](app/users/schemas.py)           | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>app.hotels.rooms</summary>

| File                                      | Summary                         |
| ---                                       | ---                             |
| [dao.py](app/hotels/rooms/dao.py)         | <code>► INSERT-TEXT-HERE</code> |
| [models.py](app/hotels/rooms/models.py)   | <code>► INSERT-TEXT-HERE</code> |
| [router.py](app/hotels/rooms/router.py)   | <code>► INSERT-TEXT-HERE</code> |
| [schemas.py](app/hotels/rooms/schemas.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>app.migrations.versions</summary>

| File                                                                                       | Summary                         |
| ---                                                                                        | ---                             |
| [374e04a9dc03_.py](app/migrations/versions/374e04a9dc03_.py)                               | <code>► INSERT-TEXT-HERE</code> |
| [ab7be87f4325_first_migration.py](app/migrations/versions/ab7be87f4325_first_migration.py) | <code>► INSERT-TEXT-HERE</code> |

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
> $ python main.py
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

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

This project is protected under the [GNU GPLv3 Licence](https://choosealicense.com/licenses/gpl-3.0/) License. For more details, refer to the [LICENSE](https://github.com/antonprv/BookingRush_fastapi_backend?tab=GPL-3.0-1-ov-file) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
