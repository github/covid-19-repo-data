[![Actions Status](https://github.com/github/covid-19-repo-data/workflows/Generate_DB/badge.svg)](https://github.com/github/covid-19-repo-data/actions)


# COVID-19 Public Repository Data

A comprehensive versioned dataset of the repositories and relevant related metadata about public projects hosted on GitHub related to the 2019 Novel Coronavirus and associated COVID-19 disease.

For a view of the latest projects, see the [covid-19](https://github.com/topics/covid-19) topic on GitHub. To preview and interact with the data provided, see the subsection [below](https://github.com/github/covid-19-repo-data/blob/master/README.md#preview-this-data-with-a-sql-interface).

## Why is GitHub doing this?

We have received a number of enquiries from researchers and the community surrounding open collaboration on projects on the platform related to the disease COVID-19 caused by the SARS-CoV-2 virus. Many projects, ordered by star count, can be found using the [covid-19](https://github.com/topics/covid-19) topic on GitHub, however, discovery of other important projects is difficult due to differences in the way users self identify their work. There are some great `awesomelists` such as https://github.com/soroushchehresa/awesome-coronavirus documenting useful projects but they are not time versioned.

As this is such an important topic to many people at this time, we've decided to do regular, versioned, extracts of data from our systems and make them available to researchers under an open license to allow for deeper analysis of these public projects from teams outside of GitHub.

If you have created any interesting research based on this data we would love to hear about it so that we can help ensure it becomes more prominently featured it. Please open a PR against the file `USER_SUBMISSIONS.md` with a link to your research. We are especially interested in highlighting the most promising and impactful projects in need of community help and support.

## Open data

Open source is bigger than any company or community. The dataset is released under [CC0-1.0](#license) for anyone to use and learn from.

There are two main sets of files, released via `TSV` and `json` formats for public consumption in the directory `data/`. 
A comprehensive data dictionary that explains the contents of these files is [here](https://github.com/github/covid-19-repo-data/blob/master/data/data_dictionary.md). The files are sorted in descending order by the count of distinct contributors at the time of extract.

The files have been versioned based on a weekly snapshot of identified repositories from the week of `2020-01-20` onward. 

**We will update this repository with new data files on a weekly basis, generally on Tuesday. We will revisit this each month and provide an update on continuing this commitment.**


### Preview This Data With A SQL Interface

The below Heroku App provides a fully equipped in browser SQL interface with full-text search and [REST API](https://datasette.readthedocs.io/en/stable/json_api.html) extensibility.

https://covid-repo-data.herokuapp.com/covid_sql/latest_data

> The above page is generated with [datasette](https://github.com/simonw/datasette), a tool for exploring and publishing data, which provides [many other](https://datasette.readthedocs.io/en/stable/index.html) features.

### Identification methodology

Rather than relying on any one GitHub topic to identify potential COVID-19 related projects, the data set is produced using a more comprehensive set of search criteria to identify projects likely to be COVID-19 related. 

Note: This has the potential to include a small number of false positives however we figured we were better to cast a wide net and allow consumers of the data to perform additional cleaning if they desire. 

Furthermore, since this data is versioned based on the week the repo was initially created, there may exist data that are included for repos that were orginally `public` that have been made `private` and are currently inaccessible. 

The following parts of public metadata are currently being used to idenfity public projects (those licensed and not) as COVID-19 related:

- The repo's description
- The name of the repo
- The topics associated with the repo
- The organization bio description where that exists

Search terms against these metadata include variations of: `covid`, `coronavirus`, `ncov` and `sars-cov-2`

## License

The data and associated documentation in this repo are open data released under the very permissive [CC0-1.0](LICENSE) public domain dedication. However, please understand:

- Third party rights:
  - Each project _referenced_ is licensed under their own terms (see the ```license_name``` field in the extract, and visit individual project repositories for details).
  - Users or others may have rights to user-provided data such as repository, organization, and user names and descriptions.
  - If you're unsure about your right to use any user-provided data or material from referenced projects, it's up to you to verify your rights.
- Open data norms:
  - If you use this dataset in a publication, a link to or citation of this repository would be appreciated.
  - If you extend this dataset, sharing your additions as open data would also be appreciated.
- If you use this dataset as a starting point for further research which involves accessing and using additional GitHub data, you will need to abide by our [privacy statement](https://help.github.com/en/github/site-policy/github-privacy-statement#public-information-on-github) and related terms.
- CC0-1.0 does not grant any trademark permissions. GitHub® and its stylized versions and the Invertocat mark are GitHub's Trademarks or registered Trademarks. When using GitHub's logos, be sure to follow the GitHub [logo guidelines](https://github.com/logos).
