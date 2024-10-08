---
layout: post
title:  Blogging with Jekyll and Developing it on Windows
categories: ["Tech"]
tags: ["Windows"]
author: Henry Leung
date: 2019-10-14T00:00:00-00:00
---

## Introduction

I was looking into how blogging is done with Github Page with Jekyll and come across a nice one
developed by [https://gaohaoyang.github.io/](https://gaohaoyang.github.io/) which this blog is based on.  While making new post which is written in markdown is straight-forward, local development such as testing after you modified the code is not easy. Mainly due to Jekyll requires Ruby which requires MSYS2 which personally dislike.

So I use Windows Subsystem for Linux (WSL) which is already installed on my Windows to do the job. 
Just follow [https://jekyllrb.com/docs/installation/ubuntu/](https://jekyllrb.com/docs/installation/ubuntu/)
to install Jekyll on your WSL. Create a file called ``blog.sh`` and edit it by

```bash
touch blog.sh
nano blog.sh
```

Copy and Paste the following and then press ``CTRL+S`` to save and then ``CTRL+X`` to exit to the terminal.

```bash
#!/bin/bash
# remove old files
rm -rf blog
# copy new files from windows, assuming from C drive here
cp -r /mnt/c/path/to/your/blog ./blog
cd  blog
bundle exec jekyll serve
```

You should see a line something like this: ``Server address: http://127.0.0.1:4000/``

Now go to a browser on Windows, type the address above and you will see your blog locally. Once you have 
done some further editing on windows, just press ``CTRL+C`` on WSL and type ``sh blog.sh`` and refresh the page 
to see the new changes. If new changes are satisfying, you can commit and push to Github from Windows.

## Python code

{% include codeHeader.html %}
``` python
import numpy as np

a = 123
print("Hello World!")

for i in range(10):
    print(i)
```

## Maths

Use `$$ \somemath $$` for maths

$$y = x^2 \hbox{ when $x > 2$}$$

```
$$y = x^2 \hbox{ when $x > 2$}$$
```

Or do block:$$log((\sigma_{predictive, i})^2 + (\sigma_{known, i})^2)$$ in line

## Image

<p class="lead"> test </p>

{{< centered_img source_path="https://dummyimage.com/600x400/000/fff" alttext="MarineGEO circle logo" maxwidth="300">}}

{{< centered_img source_path="https://dummyimage.com/600x400/000/fff" alttext="MarineGEO circle logo">}}


``[<img src="{{ site.baseurl }}/assets/img/404.jpg" alt="With alt text here, limited the image to 200px wide, click to go to homepage" 
style="width: 200px;"/>]({{ site.baseurl }}/)``

[<img src="{{ "assets/img/404.jpg" | absURL }}" alt="With alt text here, limited the image to 200px wide, click to go to homepage" 
style="width: 200px;"/>]({{ site.baseurl }}/)

## Quote

> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

## Table

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

## Tree List

Tree diagram example

```
Content
├── 1
├── 2
├── 3
│   ├── 4
│   └── 5
├── 6
└── 7
```