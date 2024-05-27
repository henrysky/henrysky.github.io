# Henry's Personal Website

Go away this is my website respository

Website favicon by ``freepik`` on https://flaticon.com/
## Local development

This website is developed using ``HUGO`` (https://gohugo.io/), please install ``HUGO`` before developing this website locally on your own computer.

To preiew the website locally, do ``hugo serve`` (or ``hugo serve -D`` for draft mode) in the root directory of this repository.

We also need to fetch list of publication on ADS by ``python ./src/gen_pub_list.py`` after making sure your have your ADS token set in environmental variable ``ADS_TOKEN``.

## Modifying CSS

We use scss to build the CSS stylesheet for the website. It makes it easier to, for example upgrade bootstrap version while keeping our own style. To build a new one

``npm i bootstrap autoprefixer upath sass shelljs`` and ``node src/build-scss.js``, ``node src/build-scripts.js``, ``node src/build-assets.js`` in the root directory of this repository
