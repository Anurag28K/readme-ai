<p align="center">
  <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="99">
  <img src="https://img.icons8.com/?size=512&id=kTuxVYRKeKEY&format=png" width="99">
</p>
<h1 align="center">README-AI</h1>
<p align="center">
    <em>Automated README file generator, powered by LLM APIs</em>
</p>
<p align="center">
  <a href="https://github.com/eli64s/readme-ai/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/eli64s/readme-ai/release-pipeline.yml?logo=githubactions&label=cicd&logoColor=white&color=c125ff" alt="github-actions">
  </a>
  <a href="https://app.codecov.io/gh/eli64s/readme-ai">
    <img src="https://img.shields.io/codecov/c/github/eli64s/readme-ai?logo=codecov&logoColor=white&color=c125ff" alt="codecov">
  </a>
  <a href="https://pypi.python.org/pypi/readmeai/">
    <img src="https://img.shields.io/pypi/v/readmeai?logo=PyPI&logoColor=white&color=c125ff" alt="pypi-version">
  </a>
  <a href="https://www.pepy.tech/projects/readmeai">
    <img src="https://img.shields.io/pepy/dt/readmeai?logo=Python&logoColor=white&color=c125ff" alt="pepy-total-downloads">
  </a>
  <!--
    <img src="https://img.shields.io/pypi/pyversions/readmeai.svg?color=c125ff" alt="python-versions">
  -->
</p>

---

## 🔗 Quick Links

