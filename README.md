<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo-news.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Rookie News</h3>

  <p align="center">
    Analyze the news contents with the help of Bing News Search API, Knowledge Graphs, Deceptive Pattern Recognition and
    all the possible NLP tools.
    <br />
    <a href="https://github.com/ajakupov/NewsExplorer"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ajakupov/NewsExplorer">View Demo</a>
    ·
    <a href="https://github.com/ajakupov/NewsExplorer/issues">Report Bug</a>
    ·
    <a href="https://github.com/ajakupov/NewsExplorer/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Analyze the news with the help of [Bing News Search API](https://learn.microsoft.com/en-us/azure/cognitive-services/bing-news-search/search-the-web?WT.mc_id=AI-MVP-5003429).
The Bing News Search API is a RESTful web service, making it easy to call from any programming language that can make HTTP requests and parse JSON. 
You can use the service using either the REST API, or the SDK.
We create a wrapper service to bring some additional functionalities, like Stylometric Analysis, Sentiment Exploration, Deceptive Opinion spam detection etc.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python-logo]][Python-url]
* [![Django][Django-logo]][Django-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python

### Installation

1. Get an API Key for [Bing News Search](https://learn.microsoft.com/en-us/azure/cognitive-services/bing-news-search/search-the-web?WT.mc_id=AI-MVP-5003429)
2. Clone the repo
   ```sh
   git clone https://github.com/ajakupov/NewsExplorer.git
   ```
3. Install python packages
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your API in environmental variables
   ```sh
   export SUBSCRIPTION_KEY=YOUR-API-KEY
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

One of the possible applications of the News Project, is the Deceptive Opinion Spam analysis. 
Deceptive Opinion Spam commonly takes the form of fake reviews (negative or positive) posted by a malicious web user to hurt or inflate a company's image. 
As these reviews have been deliberately written to deceive the reader, human reviewers are faring little better than a chance in detecting these deceptive statements. 
Thus, there is a dire need to address this issue as extracting text patterns from the fraudulent texts with meaningful substructures still remains a challenge
We can construct a model to learn the patterns that constitute a fake review, and then explore the outputs of this model to identify those patterns

_For more examples, please refer to the [website](https://www.alirookie.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Knowledge Graph Integration
- [ ] Stylometric Analysis
- [ ] Sentiment Analysis
    - [ ] Exaggeration Evaluation

See the [open issues](https://github.com/ajakupov/NewsExplorer/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Alibek Jakupov - [@twitter_handle](https://twitter.com/ajakupov1) - ajakupov.expertime@outlook.com

Project Link: [News Explorer](https://github.com/ajakupov/NewsExplorer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [The Rookie Developer Blog(https://www.alirookie.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ajakupov/NewsExplorer.svg?style=for-the-badge
[contributors-url]: https://github.com/ajakupov/NewsExplorer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ajakupov/NewsExplorer.svg?style=for-the-badge
[forks-url]: https://github.com/ajakupov/NewsExplorer/network/members
[stars-shield]: https://img.shields.io/github/stars/ajakupov/NewsExplorer.svg?style=for-the-badge
[stars-url]: https://github.com/ajakupov/NewsExplorer/stargazers
[issues-shield]: https://img.shields.io/github/issues/ajakupov/NewsExplorer.svg?style=for-the-badge
[issues-url]: https://github.com/ajakupov/NewsExplorer/issues
[license-shield]: https://img.shields.io/github/license/ajakupov/NewsExplorer.svg?style=for-the-badge
[license-url]: https://github.com/ajakupov/NewsExplorer/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/alibek-jakupov-30305b61/
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Python-logo]: https://img.shields.io/badge/python-0769AD?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[Django-logo]: https://img.shields.io/badge/django-35495E?style=for-the-badge&logo=django&logoColor=4FC08D
[Django-url]: https://www.djangoproject.com