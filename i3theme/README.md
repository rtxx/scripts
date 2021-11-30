<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">i3theme</h3>
  <p align="center">
    Simple i3 theme changer
    <br />
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project
![](screenshot1)

<!--
![](screenshot2)
![](screenshot3)
![](screenshot4)
-->

i3theme is a simple script that changes i3 theme from a list of avaiable themes. It changes automatically i3 and i3status configs, Xresources, dunst, GTK and QT (not working atm).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

i3themes needs ```xsettingsd jq feh```
jq to parse the JSON theme file, xsettingsd for GTK themes and feh for the wallpaper
* jq
  ```sh
  pacman -Syu jq xsettingsd feh
  ```

### Installation

_Installing i3theme is super simple. Because its only a script, you can run it anywhere._

1. Download it [here](https://github.com/rtxx/scripts/tree/main/i3theme)
2. Run it
   ```sh
   bash i3theme -t nord
   ```
Make sure its inside a folder with the directory 'themes', or else it wont work.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

i3theme can be used to 

* Change the theme
  ```sh
  bash i3theme -t nord
  ```
* List avaiable themes
  ```sh
  bash i3theme -l
     ```
* For more uses do
  ```sh
  bash i3theme -h
     ```
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

_Readme file made with template from https://github.com/othneildrew/Best-README-Template, thanks!_

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: screenshot1.png
