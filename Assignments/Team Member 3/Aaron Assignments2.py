{
  "cells": [
    {
      "cell_type": "markdown",
      "id": "a3f2c100",
      "metadata": {
        "id": "a3f2c100"
      },
      "source": [
        "## 1 Download the dataset: Dataset\n",
        "## 2. Load the dataset."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AN96uFHhMw6l",
        "outputId": "886037e8-129a-4ccf-b862-28c40dc970ee"
      },
      "id": "AN96uFHhMw6l",
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "33a10105",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "33a10105",
        "outputId": "7018596a-b1ed-41ed-862f-577f833c228b"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   RowNumber  CustomerId   Surname  CreditScore Geography  Gender  Age  \\\n",
              "0          1    15634602  Hargrave          619    France  Female   42   \n",
              "1          2    15647311      Hill          608     Spain  Female   41   \n",
              "2          3    15619304      Onio          502    France  Female   42   \n",
              "3          4    15701354      Boni          699    France  Female   39   \n",
              "4          5    15737888  Mitchell          850     Spain  Female   43   \n",
              "\n",
              "   Tenure    Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
              "0       2       0.00              1          1               1   \n",
              "1       1   83807.86              1          0               1   \n",
              "2       8  159660.80              3          1               0   \n",
              "3       1       0.00              2          0               0   \n",
              "4       2  125510.82              1          1               1   \n",
              "\n",
              "   EstimatedSalary  Exited  \n",
              "0        101348.88       1  \n",
              "1        112542.58       0  \n",
              "2        113931.57       1  \n",
              "3         93826.63       0  \n",
              "4         79084.10       0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e1d4c145-6738-4ae8-8dd9-ddcb5fc95184\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>RowNumber</th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>Surname</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>15634602</td>\n",
              "      <td>Hargrave</td>\n",
              "      <td>619</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>42</td>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>101348.88</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>15647311</td>\n",
              "      <td>Hill</td>\n",
              "      <td>608</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Female</td>\n",
              "      <td>41</td>\n",
              "      <td>1</td>\n",
              "      <td>83807.86</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>112542.58</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>15619304</td>\n",
              "      <td>Onio</td>\n",
              "      <td>502</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>42</td>\n",
              "      <td>8</td>\n",
              "      <td>159660.80</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>113931.57</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>15701354</td>\n",
              "      <td>Boni</td>\n",
              "      <td>699</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>39</td>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>93826.63</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>15737888</td>\n",
              "      <td>Mitchell</td>\n",
              "      <td>850</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Female</td>\n",
              "      <td>43</td>\n",
              "      <td>2</td>\n",
              "      <td>125510.82</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>79084.10</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e1d4c145-6738-4ae8-8dd9-ddcb5fc95184')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-e1d4c145-6738-4ae8-8dd9-ddcb5fc95184 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e1d4c145-6738-4ae8-8dd9-ddcb5fc95184');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "file=pd.read_csv(\"/content/drive/MyDrive/IBM CSC/Churn_Modelling.csv\")\n",
        "df=pd.DataFrame(file)\n",
        "df.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d753f096",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "d753f096",
        "outputId": "8a177ae9-c974-4c0b-f72e-6e51d3d9335c"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   CreditScore Geography  Gender  Age  Tenure    Balance  NumOfProducts  \\\n",
              "0          619    France  Female   42       2       0.00              1   \n",
              "1          608     Spain  Female   41       1   83807.86              1   \n",
              "2          502    France  Female   42       8  159660.80              3   \n",
              "3          699    France  Female   39       1       0.00              2   \n",
              "4          850     Spain  Female   43       2  125510.82              1   \n",
              "\n",
              "  HasCrCard IsActiveMember  EstimatedSalary Exited  \n",
              "0         1              1        101348.88      1  \n",
              "1         0              1        112542.58      0  \n",
              "2         1              0        113931.57      1  \n",
              "3         0              0         93826.63      0  \n",
              "4         1              1         79084.10      0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b6a3ba4a-e3d0-480c-b227-793a251f3f03\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>619</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>42</td>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>101348.88</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>608</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Female</td>\n",
              "      <td>41</td>\n",
              "      <td>1</td>\n",
              "      <td>83807.86</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>112542.58</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>502</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>42</td>\n",
              "      <td>8</td>\n",
              "      <td>159660.80</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>113931.57</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>699</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>39</td>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>93826.63</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>850</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Female</td>\n",
              "      <td>43</td>\n",
              "      <td>2</td>\n",
              "      <td>125510.82</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>79084.10</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b6a3ba4a-e3d0-480c-b227-793a251f3f03')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-b6a3ba4a-e3d0-480c-b227-793a251f3f03 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-b6a3ba4a-e3d0-480c-b227-793a251f3f03');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ],
      "source": [
        "df['HasCrCard'] = df['HasCrCard'].astype('category')\n",
        "df['IsActiveMember'] = df['IsActiveMember'].astype('category')\n",
        "df['Exited'] = df['Exited'].astype('category')\n",
        "df = df.drop(columns=['RowNumber', 'CustomerId', 'Surname'])\n",
        "df.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "593698ba",
      "metadata": {
        "id": "593698ba"
      },
      "source": [
        "# perform visualization"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d1ec6b18",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 374
        },
        "id": "d1ec6b18",
        "outputId": "31b4b61d-1a18-46a2-c8bd-4e16fa2016d6"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "  index  Exited\n",
              "0     0  0.7963\n",
              "1     1  0.2037"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a6a04b7a-22c3-41a4-ac6f-61dce4425701\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>index</th>\n",
              "      <th>Exited</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>0.7963</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>0.2037</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a6a04b7a-22c3-41a4-ac6f-61dce4425701')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-a6a04b7a-22c3-41a4-ac6f-61dce4425701 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-a6a04b7a-22c3-41a4-ac6f-61dce4425701');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 5
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "import seaborn as sns\n",
        "density = df['Exited'].value_counts(normalize=True).reset_index()\n",
        "sns.barplot(data=density, x='index', y='Exited', );\n",
        "density"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c9fd1f52",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 441
        },
        "id": "c9fd1f52",
        "outputId": "f4841a65-53aa-472c-b748-2a85dbe31dc6"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x432 with 4 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "import matplotlib.pyplot as plt\n",
        "categorical = df.drop(columns=['CreditScore', 'Age', 'Tenure', 'Balance', 'EstimatedSalary'])\n",
        "rows = int(np.ceil(categorical.shape[1] / 2)) - 1\n",
        "\n",
        "# create sub-plots anf title them\n",
        "fig, axes = plt.subplots(nrows=rows, ncols=2, figsize=(10,6))\n",
        "axes = axes.flatten()\n",
        "\n",
        "for row in range(rows):\n",
        "    cols = min(2, categorical.shape[1] - row*2)\n",
        "    for col in range(cols):\n",
        "        col_name = categorical.columns[2 * row + col]\n",
        "        ax = axes[row*2 + col]       \n",
        "\n",
        "        sns.countplot(data=categorical, x=col_name, hue=\"Exited\", ax=ax);\n",
        "        \n",
        "plt.tight_layout()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "8302eef0",
      "metadata": {
        "id": "8302eef0"
      },
      "source": [
        "# Perform descriptive statistics on the dataset.¶"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f244f5b9",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 612
        },
        "id": "f244f5b9",
        "outputId": "a9c46ab0-7c0d-4a9f-878f-1c671317fcb4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 10000 entries, 0 to 9999\n",
            "Data columns (total 11 columns):\n",
            " #   Column           Non-Null Count  Dtype   \n",
            "---  ------           --------------  -----   \n",
            " 0   CreditScore      10000 non-null  int64   \n",
            " 1   Geography        10000 non-null  object  \n",
            " 2   Gender           10000 non-null  object  \n",
            " 3   Age              10000 non-null  int64   \n",
            " 4   Tenure           10000 non-null  int64   \n",
            " 5   Balance          10000 non-null  float64 \n",
            " 6   NumOfProducts    10000 non-null  int64   \n",
            " 7   HasCrCard        10000 non-null  category\n",
            " 8   IsActiveMember   10000 non-null  category\n",
            " 9   EstimatedSalary  10000 non-null  float64 \n",
            " 10  Exited           10000 non-null  category\n",
            "dtypes: category(3), float64(2), int64(4), object(2)\n",
            "memory usage: 654.8+ KB\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        CreditScore           Age        Tenure        Balance  NumOfProducts  \\\n",
              "count  10000.000000  10000.000000  10000.000000   10000.000000   10000.000000   \n",
              "mean     650.528800     38.921800      5.012800   76485.889288       1.530200   \n",
              "std       96.653299     10.487806      2.892174   62397.405202       0.581654   \n",
              "min      350.000000     18.000000      0.000000       0.000000       1.000000   \n",
              "25%      584.000000     32.000000      3.000000       0.000000       1.000000   \n",
              "50%      652.000000     37.000000      5.000000   97198.540000       1.000000   \n",
              "75%      718.000000     44.000000      7.000000  127644.240000       2.000000   \n",
              "max      850.000000     92.000000     10.000000  250898.090000       4.000000   \n",
              "\n",
              "       EstimatedSalary  \n",
              "count     10000.000000  \n",
              "mean     100090.239881  \n",
              "std       57510.492818  \n",
              "min          11.580000  \n",
              "25%       51002.110000  \n",
              "50%      100193.915000  \n",
              "75%      149388.247500  \n",
              "max      199992.480000  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-bf859897-63e8-44e6-83b1-b20b050bdff5\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>650.528800</td>\n",
              "      <td>38.921800</td>\n",
              "      <td>5.012800</td>\n",
              "      <td>76485.889288</td>\n",
              "      <td>1.530200</td>\n",
              "      <td>100090.239881</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>96.653299</td>\n",
              "      <td>10.487806</td>\n",
              "      <td>2.892174</td>\n",
              "      <td>62397.405202</td>\n",
              "      <td>0.581654</td>\n",
              "      <td>57510.492818</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>350.000000</td>\n",
              "      <td>18.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>11.580000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>584.000000</td>\n",
              "      <td>32.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>51002.110000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>652.000000</td>\n",
              "      <td>37.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>97198.540000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>100193.915000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>718.000000</td>\n",
              "      <td>44.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>127644.240000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>149388.247500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>850.000000</td>\n",
              "      <td>92.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>250898.090000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>199992.480000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-bf859897-63e8-44e6-83b1-b20b050bdff5')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-bf859897-63e8-44e6-83b1-b20b050bdff5 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-bf859897-63e8-44e6-83b1-b20b050bdff5');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ],
      "source": [
        "df.info()\n",
        "df.describe()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "c3d48704",
      "metadata": {
        "id": "c3d48704"
      },
      "source": [
        "# Handle the missing value"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fa404402",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fa404402",
        "outputId": "789593c8-dc51-4efb-bdd1-2b04a1530dc9"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "CreditScore        0\n",
              "Geography          0\n",
              "Gender             0\n",
              "Age                0\n",
              "Tenure             0\n",
              "Balance            0\n",
              "NumOfProducts      0\n",
              "HasCrCard          0\n",
              "IsActiveMember     0\n",
              "EstimatedSalary    0\n",
              "Exited             0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ],
      "source": [
        "df.isna().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "031c7236",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "031c7236",
        "outputId": "74a3a12c-7320-422e-faf8-9597a7d6e2ab"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "unique of Geography is 3 they are {'Spain', 'Germany', 'France'}\n",
            "unique of Gender is 2 they are {'Female', 'Male'}\n",
            "unique of HasCrCard is 2 they are {0, 1}\n",
            "unique of IsActiveMember is 2 they are {0, 1}\n",
            "unique of Exited is 2 they are {0, 1}\n"
          ]
        }
      ],
      "source": [
        "for i in df:\n",
        "    if df[i].dtype=='object' or df[i].dtype=='category':\n",
        "        print(\"unique of \"+i+\" is \"+str(len(set(df[i])))+\" they are \"+str(set(df[i])))"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "d653b22c",
      "metadata": {
        "id": "d653b22c"
      },
      "source": [
        "#  Find the outliers and replace the outliers"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1a74a611",
      "metadata": {
        "id": "1a74a611"
      },
      "outputs": [],
      "source": [
        "def box_scatter(data, x, y):    \n",
        "    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(16,6))\n",
        "    sns.boxplot(data=data, x=x, ax=ax1)\n",
        "    sns.scatterplot(data=data, x=x,y=y,ax=ax2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "9f745587",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 458
        },
        "id": "9f745587",
        "outputId": "3805e01f-940f-408c-d682-64819f837b07"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "# of Bivariate Outliers: 19\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1152x432 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "box_scatter(df,'CreditScore','Exited');\n",
        "plt.tight_layout()\n",
        "print(f\"# of Bivariate Outliers: {len(df.loc[df['CreditScore'] < 400])}\")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "46d72a78",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 458
        },
        "id": "46d72a78",
        "outputId": "1391f914-087d-44aa-baa5-5ac0fca1f451"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "# of Bivariate Outliers: 3\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1152x432 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "box_scatter(df,'Age','Exited');\n",
        "plt.tight_layout()\n",
        "print(f\"# of Bivariate Outliers: {len(df.loc[df['Age'] > 87])}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "2802f875",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 458
        },
        "id": "2802f875",
        "outputId": "e04bf7df-4ad3-469f-ada1-ceffbe919352"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "# of Bivariate Outliers: 4\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1152x432 with 2 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAABHgAAAGoCAYAAAA99FLLAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzde5wcV3nn/+/TXX2fi6TRWJbli2xLAiyZcFEcQrJAfMPws2QnEGJI1mwCIZuAUfAmGycByxZmWZKsWYd1SCA/NiY34yULSA4320C8GwdimYttYWyNZcu2kKyRRppL9/T97B9V3erp24xi97RK+rxfL72mu+pU1VNV55yqflTdx5xzAgAAAAAAQHhF+h0AAAAAAAAAXhgSPAAAAAAAACFHggcAAAAAACDkSPAAAAAAAACEHAkeAAAAAACAkPP6HcDxWr58uVu9enW/wwAAAAAAAFh0Dz300CHn3Gjz9NAleFavXq2dO3f2OwwAAAAAAIBFZ2Z7203nK1oAAAAAAAAhR4IHAAAAAAAg5EjwAAAAAAAAhBwJHgAAAAAAgJAjwQMAAAAAABByJHgAAAAAAABCjgQPAAAAAABAyJHgAQAAAAAACDkSPAAAAAAAACFHggcAAAAAACDkSPAAAAAAAACEHAkeAAAAAACAkCPBAwAAAAAAEHIkeAAAAAAAAELO63cAp6JPfOITGhsb63cYAIA+2LdvnyRp1apVfY4EvbRmzRpdd911/Q4DAACcQkjw9MHY2Ji+/+hjqqSX9TsUAMAii+YmJUkHClyCT1bR3ES/QwAAAKcg7i77pJJeptmXvrnfYQAAFlnqR1+WJK4BJ7HaOQYAAFhM/AYPAAAAAABAyJHgAQAAAAAACDkSPAAAAAAAACFHggcAAAAAACDkSPAAAAAAAACEHAkeAAAAAACAkCPBAwAAAAAAEHIkeAAAAAAAAEKOBA8AAAAAAEDIkeABAAAAAAAIORI8AAAAAAAAIUeCBwAAAAAAIORI8AAAAAAAAIQcCR4AAAAAAICQI8EDAAAAAAAQciR4AAAAAAAAQo4EDwAAAAAAQMiR4AEAAAAAAAg5EjwAAAAAAAAhR4IHAAAAAAAg5EjwAAAAAAAAhBwJHgAAAAAAgJAjwQMAAAAAABByJHgAAAAAAABCjgQPAAAAAABAyJHgAQAAAAAACDkSPAAAAAAAACFHggcAAAAAACDkSPAAAAAAAACEHAkeAAAAAACAkCPBAwAAAAAAEHJevwM4Fe3bt0+RfK7fYQAAAAAAcEr4xCc+IUm67rrr+hxJ75Dg6YPZ2VlZtdTvMAAAAAAAOCWMjY31O4Se4ytaAAAAAAAAIUeCBwAAAAAAIORI8AAAAAAAAIQcCR4AAAAAAICQI8EDAAAAAAAQciR4AAAAAAAAQo4EDwAAAAAAQMiR4AEAAAAAAAg5EjwAAAAAAAAhR4IHAAAAAAAg5EjwAAAAAAAAhBwJHgAAAAAAgJAjwQMAAAAAABByJHgAAAAAAABCjgQPAAAAAABAyJHgAQAAAAAACDkSPAAAAAAAACFHggcAAAAAACDkSPAAAAAAAACEHAkeAAAAAACAkCPBAwAAAAAAEHIkeAAAAAAAAEKOBA8AAAAAAEDIkeABAAAAAAAIORI8AAAAAAAAIUeCBwAAAAAAIORI8AAAAAAAAIQcCR4AAAAAAICQI8EDAAAAAAAQciR4AAAAAAAAQo4EDwAAAAAAQMiR4AEAAAAAAAg5r98BAAAAnEwi+SmNjU1ry5Yt/Q4FAAAExsbGlEql+h1GT4XiCR4ze4+Z7TSznePj4/0OBwAAAAAA4IQSiid4nHOfkvQpSdq4caPrczgAAAAdVZNDWnPeCt122239DgUAAAROhSdrQ/EEDwAAAAAAADojwQMAAAAAABByJHgAAAAAAABCjgQPAAAAAABAyJHgAQAAAAAACDkSPAAAAAAAACFHggcAAAAAACDkSPAAAAAAAACEHAkeAAAAAACAkCPBAwAAAAAAEHIkeAAAAAAAAEKOBA8AAAAAAEDIkeABAAAAAAAIORI8AAAAAAAAIUeCBwAAAAAAIORI8AAAAAAAAIQcCR4AAAAAAICQI8EDAAAAAAAQciR4AAAAAAAAQo4EDwAAAAAAQMiR4AEAAAAAAAg5EjwAAAAAAAAhR4IHAAAAAAAg5EjwAAAAAAAAhBwJHgAAAAAAgJAjwQMAAAAAABByJHgAAAAAAABCjgQPAAAAAABAyJHgAQAAAAAACDkSPAAAAAAAACFHggcAAAAAACDkSPAAAAAAAACEnNfvAE5FqVRK00XX7zAAAAAAADglrFmzpt8h9BwJnj5YtWqVDhSe73cYAAAAAACcEq677rp+h9BzfEULAAAAAAAg5EjwAAAAAAAAhBwJHgAAAAAAgJAjwQMAAAAAABByJHgAAAAAAABCjgQPAAAAAABAyJHgAQAAAAAACDkSPAAAAAAAACFHggcAAAAAACDkSPAAAAAAAACEHAkeAAAAAACAkCPBAwAAAAAAEHIkeAAAAAAAAEKOBA8AAAAAAEDIkeABAAAAAAAIORI8AAAAAAAAIUeCBwAAAAAAIORI8AAAAAAAAIQcCR4AAAAAAICQI8EDAAAAAAAQciR4AAAAAAAAQo4EDwAAAAAAQMiR4AEAAAAAAAg5EjwAAAAAAAAhR4IHAAAAAAAg5EjwAAAAAAAAhBwJHgAAAAAAgJAjwQMAAAAAABByJHgAAAAAAABCjgQPAAAAAABAyHn9DuBUFc1NKPWjL/c7DADAIovmDksS14CTWDQ3IWlFv8MAAACnGBI8fbBmzZp+hwAA6JN9+8qSpFWrSACcvFZwrQcAAIuOBE8fXHfddf0OAQAAAAAAnET4DR4AAAAAAICQI8EDAAAAAAAQciR4AAAAAAAAQo4EDwAAAAAAQMiR4AEAAAAAAAg5EjwAAAAAAAAhR4IHAAAAAAAg5EjwAAAAAAAAhBwJHgAAAAAAgJAjwQMAAAAAABByJHgAAAAAAABCjgQPAAAAAABAyJHgAQAAAAAACDkSPAAAAAAAACFHggcAAAAAACDkzDnX7xiOi5mNS9rb7zheBMslHep3EMAJhnYBtKJdAK1oF0Ar2gXQ6mRtF+c450abJ4YuwXOyMLOdzrmN/Y4DOJHQLoBWtAugFe0CaEW7AFqdau2Cr2gBAAAAAACEHAkeAAAAAACAkCPB0z+f6ncAwAmIdgG0ol0ArWgXQCvaBdDqlGoX/AYPAAAAAABAyPEEDwAAAAAAQMiR4AEAAAAAAAg5EjyLzMyuMLPHzWzMzG7odzxAL5jZ02b2iJl938x2BtOWmdk9ZrY7+Ls0mG5m9qdBm3jYzF7VsJ53BuV3m9k7G6a/Olj/WLCsLf5eAt2Z2WfM7KCZPdowreftoNM2gBNBh3Zxk5ntC64Z3zezNzfM+/2gjj9uZm9smN72fsrMzjWz7wTTP2dm8WB6Ing/FsxfvTh7DMzPzM4ys2+a2Q/NbJeZbQmmc83AKatLu+Ca0QUJnkVkZlFJt0t6k6QLJL3dzC7ob1RAz/ycc+4VzrmNwfsbJN3nnFsr6b7gveS3h7XBv/dI+qTk33BI2irppyRdJGlrw03HJyX9esNyV/R+d4Dj9ldqrZuL0Q46bQM4EfyV2vfZHw+uGa9wzn1ZkoJ7pGskrQ+W+TMzi85zP/WxYF1rJB2R9K5g+rskHQmmfzwoB5woypL+k3PuAkmvkfTeoE5zzcCprFO7kLhmdESCZ3FdJGnMObfHOVeUdKekq/ocE7BYrpJ0R/D6DklXN0z/rPN9W9ISM1sp6Y2S7nHOTTjnjki6R9IVwbwh59y3nf8r8Z9tWBdwwnDO3S9pomnyYrSDTtsA+q5Du+jkKkl3OucKzrmnJI3Jv5dqez8VPJFwsaTPB8s3t7Fau/i8pEtqTzAA/eac2++c+27welrSY5JWiWsGTmFd2kUnXDNEgmexrZL0bMP759S9kgJh5SR93cweMrP3BNNWOOf2B68PSFoRvO7ULrpNf67NdCAMFqMddNoGcCJ7X/BVk880PHFwvO1iRNJR51y5afqcdQXzJ4PywAkl+CrIKyV9R1wzAEkt7ULimtERCR4AvfCzzrlXyX8U8r1m9rrGmcH/Hrm+RAacIBajHdDWEBKflHS+pFdI2i/pv/U3HKA/zGxA0j9I+m3n3FTjPK4ZOFW1aRdcM7ogwbO49kk6q+H9mcE04KTinNsX/D0o6QvyH418PnhEWMHfg0HxTu2i2/Qz20wHwmAx2kGnbQAnJOfc8865inOuKunT8q8Z0vG3i8Pyv6riNU2fs65g/nBQHjghmFlM/ofYv3XO/e9gMtcMnNLatQuuGd2R4FlcD0paG/xad1z+j0Bt73NMwIvKzDJmNlh7LelySY/Kr+u10RzeKelLwevtkq4NRoR4jaTJ4FHhr0m63MyWBo9eXi7pa8G8KTN7TfBd2Gsb1gWc6BajHXTaBnBCqn24DPy8/GuG5Nfla4LRTM6V/8Ow/6oO91PB0wfflPTWYPnmNlZrF2+V9I2gPNB3QT/+/0t6zDl3a8Msrhk4ZXVqF1wzurOQxHnSMH8Yt/8uKSrpM865j/Q5JOBFZWbnyX9qR5I8SX/nnPuImY1IukvS2ZL2Snqbc24i6Lz/h/xfu89J+lXnXG1o9V+T9AfBuj7inPufwfSN8kdiSUn6iqTrwtLp4tRhZn8v6Q2Slkt6Xv7IJl9Uj9tBp7bW8x0GFqBDu3iD/EftnaSnJf1G7TdBzOwPJf2a/NFUfts595Vgetv7qeAadKekZZK+J+lXnHMFM0tK+mv5v+EwIeka59ye3u8xMD8z+1lJ/0fSI5KqweQ/kP97I1wzcErq0i7eLq4ZHZHgAQAAAAAACDm+ogUAAAAAABByJHgAAAAAAABCjgQPAAAAAABAyJHgAQAAAAAACDkSPAAAAAAAACFHggcAAJz0zKxiZt83sx+Y2XfN7LULWGZmMWIDAAB4MXj9DgAAAGARzDrnXiFJZvZGSR+V9Pr+hgQAAPDi4QkeAABwqhmSdESSzGzAzO4Lnup5xMyuai7cqYyZrTazx8zs02a2y8y+bmapYN4aM7u34Ymh84Ppv2tmD5rZw2Z28yLuMwAAOMmZc67fMQAAAPSUmVUkPSIpKWmlpIudcw+ZmScp7ZybMrPlkr4taa1zzpnZjHNuoFMZSedIGpO00Tn3fTO7S9J259zfmNl3JP1X59wXzCwp/z/VflbSWyX9hiSTtF3SHznn7l/MYwEAAE5OfEULAACcChq/ovXTkj5rZhvkJ1r+i5m9TlJV0ipJKyQdaFi2UxlJeso59/3g9UOSVpvZoKRVzrkvSJJzLh9s93JJl0v6XlB+QH6iiAQPAAB4wUjwAACAU4pz7l+CJ3FGJb05+Ptq51zJzJ6W/5RPo1/uUqbQUK4iKdVl0ybpo865v3jhewEAADAXv8EDAABOKWb2UklRSYclDUs6GCRufk7+166aLaRMnXNuWtJzZnZ1sL2EmaUlfU3Sr5nZQDB9lZmd9qLtGAAAOKXxBA8AADgVpMys9lUqk/RO51zFzP5W0g4ze0TSTkk/arPsQso0+/eS/sLMtkkqSfpF59zXzexlkv7FzCRpRtKvSDr4QnYMAABA4keWAQAAAAAAQo+vaAEAAAAAAIQcCR4AAAAAAICQI8EDAAAAAAAQciR4AAAAAAAAQo4EDwAAAAAAQMiR4AEAAAAAAAg5EjwAAAAAAAAhR4IHAAAAAAAg5EjwAAAAAAAAhBwJHgAAAAAAgJAjwQMAAAAAABByXr8DOF7Lly93q1ev7ncYAAAAAAAAi+6hhx465JwbbZ4eugTP6tWrtXPnzn6HAQAAAAAAsOjMbG+76XxFCwAAAAAAIORI8AAAAAAAAIRcTxM8ZnaFmT1uZmNmdkOb+Qkz+1ww/ztmtrqX8QAAAAAAAJyMevYbPGYWlXS7pMskPSfpQTPb7pz7YUOxd0k64pxbY2bXSPqYpF/qVUwngqOzeT1xIKvnpwpaMZTQutMzWpJK9jusF0216vT04ayen8prxVBSq0cyikTsBZftl2rV6alDWe2dyCoT97RiKKEzl6T1zJHcccc93/7W5h/OFhSPRlSsVBWPRpTNV5SIRTSZL2okk9T6lUPyvEhL+VyxohVDSZ05nNIPD0xp39FZjQzElYl7ms6XNTqQ0GyprCOzJeVLFZ02mFAsGtF0vjwnnmrV6ZkJv47mS2Wl454mZ0saSsVUKFd0xnBaZy1J6bHnp3Q4W9BQMq6qc0pEIzo6W1TciypbKOuckYzinunwTFHlalWFslOuWNbyTEIV55SMRVWuVHVopqh0PKqRgZhikajGZwpKxz1Vnb//R2dLkpxi0agOThU0OpTQklRUhZJTrlRRqeKULZS1YighSYpaRE5V5YpVTWSLOnskLeecfjyZ13Aqpmq1qnTMU9U5FStOh7NF/1hETPun8lo+kNBMoaRM3JMXjehQEM9AIqpcsaKZQlnDqZjiwbxkLKrhpKdSVXp+Kq/lgwkVy2WZIkrETLGIf1zS8ZiO5opKxqIaSHgqVSsyRTQ+XdBosP0fT+Y1OphQ1KTD2ZIGU1ElolGVqxVFFNH4TFEDSU/JmMmziErVqiayJS1Jx5T0oiqUK5KkUsU/1oMpT14kosMzRY0O+OudKZWViEZ1KFjXUMLTUMp0aKaiA1MFnTaY0FAqqnyxqtlSRTOFigaTnvLlspamYipWpEMzBS0fSGi2WFbci2q2VFYyFlXUTPFoRJGIFI2YZotVjc8UNZKJKWKmo7mSBlOeKtWKUrGYssWKcsWyhpKe0nFP+VJFQ0lP0/mKDs74sdTqoHPy4xtKKBOP6tmJnEYGEqqqInNRHZop6PQhvy/dP5XX6EBcAwlP04WyDs0UNZKJKx2PKh41zRQrmi1W5JxTOu7pcLaopemYf6yyBQ0mYyqWK0rFPU3lS1qSiqlcDY5pIqZD2aIGE56G056KJaf9k3mdsSSpYqWq6dmyhtIxTc6WNJjwtCTlaTJf9s/BoH/MhpIxFSpVTc2WtSwTU8VVFI94milWJFUVj3o6NOPXi1KlrLjnqViuKlsoa2kmpohFdGi6oHTCUzzq9yFxL6J82d+vdMxv80PpmGbyJQ0mY0rFIqo6JzlTsVrVbLGiQrmq4ZQf65JUTGbS+HRRo4NxxaMRHckVlUnEgjYQ1VDSPw+1ejpbLMvMNJDwlElENFusarrgt5HRgbjKVafJ2ZKWZWIyZzqaL2koGdNUvqTBRExTsyUNp2PKFUtKx2MqVcoaiMc0W67Wz1kmHlWp4tejZZm4SpWKUjFPuWJF0/myVg4n5Jw0PlPQkrTfF03OljSSiatUqWoyX9ZpgwmVK1Xli/45nS6UlIr5/dqKIX/ekZzfx+VLZaUTnlxVmsr7bX2mUJIXiWgw6WkgHtGR2YqmC6XgOJe0NB1XtlhSNBJVJh5R3ItqOl/W4WxRpwf90kyhpITnb3N0IC4v6Hun82UtH4grVywrFfdUqpQV86KSMx3NFTWY9LQ0HdPkbEUHp/37hpFMVBPZisZnihpKelqSimm6UNJ03m8rIwMxTecrej5oL8vSUR3JVXQkV9KydExHckWl4568iEkmJb2I8uWqpmZLOmckpanZY+seTHiazBc1kDjWXkcHEipWqjqSLWnlsH8dmSlUNJEtauVwXMWK6vc45WpFXiSqw9mClmcS8iKm547mdfpQQvFoRAdnChpO+XXstMGEEl5EByYLGgnqz0TQ1pKxqA7nilqSismLOJWrVu87yxV/G0dnSxpKecqXyvIiUUUjUiwakcnvjyrOqVj2+/wVgwnJqpLzrzFLUn7/PJyOq1KtanLW38+KKpKLzOnzUnFPE7milqXj9T6wUC5rMBFXuVrV0dmSlqXjikSk2WJVM4WyRjJxOTkdyZWUjkWVjEeV9Pzr9kS2pNHBuGZLZQ0n48qXqzoc9M9LUp6m8uXguuMpHvX7ulTMUyxqGgrm1/oXp6piFtVMsaxc0b/Ol6pVFUoVJWPesWMWnJeJbFEDCU+DSU8mp4qTimX/ujKU9BSLmeIRv+84NFNSOh7VYNLf9ky+oueDOulUVSIaVT5ouyuHkqrK6WjOb/OTs35dKZSr9fM7MuBpMlfRRK4U1PGSUrGoBhNRFSpO49N+uXTMb09LMjHNFisany5qOO1pIO737zPBvKj55ykT9IuxaESpmH+MC+WqSpWqUjFP4zMFrRz2rxWHZorKxKNKxCKaKfj90OSsf02tVKqKRaPyoqbpfFmzpYrOW55RoVLRxIzf3kYH44pFI/XzlSuWFfciSnn+NfaMpUlVKv79x1DSC/q7ikYyiY73gLV7xLOXpvXskZwOzuRVKjvlihUtSceUjkd1JFdUPBrVaYMJmUn7J48ts3ciN+ee9exl3bfTeO/XfL9bW7bdvKnZkn48mdfK4VT9vvSFqsV24GheMc90ZLakkXRcF54xrHg82pfPDWH4rAI06+WPLF8kacw5t0eSzOxOSVdJakzwXCXppuD15yX9DzMz55zrYVx9c3Q2r68/Oq4btz+qfKmqZCyibZs36PINoydFkqdadfrqrgO6/q7v1/fv1re9QlesP72lMzyesv3SLsbrL1unlcNJ/e7nHz6uuOfb39r8j331Mf3SxrP1uZ3P6Jc2nq0//cbuevn3X7xWn9v5Q1138VptvvAM3fv4wXr5WrmN5wzrbT95jm780rE6tnXTev39d/ZqMl/Sf3z9Gt28Y9ec/fmf//y0juSKuvVtr9DlL1uhb+0+qN3Pz+jOB5/ROy46Rx+/94k5MXzwi4/qfT+3Vp97cK8ufunp9Vjbxbxt83pFIv6Hxtvua96XZ3TNT56tz/7LXh3JFbV103r9+T+Nae/hWSVjEX30Fy7U+HRBX9+1X2951dm6+e5jcX/4qg0ycy3rvXnzej309CG9evVybd2+S0vTcV370+fMKXPTpvVKx03ZoptzLLZcsrYeywcuXadMIqpb/vEx5UtVnTOSajl2jeWbY9965Xr9w3ef0SUvO10jmZiyxao+9tXv1Zf9gze9VKm4pw81nKfm9f39d/bqiYMz+uO3Xqh8ybWUXZLyVKo4ff6h5/TWV59Zr2vZYmXO/jae4xuueKmWDcT1nz//UNdYPnzVBpUrFd1892P1aX/45pfpoFfU1u27Ws5j7fz/8k+do2WZmE4fTmj/0aI+9KVHO56DYjmn//KVH9WnfewtF2oo5Wnv4ZxubNjGBy5dp1QsMqfszZvX66uP7Nd0oaRf3Hj2nJhqx3HVkkTLvK2b1mvFUFxjB7P62+/srdfXdjE279u7fuZcFStOf/L1x+dsazDp6a4Hn9WVP3GGbr1nblv5xo8O6G0bz56zPzdtWq9nj8zW61YyFtEfveVCHZiabqjr363P++jPX6iJXFZ//LXHtTQd16/+zOo529lyyVqNZGJyMv3Zt8Za2uAHLl2nv/vXvfqtN6zxP7RUnfYezrXd1//4+jX1evdHb7lQhbLTh/7mu3O2lYlH9cl/2qMjuWJ9uV//d+dpSTquZydyLXXv7h/8WG+6cKXufLBzP1E7Vr/2M+fpmYnCnHa2ddN6Dac8/fm3ntRkvqQPXLpO+yendNt97c9bYzua06aufJmyxar++ttPdz3vv3/FS1WoVFvOZW0/k7GoPvGN3R36Z79PO2NJUrfe84SKZadrf/qc+r7Xtvmbrz+vpZ3etGm9Pv/Qbr311WfLi0of/KJ/DC6/YLkufdnKOXVo2+YNuv1bu7X38Gzbvmnb5vW6/Vt+f1Rb/vZvjekdF52jLfc+0XI+JSkSMT35/JQmZ5e29DXL0jEVmtpr7djGPdN737BGN27fpXWnDejtP3VOPZZzRlL6rTesads+a/1cVE7X/f335sz/yiP7W9rTlkvWKh2L6vM79845Hu32v/FcZOJRLQ+S5hO5cstxumvnM7rsgpVzrnONMd5y9QZ94hu75/Ttf37/rvr75n6idk2Le9b1mrHlkrU6fTipUrmij987piO5oj7+tp/Qj49O14/XfNedbZsvkGQtdUOq6sbtPzzWX266QE6mm3Z8t+N52bZ5vZYNxHV4pthyvmrXmlq7v/0dr9ShpnIfe8uFKpSruvFLHWLddIEOZ4stx//ex/brFWeN1NtSu9i2blqvrz+6Xz+9Znm9TjQem079YiYe1dJMXDP5kv78/j1d232tfn3mgR/Wz+Vvvn6NvOix+5el6bjef/H5Ojpb7tjnNNa9rzyyX2+6cGVL2YGEp7/8vz/Q713xspZ7wMZ7xFuu3qBqtarD2VJLv5qIRvSZB56q1/FP/tMexT3TdcE9WuP21q4Y0MUvWdFxO7V7v68/9vyc6bVl37D2tDnz2tXLW67eoKt/YtULSvK0i+39F6/VR3Y+o/f+3Fpt3rBS39g9vqifG8LwWQVop5df0Vol6dmG988F09qWcc6VJU1KGulhTH31xIFsPbkjSflSVTduf1RPHMj2ObIXx9OHs/VOUPL37/q7vq+nD7fu3/GU7Zd2Md56zxPafXDmuOOeb39r8698+Sr96Td21/82lq9N/+AXH9XDP56cU75W7trXnldP7tSWu3nHLr37defrypevql+QG/fnF151Zj2eXfsn9fBzk7rtPn9btZve5hg+9KVHde1rz5sTa7uYb9y+S0nPq9+cNK/ntvt217d/845duvLlq+plnjqU1a33PKFrX3tePblTm/ehLz3adr1bt+/S1a869qH+F151ZkuZm3bs0pJ0ouVYNMby8Xuf0MHpQn1+u2PXLfab796la197nm67b7fS8Zg+9tUfzVn2ULZY/xDVaX3vft35ypeqGk7F25bdP1XQoWxR737d+TqULdb/Ne9v4zn+r1/9kcaa6m+7WD70pUe1f6owZ9r4TKF+XJvPY+3vrfc8oaTnKWrR+jo7nYND2eKcaU+OZ5WOxeofVmrTP37vEy1lt27fpf/ws+fq2tee1xJT7Ti2m3fzjl3yIhHdes8Tc+pruxib9+1QtlhP7jRu6+B0Qe9+3fn1DxeNy1/72vNa9uemHbvm1K18qaqx8c51/anDfnKnFmfzdmp1bOv2XW3b4Mfv9fd16/ZdKn7Ai/gAACAASURBVJWdqlV13NfGejc2nm1b7w5li/X6VFvu4HRBTzw/3bbuvft159f7k25927WvPU9Vp5Z2dvOOXapWVe/D9hzK1rfT7rw1tqPG1/unCvqTrz8+73k/nCu2PZe1/fzgFx/t2j/fdt9uPTme1ZUvX1Vff/M227XTm3b4fcZNO/w+szbvl19zbksdunH7o/X+pl3fdOP2Y/1Rbfl2/XntfB7KFnVwuqA3Xriq7TnfN5lvaYO1Y3vly1fV43v3686fE0ut3nXr59KJWMv8du3ptvt263Cu2HI82u1/47k4lC2qWpVKlda6deN2/5i3Oy61GGvnu14f757b1zf3E43Hpds147b7duupQ1ml47H6tEpVc47XfOtIx1v7yxu3P6p0fO4x3TeZ103znJcbt+9SPBppe75q15radmNtyj05nq0nd9rGmoi1Pf6//Jpz57SldrHdvMPv7xvrROOx6dQvHsoWtfvgjPZPFeZt97X61Xgua22xsb/ZP1Xo2uc01oNa39dcdnzGj6fdPWBj2Q9+0T+X7frVWqyNfXLt/rB5ew8/N9l1O7V7v+bptWWb57Wrlx/84qPatX9SL0S72GrH88YvPapH2sTY688NYfisArQTih9ZNrP3mNlOM9s5Pj7e73D+zZ5v+MBUky9V9fxUoU8Rvbien8q33b+D0/kXVLZfOsVYbXq+bCFxz7e/tflmmvO3uXxt+oGm8jWzhXLb5fyvUnReZ+31/sm8qm5hMdS2NV/M2WL7mBqXa45FUj2OTvuU7TD90MyxdtYppolsad5j0XieF3LsGmOvHfNOcdb2rdv6ZotlSeoYa9X565ktlOuvF7Le5vrbaZmFlms+/9liWePT85+Ddus/OL3wNnc0V+pYN8w6t4UjwfFsjGu+um7W/TjNdqjjnaZ3OrbtYm7c7nxtbL79yBbLHdtNvV0H9a7b/jbX+251b7a4sH5itkts2WK53oct5Hi0a5ft+rV2y3er5wvtG2vHqN0+d6tL9T4jOAeS6vW10z7Odwza1ffGco19x3iX9teuDTbuo9Ta5hZyfhr3tX4cOtSDqms9Hgs5F93qfbc+pPl1t/fNfxey77XYatOaY5xvHd3aS6Pm+tZpvZ3qWu3817bb7po037WnU6xHcws7n93KLaRuL7R8u+vZQtpuc32Zrx7XyjTfAzaX7XT/1LiO5v6mXdn5trN/snPbb57XaTsHJl/Y/Xun2I7d97b/DNXLzw1h+KwCtNPLBM8+SWc1vD8zmNa2jJl5koYlHW5ekXPuU865jc65jaOjoz0Kt/dWDCWUjM095MlYpP7bIWG3YijZdv9OG2z9+tnxlO2XTjE2P5W5kLjn29/G+c1/G8s75/89vU15SUonvLbLpeJe13XWXq8cTilqC4uhcVvdymfi7WOqradx+41fzqzF0WmfMsn200cH5razdmWWZWLzHot257lb+cbYa8e8U5yNx7jT+mrnrFOsEZMi5p/zqKn+73j3q9MyCy3XeB5r53t0cP5z0G79pw0uvM0tScc61g3nOreFpQ3Hc74YG/et23FKd6jjnaZ3OrbtYm7e7nxtrNt+ZOJex3ZTK1Ord932t7ned6t76TaxdSrXKbZM3OsY10LbZad+7Xja5kL7xuZj1Fy+0zbqfUb82Lfn5+ur5jsGyzrU99r7Wj8Smaf9tWuDzfvYqc11W65xX2vTOq0nYp2PR7tt1JbpVu+79SHNr7u973RN67beWmy1aZ1i7LSObu2lUaf61vx+6TzXmnZ1ar5tzBfrkvTCzud85ear2wst3+56tpC221xf5qvHtTLt7gEby3a6f2pcR7v+prnsfNtZOZzquGynec3vTx9+YffvnWI7dt/b/jNULz83hOGzCtBOLxM8D0paa2bnmllc0jWStjeV2S7pncHrt0r6xsn6+zuStO70jLZt3jDnZmvb5g1ad3qmz5G9OFaPZHTr214xZ/9ufdsrtHqkdf+Op2y/tIvx+svWae1pA8cd93z7W5u/4wf79P6L19b/NpZ//8VrdffD+3TL1Rv08jOG55SvlbvjgT3adtXcOrZ103r95f1PascP9mnrpvUt+/O/v/tcPZ71K4d04ZnD2nKJH8MHLl3XNoYPX7VBdzywZ06s7WLetnm98uWytlzSfl+2XLK2vv2tm9br7of31cusXp7R9Zet0x0P7NHWK+fG/eGrNihfal3vzZvX6wvffUY3b/bL/8NDz7WUuWnTeh3NFVqORWMsH7h0nU5rSFK0O3bdYt965Xp99oE92nLJWuUKJf3eFS+ds+xIJq4PN52n5vX95f1PKhmLaHK22LbsyqGElmfi+vT9T2okE6//a97fxnN8wxUv1Zqm+tsulg9ftUErG26mkrGIlg8k6se1+TzW/l5/2Trly2VVXKW+zk7nYHkmPmfaeaMZ5UolbWvaxgcuXddS9ubN6/VX//cp3fHAnpaYasex3bytm9arXK3q+svWzamv7WJs3reRTFy/c/lLWrZ12mBCn77/SV1/WWtbueOBPS37c9Om9XPqVjIW0fmjnev66pGMfveNL6nH2bydLZesVa5Y0s2b17dtgx+4dJ3ufnifbt68XjHPFDF13NfGenf+aKZtvVueidfrU2250cGE1q4YbFv3Pn3/k/X+pFvfdscDexSRWtrZ1k3+73jV+rBzl2fq22l33hrbUePr04cS+p3LXzLveV+Wjrc9l7X9vOXqDV375y2XrNX5oxnd/fC++vqbt9mund60ye8zbtrk95m1eX/z7ada6tC2zRvq/U27vmnb5mP9UW35dv157Xwuz8R12mBCX31kX9tzvmo42dIGa8d2xw/21eP79P1Pzollxw/2dWyftXObK5Ra5rdrT1suWauRdLzleLTb/8ZzsTzj/9hxLNJat7ZtXq87HtjT9rjUYrzl6g0tfXvj++Z+ovG4dLtmbLlkrc5dnlGuWKpPi5rmHK/51pErtPaX2zZvUK4495ieMZzUTfOcl22b16tYqbY9X7VrTW27pTblzhvNaNtVXWLNl9oe/7/99lNz2lK72LZu8vv7xjrReGw69YvLM3GtPW1AK4cS87b7Wv1qPJe1ttjY35w+lOja5zTWg1rf11x2dCChux/e1/YesLHsLVf757Jdv1qLtbFP3vED//6weXsvP3O463Zq937N02vLNs9rVy9vuXqD1q8c1gvRLrba8dx21QZduHJ40T83hOGzCtCO9TKfYmZvlvTfJUUlfcY59xEz2yZpp3Nuu5klJf21pFdKmpB0Te1HmTvZuHGj27lzZ89i7rVTZRStg9N5nTa4sFG0FlK2X2ojBzwzkVW6aRSt4417vv2tzZ/IFhRrHEWrUFHci2g6X9SyTELrVw7PGUWrVr7bKFozBX/0qtooWoVStT76w3yjaGXinj86STKmYqWilQ2jaE1kCxpM+qODxCJ+MqJ5FK2JmaJK1aqKZadssayRTEJO/qhb5arrMIpWVM45xYJRtExOXjSqg9MFjQ4ktCTdOopWbTSJiJkkd2wUrWVpOfkjHQ0lY6q6uaNoTWSL9VGsDkzlNTKQULZQCkaZiehw1o8vE4yilS1UNJTyglG0ikrGInNH0RpIqFjxR9GKe1YfCSwd93Q05994D8Q9lVyHUbQGEopGglG0ksEoWq55FK2IPDOVqv5j9cNtR9GqaDAZlRftPorWYMLTcDCK1vNTfixDyaj/iHnJ39+BpKdCuaIlKa/tKFr5UkUJL6JopHUUrUMzRS1rGUXLH80kW6xotlDRQCqqTNMoWuMz/rnOl4+NolWLLxOP6tkj/ihaThUpGEVrxVBSJunAVF7LG0bROhyMwJSORRX3WkfRmsgWtaQ+ipY/clFtFK3pfEnDyZgqzj+mAwl/1K2BhKfhlKdi2Wn/VF5nDDeMopXyR4oaWMAoWkvTMVVVVTwSnTuKVtbf/1KlorgXDUbRqmhpxlNE/jlNJaJzRtEqlKrKlcpKxTzN5P04ssWSBuL+/347tRlFKxnTZL6k4VRMEQtG0RqIK+61jqI1mPCfDGgcRUtmGowHo2iVqpoJRtFaPhBXpeo0OVvWkrSniIJRtBL+iE8DtVG0UjHlgpHSSpVKMIpWpX7OaqNoHZopamkmrnLFHw2oPorWUEJO0viMP8KSUzByVzquUrWqqdmKRgf90Y3yJX8ErplCScnaKFqDCZWr/uhGg0E9T8WjkpOmZssaTseULZQVjZgGE54GEv4oWjPBSFzHRtEqKxqJzBlFayJb1GlDCZmkmUJZCS+qqdmSlg/E5UUi/ghAwQhLx0bRqsiLRmTy28tAIqplmfajaNXa8NL6KFqVel9aH0VrMKFlGX8UraPBaEVHcv5oSF5Qd46NolXWOSNJTc366x5sHEUrHlOuVFGuUNHywbiKFf9rMyuC0bBmChVN5IpaOZRQseJ0cNrfdqVaUTQS1US2oJFgFK19k3l/xKymUbRqT182j6I1kPCUikU1kStquHkUrYFjI0IdG0WrIi8SUTQiedGIIpo7ilatz49YVW7OKFp+X1qp+seiNkqfXESHZ/z4Z8t++zqSK2rpnFG0KhpIxOojcC1Nx+qjaGULZS0LRtE6mvOTd6l4VMloRLmSP7rZSCaufLlhFK1aH5P0+7Dm604qHlUs6tfJWh83OpCQs7mjaI0OJFR2VRXLFSW81lG0jmSLyrQZRetIzu+/4l4wipbaj6JVO8+yquLBKFqHZ4paMZT022LOH8VvMl/S6YP+6GsHpgoaycS1LONpavbYKFpTsyUlu42ilY5pthSMopXylEn49zbZfEXDGa8+itZAwo8vFo0oGYvU+7o5o2gNJSWT348Go2hlG0fRSvn3Cl5kYaNoTcwUlamNohWNKBULRtFaklSl6rR/sqCBZFRLUv4+LOsyilbtHrHjKFqxqI7OFhVrGEXrwNSxZfZO5Obcs3YaRav5XrTd/W7zKFqN86ZmS9o/mdfpw8n6fekLVR9FazKvWNR0dNbvX1/eNIrWYn5uCMNnFZy6zOwh59zGlulhe2Am7AkeAAAAAACAf6tOCZ5efkULAAAAAAAAi4AEDwAAAAAAQMiR4AEAAAAAAAg5EjwAAAAAAAAhR4IHAAAAAAAg5EjwAAAAAAAAhBwJHgAAAAAAgJAjwQMAAAAAABByJHgAAAAAAABCjgQPAAAAAABAyJHgAQAAAAAACDkSPAAAAAAAACFHggcAAAAAACDkSPAAAAAAAACEHAkeAAAAAACAkCPBAwAAAAAAEHIkeAAAAAAAAEKOBA8AAAAAAEDIkeABAAAAAAAIORI8AAAAAAAAIUeCBwAAAAAAIORI8AAAAAAAAIRcTxM8ZnaFmT1uZmNmdkOb+deb2Q/N7GEzu8/MzullPAAAAAAAACejniV4zCwq6XZJb5J0gaS3m9kFTcW+J2mjc+7lkj4v6Y96FQ8AAAAAAMDJqpdP8Fwkacw5t8c5V5R0p6SrGgs4577pnMsFb78t6cwexgMAAAAAAHBS6mWCZ5WkZxvePxdM6+Rdkr7SboaZvcfMdprZzvHx8RcxRAAAAAAAgPA7IX5k2cx+RdJGSX/cbr5z7lPOuY3OuY2jo6OLGxwAAAAAAMAJzuvhuvdJOqvh/ZnBtDnM7FJJfyjp9c65Qg/jAQAAAAAAOCn18gmeByWtNbNzzSwu6RpJ2xsLmNkrJf2FpM3OuYM9jAUAAAAAAOCk1bMEj3OuLOl9kr4m6TFJdznndpnZNjPbHBT7Y0kDkv6XmX3fzLZ3WB0AAAAAAAA66OVXtOSc+7KkLzdNu7Hh9aW93D4AAAAAAMCp4IT4kWUAAAAAAAD825HgAQAAAAAACDkSPAAAAAAAACFHggcAAAAAACDkSPAAAAAAAACEHAkeAAAAAACAkCPBAwAAAAAAEHIkeAAAAAAAAEKOBA8AAAAAAEDIkeABAAAAAAAIORI8AAAAAAAAIUeCBwAAAAAAIORI8AAAAAAAAIQcCR4AAAAAAICQI8EDAAAAAAAQciR4AAAAAAAAQo4EDwAAAAAAQMiR4AEAAAAAAAg5EjwAAAAAAAAhR4IHAAAAAAAg5EjwAAAAAAAAhBwJHgAAAAAAgJDraYLHzK4ws8fNbMzMbuhS7i1m5sxsYy/jAQAAAAAAOBn1LMFjZlFJt0t6k6QLJL3dzC5oU25Q0hZJ3+lVLAAAAAAAACezXj7Bc5GkMefcHudcUdKdkq5qU+7Dkj4mKd/DWAAAAAAAAE5avUzwrJL0bMP754JpdWb2KklnOef+sduKzOw9ZrbTzHaOj4+/+JECAAAAAACEWN9+ZNnMIpJulfSf5ivrnPuUc26jc27j6Oho74MDAAAAAAAIkV4mePZJOqvh/ZnBtJpBSRskfcvMnpb0Gknb+aFlAAAAAACA4+N1m2lm13eb75y7tcvsByWtNbNz5Sd2rpH0joZlJyUtb9jWtyT9jnNu5/xhAwAAAAAAoKZrgkf+UzaS9BJJPylpe/B+k6R/7bagc65sZu+T9DVJUUmfcc7tMrNtknY657Z3Wx4AAAAAAAALY865+QuZ3S/p/3POTQfvByX9o3PudT2Or8XGjRvdzp085AMAAAAAAE49ZvaQc67l520W+hs8KyQVG94Xg2kAAAAAAADos/m+olXzWUn/amZfCN5fLemO3oQEAAAAAACA47GgBI9z7iNm9hVJ/y6Y9KvOue/1LiwAAAAAAAAs1PEMk56WNOWcu03Sc8HoWAAAAAAAAOizBSV4zGyrpN+T9PvBpJikv+lVUAAAAAAAAFi4hT7B8/OSNkvKSpJz7sc6NoQ6AAAAAAAA+mihCZ6i88dTd5JkZpnehQQAAAAAAIDjsdAEz11m9heSlpjZr0u6V9Jf9i4sAAAAAAAALNRCR9H6EzO7TNKUpJdIutE5d09PIwMAAAAAAMCCLCjBY2Yfc879nqR72kwDAAAAAABAHy30K1qXtZn2phczEAAAAAAAAPzbdH2Cx8x+U9JvSTrPzB5umDUo6Z97GRgAAAAAAAAWZr6vaP2dpK9I+qikGxqmTzvnJnoWFQAAAAAAABZsvgSPc849bWbvbZ5hZstI8gAAAAAAAPTfQp7guVLSQ5KcJGuY5ySd16O4AAAAAAAAsEBdEzzOuSuDv+cuTjgAAAAAAAA4XgsaRcvM3tX0PmpmW3sTEgAAAAAAAI7HQodJv8TMvmxmK81sg6Rvyx9JCwAAAAAAAH0232/wSJKcc+8ws1+S9IikrKR3OOcYJh0AAAAAAOAEsNCvaK2VtEXSP0jaK+nfm1m6l4EBAAAAAABgYRb6Fa0dkj7knPsNSa+XtFvSgz2LCgAAAAAAAAu2oK9oSbrIOTclSc45J+m/mdmO3oUFAAAAAACAher6BI+Z/WdJcs5NmdkvNs3+D/Ot3MyuMLPHzWzMzG7oUOZtZvZDM9tlZn+30MABAAAAAADgm+8rWtc0vP79pnlXdFvQzKKSbpf0JkkXSHq7mV3QVGZtsN6fcc6tl/TbCwkaAAAAAAAAx8yX4LEOr9u9b3aRpDHn3B7nXFHSnZKuairz65Jud84dkSTn3MF51gkAAAAAAIAm8yV4XIfX7d43WyXp2Yb3zwXTGq2TtM7M/tnMvm1mbZ8KMrP3mNlOM9s5Pj4+z2YBAAAAAABOLfP9yPJPmNmU/Kd1UsFrBe+TL9L210p6g6QzJd1vZhc65442FnLOfUrSpyRp48aN8yWWAAAAAAAATildEzzOuegLWPc+SWc1vD8zmNboOUnfcc6VJD1lZk/IT/gwBDsAAAAAAMACzfcVrRfiQUlrzexcM4vL/8Hm7U1lvij/6R2Z2XL5X9na08OYAAAAAAAATjo9S/A458qS3ifpa5Iek3SXc26XmW0zs81Bsa9JOmxmP5T0TUm/65w73KuYAAAAAAAATkbmXLh+0mbjxo1u586d/Q4DAAAAAABg0ZnZQ865jc3Te/kVLQAAAAAAACwCEjwAAAAAAAAhR4IHAAAAAAAg5EjwAAAAAAAAhBwJHgAAAAAAgJAjwQMAAAAAABByJHgAAAAAAABCjgQPAAAAAABAyJHgAQAAAAAACDkSPAAAAAAAACFHggcAAAAAACDkSPAAAAAAAACEHAkeAAAAAACAkCPBAwAAAAAAEHIkeAAAAAAAAEKOBA8AAAAAAEDIkeABAAAAAAAIORI8AAAAAAAAIUeCBwAAAAAAIORI8AAAAAAAAIQcCR4AAAAAAICQ62mCx8yuMLPHzWzMzG5oM/9sM/ummX3PzB42szf3Mh4AAAAAAICTUc8SPGYWlXS7pDdJukDS283sgqZiH5R0l3PulZKukfRnvYoHAAAAAADgZNXLJ3gukjTmnNvjnCtKulPSVU1lnKSh4PWwpB/3MB4AAAAAAICTUi8TPKskPdvw/rlgWqObJP2KmT0n6cuSrmu3IjN7j5ntNLOd4+PjvYgVAAAAAAAgtPr9I8tvl/RXzrkzJb1Z0l+bWUtMzrlPOec2Ouc2jo6OLnqQAAAAAAAAJ7JeJnj2STqr4f2ZwbRG75J0lyQ55/5FUlLS8h7GBAAAAAAAcNLpZYLnQUlrzexcM4vL/xHl7U1lnpF0iSSZ2cvkJ3j4Dtb/a+/Ow+yo6ryBf0+td+1Op5ckBEgI6RDsICgRGMdBIGw6kPC+Iq6g4jPo+4IgqDOO77xGgo4zPIqj44oPjKDiBuoArwuIIOMAsklYZIsJiYSks/R6l7q1nfePqrq5S9Xtm9BJ5ybfz/PwpG+tv3PqnFOni9v1IyIiIiIiIiLaDXvtAY+U0gVwGYBfA3gWQbasZ4QQa4QQK8PNPgbg74QQawH8AMD7pZRyb8VERERERERERHQg0vbmwaWUv0Dw8uTaZZ+u+flPAP56b8ZARERERERERHSgm+mXLBMRERERERER0avEBzxERERERERERB2OD3iIiIiIiIiIiDocH/AQEREREREREXU4PuAhIiIiIiIiIupwfMBDRERERERERNTh+ICHiIiIiIiIiKjD8QEPEREREREREVGH4wMeIiIiIiIiIqIOxwc8REREREREREQdjg94iIiIiIiIiIg6HB/wEBERERERERF1OD7gISIiIiIiIiLqcHzAQ0RERERERETU4fiAh4iIiIiIiIiow/EBDxERERERERFRh+MDHiIiIiIiIiKiDscHPEREREREREREHY4PeIiIiIiIiIiIOhwf8BARERERERERdTg+4CEiIiIiIiIi6nB8wENERERERERE1OG0vXVgIcSNAM4BsE1KuSxmvQDwZQBvBVAC8H4p5eN7K579xVjZwgtbixieqGBOl4klc7OYlU61ta/vS7y0s4jhCQtzulJY2JuFooi9HPH+G0e7auPNGBpsz0Nv1tytuH1fYtNIcN2KtosFs7M4oi/Y/9XWx+7u32r7xnWH92SwabTUtG203c5iBYaqoGR7GMinoCrAlvHmbTfsKOKV8RJMTcVE2UE+pWMgb0JRgB2TNizXQ8XxcURfFp4v8ZfRErKmhrLtIqVrmNNl4vDZzeVKKovr+nhmyzi2jFs4tCeNlKZie6ESW6boc21ZGreLrntKU+H7EiXHhecDjutjds7EhGXDUNW6OKNrvrOwq3wLeuuve9QmbNdD2lAxUrSR0lX0ZA10pzXsmLRRsj0UKi7mdJkQENgyYaEvZ0ARAsPjFnrzJrKGCsvxYLs+ihUP3RkdpqpgeLKCnKkGdek40BQNO4sVzErrSOsqbM9H2fZRdjzkUxrSugrXl9g+aaEvZ0JVBFQhMFKykTU1+NJHWtNQqLgwdRWOF5wzY2jYXqigJxPEXbZ9bJusIJfSkNIFulIaxsseJiwHs9IGJi0H+ZQGCaBUcZE2NGyfrKA3Z2Bul4mdRQfDExbmdadgOT4mLRddaQ1lx0VaU6GpCkaKNvJpHbbjIW1oKFQcmKoKU1eq5yk5HooVF4d0p5EzNWydsDC/J4VtEza2TliYkzeR1gVKjsSOQgV9ORPjZQe9WQP9eR1bx21MWA56MgZKtodJy0V/3oAnfUAqsBwXWVPDzqKNjK5B1wQyhoKKIzE8UcFAl4m0rqBoe3BcCU/6yBkathds9OZ1mIqKCctFoeKiL2cgpQftz/EkHN9D3tRhOT6Ktot8SoMAYGoqSo6LrK7BB1CsODA1DaMlG7OzUd3qcDwPuqpi+2QQh4DAaNHGrEywTlNVFCoOcqaO7ZMVzOtOQQhgeKKCrKEin9Lg+hI7CjbmdhlwPFTLZKgC2ydt5NMaLCfoowICk5aDrrSOSctBSlPRldZhOS7GSi66MzoKFQeaoiBnakjpCsZKNjRVxbbw/JDA9kIFOVODqSsoVBz0pE1YroexkoOsEbRl23NhqhoKdnB9Z2cNjJcdDORNVFwfY2UH3SkdE5aDfEqFgIChKbBcD5PloL2ZukBG02C5HlRFwHJ87CzamNtlwlAVbBopY063CQAYLzmYldEhALhSwnYlCpaL3pwBy3GRMYLylB0fjutjsuIiravIGCryKRUTZQ/DkxX05wyYqoJxy0Ha0DBZcZA3dOwoBm3P9Tx0pQxMVlzsLNiY152CpggMT1roThuYsIK2abkeCpaLWRkDJdtFSlchhA9IFROWg+60jvGSA1NXwn7rQUoF2yYrmJM3YWhBeW1PomQH9deVUjFZ9jBSstGTNeCH5SyGbdP1PahCxc6ijbypIZfSMGm5KNkuerMmxso20oaKXDhWer4I+mgq6BcpVYXj+8E1MXWMlsJ1qoKRooOMoSJtqFAF4HgSI0UbGVNDOmwHKV2DrijYGo4LmiIwYbkoVlzkTA2GLqArKiYrLgphP9WUcOwydOwsVjA7ayCtqxgr2ehO67A9WS2PpgApXYWhKXA9iaLtYWfBDvqOCPq7hA9DVcMx2au2f0NVkTOD8alY8ZBP6Rgr2ejNmgAkymEfzhoacqYKX0rsLDiYnTNQtj1I+EhpGrZNBjGmdAWqEFjSn4dhwUH9+AAAHklJREFUqNiwo4hNI0WkjaDvd5k6RksOulIaTE3F8ISFXHhNovG67HiYkzfh+BKTloPerImS7WGkaKM/b4bX3USXqWLzuAXb85DRgz6aT+ko2y4MTYUnPaQ1HZbjIWOoKNoeynZwjxkvO5iV1jEro2Ki7KNgu6g4PuZ2p2A5HlQhMG7Z6M2mcPScPF4eL2NnMbgnFSwPO4o2ukwNaUNF1lQwXgr6ydwuEwNdJl4Zq59zHdqdxp+2TmDzWBl9+aC/qIqCtKZCCKAYzkM0Fdg6vmuutWB2BhtHSsEcRFWDfpfSq/ezkuNhblcKk5aDV8YtzOtOV+ON7v++9KFAYLLiwFBVFMN273g+xi0Hh/VkUHE9vDJWRl/OhOP7GC06OGRWGksHdh1rIJ+CgMSfdxSDe31Gx9I5XVAUUb3OWVNDxfVwSHemOl9Imsc1zlvamT/GzZsANM39No6UsHGkiKyhYSBvQoj6+V3tPrXzv3ndKXg+sG2yeS5YOw8+ojcLX9Zv1xhHtGzDjmI1lrndJlyvvf2ma248HTrtd5/pdqCU/0Apx1SElHLvHFiIkwEUANyc8IDnrQA+guABz4kAviylPHGq4y5fvlw++uij0x3uPjFWtnDX09vx6dufhuX4SOkK1qxchjOX9U/5kMf3JX71zFZc9eMnqvted8FxOHto7j5tmPtLHO2Ki/fy0wbxo0c34R/OPrqtuH1f4rfPD+PF4QK+fM+LdeU+8+g5uOvZ4T2uj92tz1bbA6hbt6A3jY+cNoh/+vnTsTH/66+exTuWH46v/HZXma5YMYibH9yI0ZI95bZXnbEEh/aksXFnCV++50X0ZAxc9FcL6uooqut3vuFwDM7J4bSj5tQ9jIory+lHDeD2p17BP/386dhjfva8Zfj3376IjTvL1c8/fHgjTls6txpfXNkvP20Qv31uK95z0kJsHbdaxnnK4ADue3EbXhkto2h7sdf9vhe34cXhAn74yKbYepzfk8ZE2cFn/9+zdct/+dQWvOWYeXXH/Pz/PAauJ/F///Pp2GvxibOOQn/exN/f+iR6MgauPH0xdE2tK8eC3jQ+/ObFuPqOZ6rHWH3OEL55/7pqXTV+vuqMJTBVBZ//1XPVY1x26mBTHIfMSuG7D75UV8cpXcE//e3R0BQFn6k559Urh/D1+9bBdmXTtfvHs5ei4vm47u4Xmur+HcsPr16D3oyOMcut2+6qM5bguVfGceKRfVh9+zM1Y+gQvnbfrjJFx7v0lEH85tlX8DeDc1CouHVxXLNqGe7+0ys44Yh+fOGu56vLP3HWUejLGfiH256qOz4g8bX7/ox3n7AAX/rNC+jJGPhfb17U1DauWbUMZdvFDf+9ARe/8QiUnPr1V52xBClNQXdGh4DEzQ9uxNtefziuvvOZpnb69uWHY/Xtz8T2gdXnDOG2xzdVr0dPxsAH/nphXX1dsWIQWUPFE5tGcdKRffh0TZ3Vtq0rT1+CtK7gn3/5XFMMbzv+8Lr2VNtP5s9KI2OquOyWPyaeP2dqkFLWHfuKFYNY1JfBxpFy3fYfP/Mo9OYM/NtvXmjqT6vPORqqojSVYXBODrbrY7zs1rf7c4dw19NbcMKi3rp6u3rlECqOVxfPZ84dwq2PbcJFbzwCIwUb//Kr+ljnz0rh5gdfwqMbx5HSFXzqLUtRdnzc8vDGpjivPf+1KNteXfusreu49n/l6Uvw2MYdWHH0PHz9vnXxY0lNDAt607jqjCV4ZcxqantfvfdF2K5sapsLetO49JTFdfW3+twhfPN3u/rNlacvwS0Pb8RVZyxBxfGb6jqfCh6C7Sw41T4Qd83nz0rhi3e/UD3uFSsGkdFV3PjABrznxAX4j/9+CYYm8L9PWVytpwW9aXz09CVN43Lj+BTFnTUVWHZzjFlDxWG9aWwdt+vaw5qVy/DC1lEcc9hsDE9UYsefD795MW57bFPTfaRxTI368K2PvYy3HDMP9zy7takPrz53CN3p4OFWyfbxsZ+sbTrfu09YgFse3oh3vuHwavv41FuWwtTVuvbzybOXYnZOR7HiN/XFqI9+83fN7aa6Powt6f78xF924pzXzsfmhvb08TOPwncfeqk6Ll966iB+/MhGXHD8YZBC1MV47duWwXJk3fW4euUQfvXUFjy4YaR6ntNfcwg+XXNvWX3OEO59fgtOXTqvqf9GbTO6J3313hfryrigN40Pn7w4sWxrVi3Djx/ZWO0zHz55Mb55f3z/iuo/6ec1q5bha/e+WNema7db1J+F6wEf+0l788xo7hM3r5pq/pg0bzI0gctu+WPi/CfqH9/43XqMlmx89d2vg+3KuuMkzU8a5zxJ873GOFK6gq+++3WoOLKubhrHnrj9kpbtydx4On436bTffabbgVL+A6UctYQQj0kplzct31sPeMKTLgRwZ8IDnm8BuE9K+YPw8/MATpFSbml1zE5+wPPwhp246MaHYTl+dVlKV3DzxSfghCN6W+67fnsBb/3KfzXt+4vL/waL+nN7Leb9NY52JcX7wTctwg2/X99W3Ou3F/DzJzbj+vvXNx3nR5echHdc/9Ae18fu1mer7QHUrbv01MW44ffJMUd1EFc3X7t3XVvbfuH8Y/HxW4PJa9L5on0vOXkRzjtufrVcSWX53gdPxHtv+MOUx/zaveuqn689/1j8fRhHq7Jfe/6xWLdtMvZa1sa5YukA7nluGwAkXvd7ntuG6+9fn1g3l5y8CADwlXvWNcVQGysAXL5icWJM0bW45ORF+Mo963DpqYtx9Nw8XmgoR7t11fg5Om6rY1xy8iIsHsjvVtwAmo7Vavsbfr+rLmvbVe12N77/Dbj4O4+0VcYbfr8e37rweDy2cTT2nN+68Hh86LuPxZa18Zp94fxj8ezWyWp5Lj11MVQlvm1ccvIieD5argeA5Qt6MFZ2m+q0sY20astTbXPJyYtw0qLelnWWVOa4dtrYT5Yv6MFFNz7S8vxAcx9Iur5R3bXbbq6/8HhMlN3YY+3O9W01LkRt//If/LEulrh+P1U/TlofxdpqLIliaNX2on7XuH53xoZW7XbJQH7K8T66ho1jTHRd48aGqfpT4/W6/sLjcUnCtV2+oCd23Xc+cAIe+POOluNPu/eR2vEwqZ984fxj0ZXWYmNpHO+mah9J5Y3OndRu2hkjWo2RjXFee/6xUICm/nbzxW+Ije9bFx6P9934SMv+mLQ8qpMo7sYy1pan1RgZ9Zm4YzSeq52f4/ZJGs+S5pnR3Ccpnlbzx6R5U7v38ahvJrW1pPZcO+eZqv/X9tepxsSk/ZKW7cnceDp+N+m0332m24FS/gOlHLWSHvDM5Dt45gP4S83nl8NlTYQQlwghHhVCPLp9+/Z9EtzeMDxRqWtUAGA5PoYnKm3sa8Xuu23SmtYYOyWOdiXFK0T7cQ9PWPAlYo+zZfzV1cfu1mer7RvXRWVMijlpvRDtb1u03eryVsezHL/6Vd6pyrK1ZvlUMUafyxW3rbKXbTfxWtbGuWU8uOatrnu0Lulc0f5NMTTECiSfp/ZaRMcSAihWmsvRbl01fq6NsVVZyvbuxR13rKnqPvq3GFNHluNjx2T8GBpXRssJvmKfdM6xopNY1sZlRdutK48QyWXx5dTrfQmMlpzYttDYRlq15am28SWmrLOkMifFVttPRkvOlOePrc+EY0d11267GS06iccaK7V/fVuNC1Hbb4xld9t3q/VRW5yq/wGt21bU717N2NCqHtoZ76NrGLcsaWyY6ryNy0Zb9N2RhHXbJ5Pv41E87d5HfInqtkn9pGi7ibE0jndTtY+k8kbnfjVjRKsxsjHOsu3G9rekco6F40OrMiT106hOGmOINI7HSeVvdYzGc7Xzc9y6pDEoaZ4ZzX2S4mk1f0yaN7V7H5+qrSW159o5z1TnqDXVmJi0X9KyPZkbT4dO+91nuh0o5T9QytGOjnjJspTyeinlcinl8v7+/pkOZ4/N6TKR0uurPKUrmNNltrFvKnbfgXx77++ZLvtLHO1KilfK9uOe05WCKhB7nHnd6VdVH7tbn622T1rXHPOu7ZLqJq58cdtmw3dXtDpfVNeKQF25kuKd27C8VYzR54yptVX2jKElXsvaOOd1B9c8+brXt4m4bRQBNH7jMynWVjHVHi+STSWXI+kYSZ/jYowrS8bYs7jb3b7232wq/nr25+PH0LgypnQFPVk98ZyzsnpiWRuXZQ2tqTxJx432b7VeEUBPRk9st43Lk9ryVNsoAlPWWVKZk2Kr7Sc9GX3K88fWZ8L1jbZtt930ZPXEY83KtH990y3GBUUAaWPX6wpb9fup+kM7bXF3Y9id8yRtX/u5VT20M94rArFjTG0fj9t3qv5Uu6ynRd+dnbCuP598H49ia/c+oghUt03aJ2toibE0jndTXbek8taee0/HiNktxsjGODOGFtvfkso5KxwfovPsTj9tbENJ8bcqW22faXWM2jY51c9x65LGoKR5Zu3cJ26/VvPHpHlTu/fxqdpaUntunPO0OketqcaqVvHHLduTufF06LTffabbgVL+A6Uc7ZjJBzybARxW8/nQcNkBa8ncLNasXFY3sK9ZuQxL5man3HdhbxbXXXBc3b7XXXBc9UVk+8r+Eke74uK9/LRB3Pnk5rbjXtibxTGHduOKFYNN5R6a1/Wq6mN367PV9o3r7li7GZ89b1lMzN247oLjcMfazbj8tPoyXbFiED99/OWm8sVte9UZS6AoqNbLbY+93FRHUV1fsWIQrz20u65cSWV57SHd1bjjjvnZ85bhzic3132+6YH1dfHFlf3y0wZx0wPrsbAvO2WcQ/O6ccyh3ejNGgnXvbvaJpLqcfFADgM1v1xHy799/5+bjrmwL4trVi1LvBafOOsoLB7IVeukVHGaynHH2s1Yfe5Q3TFWnzNUV1eNn686Ywl6M0bdMeLiOLI/21THKT144PKZhnNevTI4R9y1m50xgndYxNR97TUoWU7TdledsQQ/eWQTrl5Zf741K+vLFB1nzcpl+P5DG9CXM5viuGZVsO7jZx5Vt/wTZx2FI/uzTccv2Q7uWLsZV56+pHoN4trGNauWoS9r4I61mzE707z+qjOWoC9r4Mj+LMZKFdz0wHqsPmeoqT5uemB9tZxx9bj6nKG663HbYy831dcVKwbRlzXwk0c2YU1DndW2rStPD2KKi6GxPdVeo8X9Odie3/L8/Tmz6dhXrBiErqBp+4+feRSO6MvG9qe5XWZsGWzPhyLQ3O7PHcJ3fr+hqd6uXjnUFM9nzh3CzQ+sx5EDOXzy7KXN/bg/i5sfWF9d1ps1cOXpS2LjPHIg19Q+a+s6rv1fefoSfP+hDbh65VDyWFITwx1rN2NRf/MYds2qZdV+19g271i7uan+Vp9b32+uPH0J7nwyOHZcXQ/kTViuW9cH4q754v5s3XGvWDGI3oyBO5/cjKvOWIKfPv4y7li7ua6e7li7OXZcbhyforjHynZsjH3Z4AXqje1hzcpl+M0zQdmSxp/V5w7F3kcajxX14Wgcj+vDq88dgqIAnu/ji28/NvZ8UX3Xto/erNHUfj559lKMle3Yvhj10bh2U11/TvI4cvlpg/jeQxtwZEx7+viZR9WNy2tWBffZkuU0xThWqjRdj6tXBn2w9jxrGu4tq88Zwvcf2hDbf6M2FN2TGst4x9rNLcu2ZtWyuj6z+pzk/hXVf9LPa1Yta2rTtdvpqsAX397+PDOa+8TFM9X8MXHedGh3Xd00zn+i/hHFfcyh3U3HSZqfNM55kuq8MY7oPI110zj2xO2XtGxP5sbTodN+95luB0r5D5RytGMm38HztwAuw66XLH9FSnnCVMfs5HfwANOTRWvbZPDG+5nOojXTcbSrPouWCsfzMftVZNEq2S4Oj8mitaf1sbv7t9q+cV2USapx22i7kWIFekMWra0Tzdtu2FHElvESjBZZtGzXx8LePcui1RhflEVr67iF+WEWrR3FSmyZos+1ZWnOohVknDI1BdLHrixano+ejIFCxYE+RRYt2/WbrntzFi0HKV0JslFlNOyctFG0PRQrHgbyBoQQ2DphoTfKojVhoS9rImMmZ9HKmkGGF8txoCoaRop2+ALPMIuW46NsB1m0MroKx5fYUbDQmzWhqQIKBEZLNjKGVs32Uqy4MGqyaKUNDTvCLFpdaQ2W7WN7oYKsqcHUBLrT9Vm0guxNbWTR6krBcn0UoixatoeUrkBTFIyWHORSWlh3QRYtI8yiVbAcdKcNlJ2g7uZ2m8ibOoYnLRwyKz6L1s5CBb1ZE+OWg9kZAwNd8Vm0+nIGJHzImixaI0UHaUOFrgqkdQW2KzE8WcFAvj6Lli99ZA0NO4o2Zmd1mGqQRSvIyGLA1BWUwyxaru8H2VQcHyXbQ84MMsVEWbQyelB/RduBqdZk0QozM7l+kCkrMYuWoqJgN2fR2jZRQdpQkTc1eGG2nzldepBFa7KCgVyYRasQZdHykNLVuixa0bXorsmiNSujo1BxoSqimiVrvDaLVldwH6vNolUMM0VZrofxkou0EWTgirJoFcMsWj1RFq2ciYrnY7zsoKuaRSvIPmZoCiqOjwnLRdpQYWgCWT3IVqOEWbRGijYG8iZMTcGm0XLw7ViJarYgIXZl0Yqyd1nhtUgZu7JoFSwPKUOZMotWoeIga+gYKVbQ25hFq2hjblcKemMWrYwBy/NQsDzMSusoOWEWLUgASnMWLUODhAc/zKIVlG9XFq1yxUNPVg+yaFn1WbQcV6JQCdqmJz0oIsj0lzM15E0NkxUXJdsLsphZNtKaGl4fH74PjJSCbXVNwFRVuL6PSStoc6OlIMNZbRatjK5CUYIsWqNFB2lTRUpXUKwEZdQVBcOTFubkU9DVIItWqeIhY6owa7JoRZm/NCUau4IsWj0ZAxlDxXjJRleYRSsqj6oAaU2Foddk0QrbgyKC/i7hQ1dUlJ0wi1YqaD+aqiBvaCi7Hkq2i5wZZNGanTUhwixaJTvIQpUzVPgIs2hlgzFqd7JoWbaLrKljrLwri9a2CQuZ8JqoYeYwy/bR32XA9SUKloPZYRat0ZKNvpyJsu0G43VKw+ZxC044jhcqQd8phVm0fN9HSg/6eV0WrbSOcas+i1b0J3hzu4J+GIwJQT0cPacLL4+XMVIM7kkFK6jfnKkh0zKL1q45V10WrZwJ1/egCAUZPT6LVjTXirJobRkvwajJoiVlUO+1WbS2jFuY252qxhvd/6WUQXnCsa1kB+OO60lMWA4OrWbRstCbNeBKH2NFF/O6TSwNj7Vt0kJ/ro0sWmHmsHltZNFqnLfsThat2nkTgKa538aREjaNFJGpyaJVO7+r3ac/t2v+N7cryKK1vdA8F6ydBy8Ms2jVbtcYR20WrSiWKItWO/tN19x4OnTa7z7T7UAp/4FSjsg+f8myEOIHAE4B0AdgGMBqADoASCm/GaZJ/yqAsxGkSf+AlHLKJzed/oCHiIiIiIiIiGhPJT3g0eI2ng5SyndNsV4CuHRvnZ+IiIiIiIiI6GAxk+/gISIiIiIiIiKiacAHPEREREREREREHW6vvmR5bxBCbAewcabjmAZ9AHbMdBBE+xn2C6Jm7BdEzdgviJqxXxA1O1D7xQIpZX/jwo57wHOgEEI8GvdSJKKDGfsFUTP2C6Jm7BdEzdgviJodbP2Cf6JFRERERERERNTh+ICHiIiIiIiIiKjD8QHPzLl+pgMg2g+xXxA1Y78gasZ+QdSM/YKo2UHVL/gOHiIiIiIiIiKiDsdv8BARERERERERdTg+4CEiIiIiIiIi6nB8wLOPCSHOFkI8L4RYJ4T45EzHQ7Q3CCFeEkI8JYR4QgjxaLhsthDibiHEi+G/PeFyIYT4StgnnhRCvL7mOO8Lt39RCPG+muXHh8dfF+4r9n0piVoTQtwohNgmhHi6Ztle7wdJ5yDaHyT0i88IITaH94wnhBBvrVn3j2Ebf14IcVbN8tj5lBDiCCHEH8LlPxJCGOFyM/y8Lly/cN+UmGhqQojDhBD3CiH+JIR4RghxRbic9ww6aLXoF7xntMAHPPuQEEIF8DUAbwHwGgDvEkK8ZmajItprTpVSHielXB5+/iSAe6SUgwDuCT8DQX8YDP+7BMA3gGDCAWA1gBMBnABgdc2k4xsA/q5mv7P3fnGIdtt30Nw290U/SDoH0f7gO4gfs78U3jOOk1L+AgDCOdI7AQyF+3xdCKFOMZ/61/BYiwGMAvhguPyDAEbD5V8KtyPaX7gAPialfA2AkwBcGrZp3jPoYJbULwDeMxLxAc++dQKAdVLK9VJKG8APAaya4ZiI9pVVAG4Kf74JwHk1y2+WgYcAzBJCzANwFoC7pZQjUspRAHcDODtc1yWlfEgGb4m/ueZYRPsNKeX9AEYaFu+LfpB0DqIZl9AvkqwC8EMpZUVKuQHAOgRzqdj5VPiNhNMA3Bru39jHon5xK4AV0TcYiGaalHKLlPLx8OdJAM8CmA/eM+gg1qJfJOE9A3zAs6/NB/CXms8vo3UjJepUEsBdQojHhBCXhMvmSCm3hD9vBTAn/DmpX7Ra/nLMcqJOsC/6QdI5iPZnl4V/anJjzTcOdrdf9AIYk1K6DcvrjhWuHw+3J9qvhH8K8joAfwDvGUQAmvoFwHtGIj7gIaK94U1Sytcj+CrkpUKIk2tXhv/3SM5IZET7iX3RD9jXqEN8A8CRAI4DsAXAF2c2HKKZIYTIAbgNwEellBO163jPoINVTL/gPaMFPuDZtzYDOKzm86HhMqIDipRyc/jvNgA/Q/DVyOHwK8II/90Wbp7UL1otPzRmOVEn2Bf9IOkcRPslKeWwlNKTUvoAvo3gngHsfr/YieBPVbSG5XXHCtd3h9sT7ReEEDqCX2K/L6X8abiY9ww6qMX1C94zWuMDnn3rEQCD4du6DQQvgbp9hmMimlZCiKwQIh/9DOBMAE8jaOtRNof3AfjP8OfbAVwUZoQ4CcB4+FXhXwM4UwjRE3718kwAvw7XTQghTgr/FvaimmMR7e/2RT9IOgfRfin65TL0PxDcM4CgLb8zzGZyBIIXwz6MhPlU+O2DewGcH+7f2MeifnE+gN+G2xPNuHAcvwHAs1LK62pW8Z5BB62kfsF7RmuiQ+I8YIggjdu/AVAB3Cil/NwMh0Q0rYQQixB8awcANAC3SCk/J4ToBfBjAIcD2AjgAinlSDh4fxXB2+5LAD4gpYxSq18M4FPhsT4npfyPcPlyBJlY0gB+CeAjnTLo0sFDCPEDAKcA6AMwjCCzyc+xl/tBUl/b6wUmakNCvzgFwVftJYCXAHwoeieIEOL/ALgYQTaVj0opfxkuj51PhfegHwKYDeCPAN4rpawIIVIAvovgHQ4jAN4ppVy/90tMNDUhxJsA/BeApwD44eJPIXjfCO8ZdFBq0S/eBd4zEvEBDxERERERERFRh+OfaBERERERERERdTg+4CEiIiIiIiIi6nB8wENERERERERE1OH4gIeIiIiIiIiIqMPxAQ8RERERERERUYfjAx4iIiI64AkhPCHEE0KItUKIx4UQb2xjn8K+iI2IiIhoOmgzHQARERHRPlCWUh4HAEKIswB8HsCbZzYkIiIiounDb/AQERHRwaYLwCgACCFyQoh7wm/1PCWEWNW4cdI2QoiFQohnhRDfFkI8I4S4SwiRDtctFkL8puYbQ0eGyz8hhHhECPGkEOLqfVhmIiIiOsAJKeVMx0BERES0VwkhPABPAUgBmAfgNCnlY0IIDUBGSjkhhOgD8BCAQSmlFEIUpJS5pG0ALACwDsByKeUTQogfA7hdSvk9IcQfAPyLlPJnQogUgv+p9iYA5wP4EAAB4HYA10op79+XdUFEREQHJv6JFhERER0Mav9E668A3CyEWIbgQcs/CyFOBuADmA9gDoCtNfsmbQMAG6SUT4Q/PwZgoRAiD2C+lPJnACCltMLzngngTAB/DLfPIXhQxAc8RERE9KrxAQ8REREdVKSUD4bfxOkH8Nbw3+OllI4Q4iUE3/Kp9Z4W21RqtvMApFucWgD4vJTyW6++FERERET1+A4eIiIiOqgIIZYCUAHsBNANYFv44OZUBH921aidbaqklJMAXhZCnBeezxRCZAD8GsDFQohcuHy+EGJg2gpGREREBzV+g4eIiIgOBmkhRPSnVALA+6SUnhDi+wDuEEI8BeBRAM/F7NvONo0uBPAtIcQaAA6At0sp7xJCHA3gQSEEABQAvBfAtldTMCIiIiKAL1kmIiIiIiIiIup4/BMtIiIiIiIiIqIOxwc8REREREREREQdjg94iIiIiIiIiIg6HB/wEBERERERERF1OD7gISIiIiIiIiLqcHzAQ0RERERERETU4fiAh4iIiIiIiIiow/1/IB+Dzb9+iFAAAAAASUVORK5CYII=\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "box_scatter(df,'Balance','Exited');\n",
        "plt.tight_layout()\n",
        "print(f\"# of Bivariate Outliers: {len(df.loc[df['Balance'] > 220000])}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "106205ab",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 441
        },
        "id": "106205ab",
        "outputId": "fe0d2209-7156-492d-d7f1-49032f6ae4c2"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1152x432 with 2 Axes>"
            ],
            "image/png": "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ZF4aBv5rKRMmIiIiIiIiIiKLs9BXtD4OfAl4N/CWzPZp59zeJUuViIiIiIiIiIgs2kILPM4592Mze23nC2a2Wos8IiIiIiIiIiLLbzGf4LkQuBVwgGVec8DJS5QuERERERERERFZpIELPM65C5N/Tzo0yRERERERERERkYO1qChaZvaqjr89M7tiaZIkIiIiIiIiIiIHY7Fh0s8xsy+a2TozOx24mTiSloiIiIiIiIiILLOFfoMHAOfcb5jZi4A7gVngN5xzCpMuIiIiIiIiIvIYsNivaG0ALgM+B9wPvNTMykuZMBERERERERERWZzFfkXrC8CfOOf+J/BM4EfALUuWKhERERERERERWbRFfUULONM5NwXgnHPAX5jZF5YuWSIiIiIiIiIislgDP8FjZm8GcM5Nmdmvdbz88oVObmbnm9ndZrbNzN7SZ59fN7MfmNn3zezjkUwplwAAIABJREFUi024iIiIiIiIiIjEFvqK1oszz/+w47XzBx1oZh5wNXABcBrwEjM7rWOfDcl5f9k5twn4vcUkWkREREREREREDlhogcf6PO/1d6czgW3Oue3OuQbwSeDijn1+B7jaObcPwDm3c4FzioiIiIiIiIhIh4UWeFyf573+7nQM8JPM3w8m27I2AhvN7L/M7GYz6/mpIDO71My2mtnWXbt2LXBZEREREREREZEjy0I/snyGmU0Rf1qnlDwn+bv4c7r+BuBs4FjgRjN7onNuMruTc+4DwAcANm/evNDCkoiIiIiIiIjIEWXgAo9zzvsZzr0DOC7z97HJtqwHgW8550LgPjO7h3jBRyHYRUREREREREQWaaGvaP0sbgE2mNlJZpYn/sHm6zr2+VfiT+9gZmuIv7K1fQnTJCIiIiIiIiJy2FmyBR7nXAS8DvgycBfwaefc983sKjPbkuz2ZWCPmf0A+CrwJufcnqVKk4iIiIiIiIjI4cicW1k/abN582a3devW5U6GiIiIiIiIiMghZ2a3Ouc2d25fyq9oiYiIiIiIiIjIIaAFHhERERERERGRFU4LPCIiIiIiIiIiK5wWeEREREREREREVjgt8IiIiIiIiIiIrHBa4BERERERERERWeG0wCMiIiIiIiIissJpgUdEREREREREZIXTAo+IiIiIiIiIyAqnBR4RERERERERkRVOCzwiIiIiIiIiIiucFnhERERERERERFY4LfCIiIiIiIiIiKxwWuAREREREREREVnhtMAjIiIiIiIiIrLCaYFHRERERERERGSF0wKPiIiIiIiIiMgKpwUeEREREREREZEVTgs8IiIiIiIiIiIrnBZ4RERERERERERWOC3wiIiIiIiIiIiscEu6wGNm55vZ3Wa2zcze0uP1483sq2b2HTO7w8yet5TpERERERERERE5HC3ZAo+ZecDVwAXAacBLzOy0jt3eCnzaOfdk4MXA+5cqPSIiIiIiIiIih6ul/ATPmcA259x251wD+CRwccc+DhhJno8CP13C9IiIiIiIiIiIHJaWcoHnGOAnmb8fTLZlvR34LTN7EPgi8L96ncjMLjWzrWa2ddeuXUuRVhERERERERGRFWu5f2T5JcBHnHPHAs8D/tHMutLknPuAc26zc27zxMTEIU+kiIiIiIiIiMhj2VIu8OwAjsv8fWyyLetVwKcBnHPfBIrAmiVMk4iIiIiIiIjIYWcpF3huATaY2Ulmlif+EeXrOvZ5ADgHwMyeQLzAo+9giYiIiIiIiIgchCVb4HHORcDrgC8DdxFHy/q+mV1lZluS3X4f+B0zux34BPBy55xbqjSJiIiIiIiIiByO/KU8uXPui8Q/npzd9rbM8x8Av7yUaRAREREREREROdwt948si4iIiIiIiIjIz0gLPCIiIiIiIiIiK5wWeEREREREREREVjgt8IiIiIiIiIiIrHBa4BERERERERERWeG0wCMiIiIiIiIissJpgUdEREREREREZIXTAo+IiIiIiIiIyAqnBR4RERERERERkRVOCzwiIiIiIiIiIiucFnhERERERERERFY4LfCIiIiIiIiIiKxwWuAREREREREREVnhtMAjIiIiIiIiIrLCaYFHRERERERERGSF0wKPiIiIiIiIiMgKpwUeEREREREREZEVTgs8IiIiIiIiIiIrnBZ4RERERERERERWOC3wiIiIiIiIiIiscFrgERERERERERFZ4bTAIyIiIiIiIiKywvlLdWIz+zBwIbDTOXd6j9cN+GvgeUAVeLlz7ralSs9jRaPR5I6f7ueRqRrHrSpRDZvsnmmwdrhAvRlhLsdw0We2HhJ4HntmGxwzWqQWtXhkqs6a4TyjRZ/9tYjJashoySfveTwyXWPtcIFKwWOu0WLndJ3Rko+fy7F7tsHaoQItHDun6kwMF8hZi5bL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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        " box_scatter(df,'EstimatedSalary','Exited');\n",
        "plt.tight_layout()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "94d89133",
      "metadata": {
        "id": "94d89133"
      },
      "source": [
        "# REMOVING OUTLIERS"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "edd3f3e2",
      "metadata": {
        "id": "edd3f3e2"
      },
      "outputs": [],
      "source": [
        "for i in df:\n",
        "    if df[i].dtype=='int64' or df[i].dtypes=='float64':\n",
        "        q1=df[i].quantile(0.25)\n",
        "        q3=df[i].quantile(0.75)\n",
        "        iqr=q3-q1\n",
        "        upper=q3+1.5*iqr\n",
        "        lower=q1-1.5*iqr\n",
        "        df[i]=np.where(df[i] >upper, upper, df[i])\n",
        "        df[i]=np.where(df[i] <lower, lower, df[i])\n",
        "        "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "147ce48e",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 458
        },
        "id": "147ce48e",
        "outputId": "d1d85479-1510-4557-ca80-185e5651ced2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "# of Bivariate Outliers: 19\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1152x432 with 2 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAABHgAAAGoCAYAAAA99FLLAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzde7xlZ10f/s9z7nPmmsxMLgZCwEwQEpXLgPrSIjctKib2J+XSVkVpqVUu1VrF1koTaltta0WKVeoNbwje2mixiFyKVblMQIGAwBhISEgyk2QytzPn/vz+OHuds88+e59zMuRksjLv9+uV15x12Wt913Nba3+z935KrTUAAAAAtNfQuQ4AAAAAgC+OBA8AAABAy0nwAAAAALScBA8AAABAy0nwAAAAALTcyLkO4IHat29fveKKK851GAAAAAAPuZtuuumeWuv+3vWtS/BcccUVOXTo0LkOAwAAAOAhV0q5td96X9ECAAAAaDkJHgAAAICWk+ABAAAAaDkJHgAAAICWk+ABAAAAaDkJHgAAAICWk+ABAAAAaDkJHgAAAICWk+ABAAAAaDkJHgAAAICWk+ABAAAAaDkJHgAAAICWk+ABAAAAaDkJHgAAAICWGznXAQAAD09veMMbcvjw4XMdBi11xx13JEkuu+yycxwJbXLllVfmla985bkOA6CVJHgAgL4OHz6cv/r4J7MweeG5DoUWGp46niS5a8bjJpszPHXfuQ4BoNXccQGAgRYmL8yZL/vmcx0GLbTtb96eJNoPm9a0GQDOjt/gAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CZ5z4A1veEPe8IY3nOswAAAA4LxwPrwPHznXAZyPDh8+fK5DAAAAgPPG+fA+3Cd4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5UbOdQDnozvuuCNnzpzJq1/96nMdCgAMdPjw4QzN1nMdBnCeGJo+kcOHT3pGBrbE4cOHs23btnMdxpZqxSd4SikvL6UcKqUcOnr06LkOBwAAAOBhpRWf4Km1vinJm5Lk4MGDrf9fiZdddlmS5PWvf/05jgQABnv1q1+dm265+1yHAZwnFid25crHXewZGdgS58OnA1vxCR4AAAAABpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGg5CR4AAACAlpPgAQAAAGi5kXMdwPnoyiuvPNchAAAAwHnjfHgfLsFzDrzyla881yEAAADAeeN8eB/uK1oAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByI+c6AADg4Wt46r5s+5u3n+swaKHhqXuT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6rzxvUvHXlq+JuMjyY/8/sfXHP9FBy/PX33+3jznCZfm5957OC86ePny+u5j/ti3PCG7JkbyX9756TXbXvv8q/OeT92Z5z7h0lXXcMO3PjELKbn+D5fW9bvOG669OvPzsxkeGcvvHLot3/6Uy1eV048+78sys7CY3/zArWvO+6pnH1iO/bU9x/zTT96ZJz16b3723Z/JBZNj+c6veUxe/67BZdSUx/c988r8zqHb8uwvu2RVOTTH+O0P3TawjF717AN599/clb9/8PJV8TTH/t5nXLlcb/t3jebPP30kV12yZ7k8Dj5md1548PJV5XP9tVfndw7dlkO3Hs/E6FBed901GR8pfeuh+zz96uM//n9fnvnFmh/7nx9fro+N2uX3PfPKvtfyymcfyNhwyQ//3scG1m1TP899wqV5W1fd9quP5jp72/L1116dHWM1p2fLqmO/9luvzls+cGuOT8/le59xZX7+fYfXlMegOr7h2ifm7hNz+fEbP75q3xNTZ7Jzctvy9X7jE/etKcOm733DEy/NttGh/Ps//ptV1//G966No7tt/VxXPD/17V+e2YWV+ugt/97Xfuau+3Pgkj2r6qMZY45NzQ683u99xpU5cvxULr1gR98x5h9+1WMyPjyU//B//mbNtuaamvbQ216a/V78tMuX49ioH7zo4OW579TUqrY/MTqUf/dt12R0uORHfm/tWPf3D16ed33yzjzr8Zf2ba+7J0bzkq96zPJY028cGNQufuoFX5GZucX8m/+1dnz8vmdemXd1jtGvzzfHmp2vG44xN1x7dT591/25cMdk3/bximcdyLaxofzqn3921Th48DG715RldzvpN240/WNspKza1ttPB43JuydH8j/ed8ua8bi7T6/X1v/FNxzI9FzW9LHuttTvvJ++6/78748fzXd+zWPyrk/etWE5bHTMphw+feTUcrt84cHLl8ejZtzoV7fdfWvlnrv02mY87u4nhz53T556xb6e+K7J/p0jeeN7/jbf/pTL83sfXn3e5nzr9a1XPOtAxkeH8sO/+9E1bftPPnHPqvvoyMjYquv/yW//8szO175t+0UHL18uj9566G63r3/xk3J8aq7vOPjCg5evGR/6jcXdZdnUQ79yGPT8smO85Cffsf49r/u+1RtHv3tOd929rXPvaeJq6qm7Pm647prsnhjJq9/6V6tifVuf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PLXW+SSvSPKOJJ9M8rZa682llBtKKdd2dntHkntLKZ9I8p4k/7LWeu9WxQQAAADwSFRqbddP2hw8eLAeOnToXIcBAAAA8JArpdxUaz3Yu34rv6IFAAAAwENAggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpOggcAAACg5SR4AAAAAFpuSxM8pZTnlVI+VUo5XEp5TZ/tl5dS3lNK+Ugp5aOllG/eyngAAAAAHom2LMFTShlO8sYk35TkiUleUkp5Ys9uP5bkbbXWJyd5cZKf26p4AAAAAB6ptvITPE9PcrjWekutdTbJbye5rmefmmRX5+/dSb6whfEAAAAAPCJtZYLnsiSf71q+vbOu279N8o9KKbcneXuSV/Y7UCnl5aWUQ6WUQ0ePHt2KWAEAAABa61z/yPJLkvxqrfVRSb45ya+XUtbEVGt9U631YK314P79+x/yIAEAAAAezrYywXNHkkd3LT+qs67by5K8LUlqrX+ZZCLJvi2MCQAAAOARZysTPB9KcqCU8thSyliWfkT5xp59bkvynCQppTwhSwke38ECAAAAeAC2LMFTa51P8ook70jyySzNlnVzKeWGUsq1nd3+RZJ/Ukr56yRvSfLSWmvdqpgAAAAAHolGtvLgtda3Z+nHk7vX/XjX359I8rVbGQMAAADAI925/pFlAAAAAL5IEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALSfBAwAAANByEjwAAAAALTeyVQcupfxykucnOVJrvabP9pLk9Um+OclUkpfWWj+8VfE8XNx/Zjqfvut07j4xk4t3jeeqS7Znz7aJLC7WfO7e07n7xHQu3jWRK/Zuz9BQOatzbOZYvftcfsFkbjs2teY13ftdunsiC4vJkZNrXzM5NpLZhYXs3T4+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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "box_scatter(df,'CreditScore','Exited');\n",
        "plt.tight_layout()\n",
        "print(f\"# of Bivariate Outliers: {len(df.loc[df['CreditScore'] < 400])}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "6f67a35c",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 458
        },
        "id": "6f67a35c",
        "outputId": "44daab5b-e497-41cf-b725-52be3f6ab36e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "# of Bivariate Outliers: 0\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1152x432 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "box_scatter(df,'Age','Exited');\n",
        "plt.tight_layout()\n",
        "print(f\"# of Bivariate Outliers: {len(df.loc[df['Age'] > 87])}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "cfc74d3c",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 458
        },
        "id": "cfc74d3c",
        "outputId": "f2ae3134-0c4c-4389-d5a8-55ecadec59a4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "# of Bivariate Outliers: 4\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1152x432 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "box_scatter(df,'Balance','Exited');\n",
        "plt.tight_layout()\n",
        "print(f\"# of Bivariate Outliers: {len(df.loc[df['Balance'] > 220000])}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Check for Categorical columns and perform encoding.**"
      ],
      "metadata": {
        "id": "ZitUS6GTT0i5"
      },
      "id": "ZitUS6GTT0i5"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "6c653398",
      "metadata": {
        "id": "6c653398"
      },
      "outputs": [],
      "source": [
        "from sklearn.preprocessing import LabelEncoder\n",
        "encoder=LabelEncoder()\n",
        "for i in df:\n",
        "    if df[i].dtype=='object' or df[i].dtype=='category':\n",
        "        df[i]=encoder.fit_transform(df[i])"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Split the data into dependent and independent variables**"
      ],
      "metadata": {
        "id": "0RxXbkRiPNxW"
      },
      "id": "0RxXbkRiPNxW"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "215bd4de",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "215bd4de",
        "outputId": "fcb40db0-0195-48d3-f6ab-f19a1bfe5eb4"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   CreditScore  Geography  Gender   Age  Tenure    Balance  NumOfProducts  \\\n",
              "0        619.0          0       0  42.0     2.0       0.00            1.0   \n",
              "1        608.0          2       0  41.0     1.0   83807.86            1.0   \n",
              "2        502.0          0       0  42.0     8.0  159660.80            3.0   \n",
              "3        699.0          0       0  39.0     1.0       0.00            2.0   \n",
              "4        850.0          2       0  43.0     2.0  125510.82            1.0   \n",
              "\n",
              "   HasCrCard  IsActiveMember  EstimatedSalary  \n",
              "0          1               1        101348.88  \n",
              "1          0               1        112542.58  \n",
              "2          1               0        113931.57  \n",
              "3          0               0         93826.63  \n",
              "4          1               1         79084.10  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-117d1af1-8c5e-45f6-b257-d6f4c84a0540\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>619.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>42.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>101348.88</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>608.0</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>41.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>83807.86</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>112542.58</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>502.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>42.0</td>\n",
              "      <td>8.0</td>\n",
              "      <td>159660.80</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>113931.57</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>699.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>39.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>93826.63</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>850.0</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>43.0</td>\n",
              "      <td>2.0</td>\n",
              "      <td>125510.82</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>79084.10</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-117d1af1-8c5e-45f6-b257-d6f4c84a0540')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-117d1af1-8c5e-45f6-b257-d6f4c84a0540 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-117d1af1-8c5e-45f6-b257-d6f4c84a0540');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ],
      "source": [
        "x=df.iloc[:,:-1]\n",
        "x.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "96369946",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "96369946",
        "outputId": "9396a37c-6d67-4c98-de60-b4f1b9250d46"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    1\n",
              "1    0\n",
              "2    1\n",
              "3    0\n",
              "4    0\n",
              "Name: Exited, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ],
      "source": [
        "y=df.iloc[:,-1]\n",
        "y.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Scale the independent variables**"
      ],
      "metadata": {
        "id": "zQGZZVUgPthI"
      },
      "id": "zQGZZVUgPthI"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c41875dc",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c41875dc",
        "outputId": "e75235ee-d24e-45fb-f900-290c4e9e5002"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[-0.32687761, -0.90188624, -1.09598752, ...,  0.64609167,\n",
              "         0.97024255,  0.02188649],\n",
              "       [-0.44080365,  1.51506738, -1.09598752, ..., -1.54776799,\n",
              "         0.97024255,  0.21653375],\n",
              "       [-1.53863634, -0.90188624, -1.09598752, ...,  0.64609167,\n",
              "        -1.03067011,  0.2406869 ],\n",
              "       ...,\n",
              "       [ 0.60524449, -0.90188624, -1.09598752, ..., -1.54776799,\n",
              "         0.97024255, -1.00864308],\n",
              "       [ 1.25772996,  0.30659057,  0.91241915, ...,  0.64609167,\n",
              "        -1.03067011, -0.12523071],\n",
              "       [ 1.4648682 , -0.90188624, -1.09598752, ...,  0.64609167,\n",
              "        -1.03067011, -1.07636976]])"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ],
      "source": [
        "from sklearn.preprocessing import StandardScaler\n",
        "scaler=StandardScaler()\n",
        "x=scaler.fit_transform(x)\n",
        "x"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Split the data into training and testing**"
      ],
      "metadata": {
        "id": "zTz70jK6Pzqk"
      },
      "id": "zTz70jK6Pzqk"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "51f97d63",
      "metadata": {
        "id": "51f97d63"
      },
      "outputs": [],
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1fffcc64",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1fffcc64",
        "outputId": "dd2a0d2d-8b22-4f62-f8e4-20886bc4b420"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(6700, 10)"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ],
      "source": [
        "x_train.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "5b285109",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5b285109",
        "outputId": "370f3edc-a35d-4544-830b-f4c8153d895f"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(3300, 10)"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ],
      "source": [
        "x_test.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fba38e32",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fba38e32",
        "outputId": "0956402b-0b02-4bfc-fe56-02b17648afef"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(6700,)"
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ],
      "source": [
        "y_train.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "6a2e1376",
      "metadata": {
        "id": "6a2e1376"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.12"
    },
    "colab": {
      "provenance": [],
      "collapsed_sections": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}