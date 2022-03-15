# Badge Generator on Python

# Usage

-   `git clone` this repo
-   run using command `python3 src/execute.py -n--someName -l--someLogoName -bC--someBGColor -lC--someLogoColor` (_last 3 not required_)
-   you can also add `-d--true` or `-d` flag to download svg icon

# Run with Docker and Makefile

> ## You can also run this app using Docker and Makefile

> > ### Dockerfile

> -   _run:_ `docker build -t $name$ .`
> -   _run:_ `docker run -i --name $your_name$ --env-file=.env $name$`
> -   you can also provide `env` variables like: `-e=$var$` instead of env-file

> > ### Makefile
>
> -   _run:_ `make all` for repeat previous operations with one command
> -   _run:_ `make compose` for run docker-compose
> -   _also_ you can _run_ `make remove` for remove containers after `make all` or `docker build` and `docker run`, and also you can _run_ `docker remove-compose` for remove containers after `make compose`