> - [📍 Overview](#-overview)
> - [🤖 Demo](#-demo)
> - [🔮 Features](#-features)
> - [🚀 Getting Started](#-getting-started)
  > - [⚙️ Installation](#️-installation)
  > - [👩‍💻 Running readme-ai](#-running-readme-ai)
  > - [🧩 Configuration](#-configuration)
> - [🛠 Project Roadmap](#-project-roadmap)
> - [🤝 Contributing](#-contributing)

---

## 📍 Overview

***Objective***

Readme-ai is a developer tool that auto-generates README.md files using a combination of data extraction and generative ai. Simply provide a repository URL or local path to your codebase and a well-structured and detailed README file will be generated for you.

***Motivation***

Streamlines documentation creation and maintenance, enhancing developer productivity. This project aims to enable all skill levels, across all domains, to better understand, use, and contribute to open-source software.<br>

> [!IMPORTANT]
>
> Readme-ai is currently under development with an opinionated configuration and setup. It is vital to review all text generated by the LLM APIs to ensure it accurately represents your project.

---

## 🤖 Demo

Standard CLI usage, providing a repository URL to generate a README file.

[readmeai-cli-demo](https://github.com/eli64s/artifacts/assets/43382407/55b8d1b9-06a7-4b1f-b6a7-aaeccdb27679
)

Generate a README file without making API calls using the `--offline` CLI option.

[readmeai-streamlit-demo](https://github.com/eli64s/artifacts/assets/43382407/3eb39fcf-c1df-49c6-bb5c-63e141857ae3)

> [!TIP]
> <sub>Offline mode is useful for generating a boilerplate README at no cost. View the offline README.md example [here!](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-offline.md)
> </sub>

---

## 🔮 Features

Built with flexibility in mind, readme-ai allows users to customize various aspects of the README using CLI options and configuration settings. Content is generated using a combination of data extraction and making a few calls to LLM APIs.

Currently, readme-ai uses generative ai to create four sections of the README file.

> i. **Header**: Project slogan that describes the repository in an engaging way.
>
> ii. **Overview**: Provides an intro to the project's core use-case and value proposition.
>
> iii. **Features**: Markdown table containing details about the project's technical components.
>
> iv. **Modules**: Codebase file summaries are generated and formatted into markdown tables.

All other content is extracted from processing and analyzing repository metadata and files.

### Customizable Header

The header section is built using repository metadata and CLI options. Key features include:
- **Badges**: Svg icons that represent codebase metadata, provided by [shields.io](https://shields.io/) and [skill-icons](https://github.com/tandpfun/skill-icons).
- **Project Logo**: Select a project logo image from the base set or provide your image.
- **Project Slogan**: Catch phrase that describes the project, generated by generative ai.
- **Table of Contents/Quick Links**: Links to the different sections of the README file.

See a few examples headers generated by *readme-ai* below.
<table>
  <!-- row 1 -->
  <tr>
    <td colspan="2" align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-default.png" alt="default-header" width="800"/><br>
      <code>default output (no options provided to cli)</code>
    </td>
  </tr>
  <!-- row 2 -->
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-cloud.png" alt="cloud-db-logo" width="400"/><br>
      <code>--align left --badges flat-square --image cloud</code>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-gradient.png" alt="gradient-markdown-logo" width="400"/><br>
      <code>--align left --badges flat --image gradient</code>
    </td>
  </tr>
  <!-- row 3 -->
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-custom.png" alt="custom-logo" width="400"/><br>
      <code>--badges flat --image custom</code>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-skills.png" alt="skills-light" width="400"/><br>
      <code>--badges skills-light --image grey</code>
    </td>
  </tr>
  <tr>
  <!-- row 4 -->
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-flat-square.png" alt="readme-ai-header" width="400"/><br>
      <code>--badges flat-square</code>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/header-black.png" alt="black-logo" width="400"/><br>
      <code>--badges flat --image black</code>
    </td>
  </tr>
</table>

See the <a href="#-configuration">Configuration</a> section below for the complete list of CLI options and settings.<br>

<details closed>
  <summary>📑 Codebase Documentation</summary>
  <br>
  <table>
    <tr>
      <td>
        <b>Repository Structure</b><br>
        <p>A directory tree structure is generated using pure Python <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/markdown/tree.py">(tree.py)</a> and embedded in the README.
        </p>
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/directory-tree.png" alt="directory-tree" width="700" />
      </td>
    </tr>
    <tr>
      <td style="padding-top:20px;">
        <b>Codebase Summaries</b>
        <br>
        <p>Code summaries are generated using LLMs and grouped by directory, displayed in markdown tables.</p>
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/llm-summaries.png" alt="llm-summaries" width="700" />
      </td>
    </tr>
  </table>
</details>
<!-- -->
<details closed>
  <summary>📍 Overview & Features Table</summary>
  <p>The overview and features sections are generated using LLM APIs. Structured prompt templates are injected with repository metadata to help produce more accurate and relevant content.
  </p>
  <table>
    <tr>
      <td><b>Overview</b><br>
        <p>High-level introduction of the project, focused on the value proposition and use-cases, rather than technical aspects.</p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/llm-overview.png" alt="llm-overview" width="700" /></td>
    </tr>
    <tr>
      <td style="padding-top:20px;"><b>Features Table</b><br>
        <p>Describes technical components of the codebase, including architecture, dependencies, testing, integrations, and more.</p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/llm-features.png" alt="llm-features" width="700" /></td>
    </tr>
  </table>
</details>
<!-- -->
<details closed>
  <summary>🚀 Dynamic Quickstart Guides</summary>
  <br>
  <table>
    <tr>
      <td><b>Getting Started or Quick Start</b><br>
        <p>Generates structured guides for installing, running, and testing your project. These steps are created by identifying dependencies and languages used in the codebase, and mapping this data to configuration files such as the <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/language_setup.toml">language_setup.toml</a> file.</p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/quickstart.png" alt="quick-start" width="700" />
      </td>
    </tr>
  </table>
</details>
<!-- -->
<details closed>
  <summary>🤝 Contributing Guidelines & More</summary>
  <br>
  <table>
    <tr>
      <td><b>Additional Sections</b><br>
        <p>The remaining README sections are built from a baseline template that includes common sections such as <code>Project Roadmap, Contributing Guidelines, License, and Acknowledgements</code>.</p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/additional-sections.png" alt="contributing-and-more" width="700" /></td>
    </tr>
    <tr>
      <td style="padding-top:20px;"><b>Contributing Guidelines</b><br>
        <p>The contributing guidelines has a dropdown that outlines a general process for contributing to your project.</p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/contributing-guidelines.png" alt="contributing-guidelines" width="700" /></td>
    </tr>
  </table>
</details>
<!-- -->
<details closed>
  <summary>🧩 Template READMEs</summary>
  <p>This feature is currently under development. The template system will allow users to generate README files in different flavors, such as ai, data, web development, etc.
  </p>
  <table>
    <tr>
      <td>
        <h3>README Template for ML & Data</h3>
        <ul>
          <li><a href="#overview">Overview</a>: Project objectives, scope, outcomes.</li>
          <li><a href="#project-structure">Project Structure</a>: Organization and components.</li>
          <li><a href="#data-preprocessing">Data Preprocessing</a>: Data sources and methods.</li>
          <li><a href="#feature-engineering">Feature Engineering</a>: Impact on model performance.</li>
          <li><a href="#model-architecture">Model Architecture</a>: Selection and development strategies.</li>
          <li><a href="#training-and-validation">Training</a>: Procedures, tuning, strategies.</li>
          <li><a href="#testing-and-evaluation">Testing and Evaluation</a>: Results, analysis, benchmarks.</li>
          <li><a href="#deployment">Deployment</a>: System integration, APIs.</li>
          <li><a href="#usage">Usage and Maintenance</a>: User guide, model upkeep.</li>
          <li><a href="#results">Results and Discussion</a>: Implications, future work.</li>
          <li><a href="#ethical-considerations">Ethical Considerations</a>: Ethics, privacy, fairness.</li>
          <li><a href="#contributing">Contributing</a>: Contribution guidelines.</li>
          <li><a href="#acknowledgements">Acknowledgements</a>: Credits, resources used.</li>
          <li><a href="#license">License</a>: Usage rights, restrictions.</li>
        </ul>
      </td>
    </tr>
  </table>
</details>

# Example READMEs

| ⭑ | **Output File 📄** | **Input Repository 📁** | **Repository Type 🔢** |
|---|-------------|------------|-----------|
| ⭑ | [readme-python.md](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-python.md) | [readme-ai](https://github.com/eli64s/readme-ai) | Python |
| ⭑ | [readme-typescript.md](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-typescript.md) | [chatgpt-app-react-ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript) | TypeScript, React |
| ⭑ | [readme-postgres.md](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-postgres.md) | [postgres-proxy-server](https://github.com/jwills/buenavista) | Postgres, Duckdb |
| ⭑ | [readme-kotlin.md](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-kotlin.md) | [file.io-android-client](https://github.com/rumaan/file.io-Android-Client) | Kotlin, Android |
| ⭑ | [readme-streamlit.md](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-streamlit.md) | [readme-ai-streamlit](https://github.com/eli64s/readme-ai-streamlit) | Python, Streamlit |
| ⭑ | [readme-rust-c.md](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-rust-c.md) | [rust-c-app](https://github.com/DownWithUp/CallMon) | C, Rust |
| ⭑ | [readme-go.md](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-go.md) | [go-docker-app](https://github.com/olliefr/docker-gs-ping) | Go |
| ⭑ | [readme-java.md](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-java.md) | [java-minimal-todo](https://github.com/avjinder/Minimal-Todo) | Java |
| ⭑ | [readme-fastapi-redis.md](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-fastapi-redis.md) | [async-ml-inference](https://github.com/FerrariDG/async-ml-inference) | FastAPI, Redis |
| ⭑ | [readme-mlops.md](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-mlops.md) | [mlops-course](https://github.com/GokuMohandas/mlops-course) | Python, Jupyter |
| ⭑ | [readme-pyflink.md](https://github.com/eli64s/readme-ai/blob/main/examples/markdown/readme-pyflink.md) | [flink-flow](https://github.com/eli64s/flink-flow) | PyFlink |

<!--
| ⭑ | [readme-gitlab.md]() | [gitlab](https://github.com/eli64s/flink-flow) | GitLab |
| ⭑ | [readme-bitbucket.md]() | [bitbucket](https://github.com/eli64s/flink-flow) | BitBucket |
| ⭑ | [readme-local.md]() | [filesystem](https://github.com/eli64s/flink-flow) | Filesystem |
-->

---

## 🚀 Getting Started

**Requirements**

* Python: 3.9+
* Package manager or container runtime: `pip` or `docker` recommended.
* LLM API key: currently OpenAI and Google Cloud are supported.

**Repository**

A repository URL or local path to your codebase is required run readme-ai. The following are supported:
* [GitHub](https://github.com/)
* [GitLab](https://gitlab.com/)
* [Bitbucket](https://bitbucket.org/)
* [File System](https://en.wikipedia.org/wiki/File_system)

**OpenAI API Key**

An OpenAI API account and API key are needed to use readme-ai. Get started by creating an account [here](https://platform.openai.com/docs/quickstart/account-setup). Once you have an account, you can create an API key on the [API settings page](https://platform.openai.com/api-keys).

> [!WARNING]
>
> Before using readme-ai, its essential to understand the potential risks and costs associated with using AI-powered tools.
>
> * **Review Sensitive Information**: Ensure all content in your repository is free of sensitive information before running the tool. This project does not remove sensitive data from your codebase, nor from the output README file.
>
> * **API Usage Costs**: The OpenAI API is not free and costs can accumulate quickly! You will be charged for each request made by readme-ai. Be sure to monitor API usage costs using the [OpenAI API Usage Dashboard](https://platform.openai.com/account/usage).

---

### ⚙️ Installation

#### Using `pip`

> ![pip](https://img.shields.io/badge/PyPI-3775A9.svg?style=flat&logo=PyPI&logoColor=white)
>
> ```sh
> pip install readmeai
> ```

#### Using `docker`

> ![docker](https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white)
>
> ```sh
> docker pull zeroxeli/readme-ai:latest
> ```

#### Using `conda`

> ![conda](https://img.shields.io/badge/Anaconda-44A833.svg?style=flat&logo=Anaconda&logoColor=white)
>
> ```sh
> conda install -c conda-forge readmeai
> ```

<details closed>
<summary>
  <h4>From <code>source</code></h4>
</summary>

> Clone repository and change directory.
>
> ```console
> $ git clone https://github.com/eli64s/readme-ai
>
> $ cd readme-ai
> ```

#### Using `bash`
>
> ![bash](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white)
>
> ```console
> $ bash setup/setup.sh
> ```

#### Using `poetry`
>
> ![poetry](https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white)
>
> ```console
> $ poetry install
> ```

* <sub>Similiary you can use `pipenv` or `pip` install the requirements.txt.</sub>

</details>

> [!TIP]
>
> [![pipx](https://img.shields.io/badge/pipx-2CFFAA.svg?style=flat&logo=pipx&logoColor=black)](https://pipxproject.github.io/pipx/installation/)
>
> Use [pipx](https://pipx.pypa.io/stable/installation/) to automatically install and run Python CLI applications in isolated environments!

---

### 👩‍💻 Running *readme-ai*

Before running the CLI, ensure you export your OpenAI API key as an environment variable.

On `Linux` or `MacOS`
```console
$ export OPENAI_API_KEY=YOUR_API_KEY
```

On `Windows`
```console
$ set OPENAI_API_KEY=YOUR_API_KEY
```

#### Using `pip`

> ![pip](https://img.shields.io/badge/PyPI-3775A9.svg?style=flat&logo=PyPI&logoColor=white)
>
> ```sh
> readmeai --repository https://github.com/eli64s/readme-ai
> ```

#### Using `docker`

> ![docker](https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white)
>
> ```sh
> docker run -it \
> -e OPENAI_API_KEY=$OPENAI_API_KEY \
> -v "$(pwd)":/app zeroxeli/readme-ai:latest \
> -r https://github.com/eli64s/readme-ai
> ```

#### Using `streamlit`

> [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://readme-ai.streamlit.app/)
>
> Use the app directly in your browser on <a href="https://streamlit.io/">Streamlit</a>, no installation required! More details about the web app can be found <a href="https://github.com/eli64s/readme-ai-streamlit">here.</a>

<details closed>
<summary>
  <h4>From <code>source</code></h4>
</summary>

#### Using `bash`
>
> ![bash](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white)
>
> ```console
> $ conda activate readmeai
> $ python3 -m readmeai.cli.commands -r https://github.com/eli64s/readme-ai
> ```

#### Using `poetry`
>
> ![poetry](https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white)
>
> ```console
> $ poetry shell
> $ python3 -m readmeai.cli.commands -r https://github.com/eli64s/readme-ai
> ```

</details>

---

### 🧪 Tests

#### Using `pytest`
> [![pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white)](https://docs.pytest.org/en/7.1.x/contents.html)
> ```console
> $ make pytest
> ```

#### Using `nox`
> ```console
> $ nox -f noxfile.py
> ```

> [!TIP]
> <sub>Use [nox](https://nox.thea.codes/en/stable/) to test application against multiple Python environments and dependencies!</sub>

---

## 🧩 Configuration

Run the `readmeai` command in your terminal with the following options to tailor your README file.

### CLI Options

| Option                | Description                                                                            | Values                                                                                           | Default Value  | Data Type      |
| --------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------- | -------------- |
| `--align`, `-a`       | Align the text in the README.md file's header.                                         | `center`, `left`                                                                                 | `center`       | String         |
| `--api-key`           | LLM API key to generate text for the README.md file.                                   |                                                                                                  |                | String         |
| `--badges`, `-b`      | Badge icon style types for README.md badges.                                           | `flat`, `flat-square`, `for-the-badge`, `plastic`, `skills`, `skills-light`, `social` | `default`      | String         |
| `--emojis`, `-e`      | Adds emojis to the README.md file's header sections.                                   |                                                                                                  | `False`        | Boolean        |
| `--image`, `-i`       | Project logo image displayed in the README file header.                                | `CUSTOM`, `BLACK`, `GRADIENT`, `GREY`, `PURPLE`, `YELLOW`, `CLOUD`                    | `DEFAULT`      | String         |
| `🚧 --language`    | Language for generating the README.md file.                                            |                                                                                                  | `en`           | String         |
| `--max-tokens`        | Maximum number of tokens for each section of the README.md file.                       |                                                                                                  |                | Integer        |
| `--model`, `-m`      | GPT language model for generating various sections of the README.md file.              |                                                                                                  |                | String         |
| `--offline`           | Generates a README.md file without API calls, with placeholders for generated content. |                                                                                                  | `False`        | Boolean        |
| `--output`, `-o`   | Output file name for the README file.                                                  |                                                                                                  | `readme-ai.md` | String         |
| `--repository`, `-r`  | Remote repository URL or local directory path for the project.                         |                                                                                                  |                | String         |
| `--temperature`, `-t` | Sets the creativity level for content generation.                                      | `0.0 to 2.0`                                                                                   | `1.0`          | Float          |
| `🚧 --template`          | README template file for generating the README.md file.                                |                                                                                                  |                | String         |
| `--vertex_ai`         | Google Vertex AI configuration, requires location and project ID.                      |                                                                                                  |                | Tuple (String) |
| `--help`              | Displays help information about the command and its options.                           |                                                                                                  |                |                |

<sub><em><code>🚧 feature currently under development</code></em>

---

### Badges

The `--badges` option lets you select the style of the default badge set.
| **Style**      | **Preview** |
|------------------|----------|
| `default`        | ![license](https://img.shields.io/github/license/eli64s/readme-ai?flat&color=0080ff) ![last-commit](https://img.shields.io/github/last-commit/eli64s/readme-ai?flat&color=0080ff&logo=git&logoColor=white) ![languages](https://img.shields.io/github/languages/top/eli64s/readme-ai?flat&color=0080ff) ![language-count](https://img.shields.io/github/languages/count/eli64s/readme-ai?flat&color=0080ff) |
| `flat`           | ![flat](https://img.shields.io/badge/Python-3776AB.svg?&style=flat&logo=Python&logoColor=white) |
| `flat-square`    | ![flat-square](https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=Python&logoColor=white) |
| `for-the-badge`  | ![for-the-badge](https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white) |
| `plastic`        | ![plastic](https://img.shields.io/badge/Python-3776AB.svg?&style=plastic&logo=Python&logoColor=white) |
| `skills`          | [![Skills](https://skillicons.dev/icons?i=py)](https://skillicons.dev) |
| `skills-light`    | [![Skills-Light](https://skillicons.dev/icons?i=py&theme=light)](https://skillicons.dev) |
| `social`         | ![social](https://img.shields.io/badge/Python-3776AB.svg?&style=social&logo=Python&logoColor=white) |


When providing the `--badges` option, readme-ai does two things:

1. Formats the default badge set to match the selection (i.e. flat, flat-square, etc.).
2. Generates an additional badge set representing your projects dependencies and tech stack (i.e. Python, Docker, etc.)

#### Example
>
> ```console
> $ readmeai --badges flat-square --repository https://github.com/eli64s/readme-ai
> ```
>
#### Output
>
> {... project logo ...}
>
> {... project name ...}
>
> {...project slogan...}
>
> <img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat-square&color=0080ff">
> <img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat-square&color=0080ff&logo=git&logoColor=white">
> <img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat-square&color=0080ff">
> <img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat-square&color=0080ff">
>
> <br>
>
>	*Developed with the software and tools below.*
>
> <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white">
> <img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat-square&logo=tqdm&logoColor=black">
> <img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white">
> <img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML">
> <img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white">
> <img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white">
> <br>
> <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white">
> <img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white">
> <img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white">
> <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white">
> <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white">
>
> <br>
>
> {... end of header ...}
>

---

### Project Logo

Select a project logo using the `--image` option. The following options are available:

|  |  |  |
|---|---|---|
| `default` | `gradient` | `black` |
| <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100"> | <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="100"> | <img src="https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png" width="100"> |
| `cloud` | `purple` | `grey` |
|<img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100"> | <img src="https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png" width="100"> | <img src="https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png" width="100"> |

<br>

Use the `--image custom` option to ivoke a prompt to enter a custom image URL or path.

---

## 🛠 Project Roadmap

- [X] Publish readme-ai CLI as a Python package on PyPI.
  - [*PyPI Package*](https://pypi.org/project/readmeai/)
- [X] Containerize the readme-ai CLI as a Docker image via Docker Hub.
  - [*Docker Hub Image*](https://hub.docker.com/repository/docker/zeroxeli/readme-ai/general)
- [X] Serve the readme-ai CLI as a web app, deployed on Streamlit Community Cloud.
  - [*Streamlit Web Application*](https://readme-ai.streamlit.app/)
- [ ] Integrate singular interface for all LLM API providers (Anthropic, Cohere, Gemini, etc.)
- [ ] Design template system to give users a variety of README document flavors (ai, data, web, etc.)
- [ ] Develop robust documentation generation process to extend to full project docs (i.e. Sphinx, MkDocs, etc.)
- [ ] Add support for generating README files in any language (i.e. CN, ES, FR, JA, KO, RU).
- [ ] Create GitHub Actions script to automatically update README file content on repository push.

---

## 📒 Changelog

[Changelog](https://github.com/eli64s/readme-ai/blob/main/CHANGELOG.md)

---

## 🤝 Contributing

- [Discussions](https://github.com/eli64s/readme-ai/discussions)
- [Open an Issue](https://github.com/eli64s/readme-ai/issues)
- [Contributing Guidelines](https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md)

---

## 📄 License

[MIT](https://github.com/eli64s/readme-ai/blob/main/LICENSE)

---

## 👏 Acknowledgments

*Badges*
  - [Shields.io](https://shields.io/)
  - [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
  - [Ileriayo/Markdown-Badges](https://github.com/Ileriayo/markdown-badges)
  - [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons)


<p align="right">
  <a href="#top"><b>Return</b></a>
</p>

---
