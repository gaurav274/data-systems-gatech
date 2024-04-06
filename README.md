# Website for the CMU Data Interaction Group

Deployed at https://dig.cmu.edu/.

The setup is inspired by https://github.com/visdesignlab/visdesignlab.github.io and https://github.com/domoritz/domoritz.github.io. 

## Run

Install Jekyll dependencies with `bundle`. To start this page, run `bundle exec jekyll serve --livereload`.

## Run with Docker

```
docker run \
  --volume="$PWD:/srv/jekyll" \
  -p 4000:4000 -p 35729:35729 \
  -it jekyll/jekyll \
  jekyll serve --livereload
```

## Add Content

To add specific content, follow the README guides in the corresponding directories:

* [Add a person](_people)
* [Add a publication](_publications)
* [Add a post](_posts)

## Setting up docker development environment

```bash
docker run \
  --volume="$PWD:/srv/jekyll" \
  -p 4000:4000 -p 35729:35729 \
  -it jekyll/jekyll \
  /bin/bash
# Below command inside container shell
$ bundle install
# Without killing the container,
# open another terminal in the system
# get container id of the container using 
docker ps
# Below will commit the state of your container into a new image 
docker commit <container id> <gt_username>/data-systems-gatech
# Run below to preview the site on 127.0.0.1:4000 in your browser
docker run --volume="$PWD:/srv/jekyll" -p 127.0.0.1:4000:4000 -p 127.0.0.1:35729:35729 -it <gt_username>/data-systems-gatech jekyll serve --livereload
```