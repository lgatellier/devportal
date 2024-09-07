# AppAtlas
AppAtlas is a portal to centralize all your application information :
- Application catalog
- Application software components, and their relationships
- Business domains

 :construction: This project is under development. :construction:

 ## Upcoming features
 - Auth : OIDC-first authentication
 - App Catalog : this portal will be built around the concept of applications and software components (e.g. frontends, backends, etc.)

 ## Concepts
 This portal is aimed to be extensible. This modularity relies on following key concepts:
 - **action:** an action
 - **executor:** an executor defines a way to execute a task : native (python code), kubernetes (based on the Job resource), docker, system, etc. First executors will be native python (for sync tasks) and kubernetes (for async tasks). When executing a task, an executor's answer must contain the log output of the task
 - **connector:** a connector defines interactions with an external system like GitLab/GitHub, Kubernetes, ArgoCD, Jenkins, Grafana, etc.

These concepts are implemented in plugins. Some basic core plugins will be embedded in the portal.

:warning: The plugin system is not implemented yet.

## Tech Stack
This projects uses FastAPI with Jinja, HTMX and AlpineJS for web development. All core plugins are written in Python.
