{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "!pip install tensorflow\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4qmsMlxNLao3",
        "outputId": "02ac3e7c-6b17-4a96-b4f7-653826a62b05"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: tensorflow in /usr/local/lib/python3.10/dist-packages (2.15.0)\n",
            "Requirement already satisfied: absl-py>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (1.4.0)\n",
            "Requirement already satisfied: astunparse>=1.6.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (1.6.3)\n",
            "Requirement already satisfied: flatbuffers>=23.5.26 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (23.5.26)\n",
            "Requirement already satisfied: gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (0.5.4)\n",
            "Requirement already satisfied: google-pasta>=0.1.1 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (0.2.0)\n",
            "Requirement already satisfied: h5py>=2.9.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (3.9.0)\n",
            "Requirement already satisfied: libclang>=13.0.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (16.0.6)\n",
            "Requirement already satisfied: ml-dtypes~=0.2.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (0.2.0)\n",
            "Requirement already satisfied: numpy<2.0.0,>=1.23.5 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (1.23.5)\n",
            "Requirement already satisfied: opt-einsum>=2.3.2 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (3.3.0)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.10/dist-packages (from tensorflow) (23.2)\n",
            "Requirement already satisfied: protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (3.20.3)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.10/dist-packages (from tensorflow) (67.7.2)\n",
            "Requirement already satisfied: six>=1.12.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (1.16.0)\n",
            "Requirement already satisfied: termcolor>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (2.4.0)\n",
            "Requirement already satisfied: typing-extensions>=3.6.6 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (4.5.0)\n",
            "Requirement already satisfied: wrapt<1.15,>=1.11.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (1.14.1)\n",
            "Requirement already satisfied: tensorflow-io-gcs-filesystem>=0.23.1 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (0.35.0)\n",
            "Requirement already satisfied: grpcio<2.0,>=1.24.3 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (1.60.0)\n",
            "Requirement already satisfied: tensorboard<2.16,>=2.15 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (2.15.1)\n",
            "Requirement already satisfied: tensorflow-estimator<2.16,>=2.15.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (2.15.0)\n",
            "Requirement already satisfied: keras<2.16,>=2.15.0 in /usr/local/lib/python3.10/dist-packages (from tensorflow) (2.15.0)\n",
            "Requirement already satisfied: wheel<1.0,>=0.23.0 in /usr/local/lib/python3.10/dist-packages (from astunparse>=1.6.0->tensorflow) (0.42.0)\n",
            "Requirement already satisfied: google-auth<3,>=1.6.3 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow) (2.17.3)\n",
            "Requirement already satisfied: google-auth-oauthlib<2,>=0.5 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow) (1.2.0)\n",
            "Requirement already satisfied: markdown>=2.6.8 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow) (3.5.2)\n",
            "Requirement already satisfied: requests<3,>=2.21.0 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow) (2.31.0)\n",
            "Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow) (0.7.2)\n",
            "Requirement already satisfied: werkzeug>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from tensorboard<2.16,>=2.15->tensorflow) (3.0.1)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow) (5.3.2)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow) (0.3.0)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.10/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow) (4.9)\n",
            "Requirement already satisfied: requests-oauthlib>=0.7.0 in /usr/local/lib/python3.10/dist-packages (from google-auth-oauthlib<2,>=0.5->tensorboard<2.16,>=2.15->tensorflow) (1.3.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow) (3.6)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow) (2023.11.17)\n",
            "Requirement already satisfied: MarkupSafe>=2.1.1 in /usr/local/lib/python3.10/dist-packages (from werkzeug>=1.0.1->tensorboard<2.16,>=2.15->tensorflow) (2.1.3)\n",
            "Requirement already satisfied: pyasn1<0.6.0,>=0.4.6 in /usr/local/lib/python3.10/dist-packages (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow) (0.5.1)\n",
            "Requirement already satisfied: oauthlib>=3.0.0 in /usr/local/lib/python3.10/dist-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<2,>=0.5->tensorboard<2.16,>=2.15->tensorflow) (3.2.2)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import tensorflow as tf\n",
        "from tensorflow import keras\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np"
      ],
      "metadata": {
        "id": "YMcPUUSKLlTD"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "(X_train,y_train) , (X_test,y_test) = keras.datasets.mnist.load_data()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kdBiMk7NO04C",
        "outputId": "dc84bd1a-f8bc-417f-99ef-eed76f6eae80"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz\n",
            "11490434/11490434 [==============================] - 0s 0us/step\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "len(X_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q_NadYbWPKth",
        "outputId": "c3eb309c-afe8-4768-f83d-52bf27dafaf6"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "60000"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_train[0].shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i1exGpmmPWfh",
        "outputId": "4e9ae8c2-e153-40a8-ba3f-3aea07d3fdf9"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(28, 28)"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_train[0]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kCeXpnrNPicG",
        "outputId": "cb387d77-8c61-49f6-b714-6586097bb0bc"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   3,\n",
              "         18,  18,  18, 126, 136, 175,  26, 166, 255, 247, 127,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,  30,  36,  94, 154, 170,\n",
              "        253, 253, 253, 253, 253, 225, 172, 253, 242, 195,  64,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,  49, 238, 253, 253, 253, 253,\n",
              "        253, 253, 253, 253, 251,  93,  82,  82,  56,  39,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,  18, 219, 253, 253, 253, 253,\n",
              "        253, 198, 182, 247, 241,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,  80, 156, 107, 253, 253,\n",
              "        205,  11,   0,  43, 154,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,  14,   1, 154, 253,\n",
              "         90,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 139, 253,\n",
              "        190,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  11, 190,\n",
              "        253,  70,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  35,\n",
              "        241, 225, 160, 108,   1,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "         81, 240, 253, 253, 119,  25,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,  45, 186, 253, 253, 150,  27,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,  16,  93, 252, 253, 187,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0, 249, 253, 249,  64,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,  46, 130, 183, 253, 253, 207,   2,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  39,\n",
              "        148, 229, 253, 253, 253, 250, 182,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  24, 114, 221,\n",
              "        253, 253, 253, 253, 201,  78,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,  23,  66, 213, 253, 253,\n",
              "        253, 253, 198,  81,   2,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,  18, 171, 219, 253, 253, 253, 253,\n",
              "        195,  80,   9,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,  55, 172, 226, 253, 253, 253, 253, 244, 133,\n",
              "         11,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0, 136, 253, 253, 253, 212, 135, 132,  16,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0]], dtype=uint8)"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.matshow(X_train[5])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 454
        },
        "id": "Xy_MAcB-PqdV",
        "outputId": "1bfeffa5-7a86-4be2-f5cf-0eeb329c184b"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.image.AxesImage at 0x7875bba53bb0>"
            ]
          },
          "metadata": {},
          "execution_count": 12
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 480x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAaMAAAGkCAYAAACckEpMAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAdUklEQVR4nO3df3BV5b3v8c8mhA1osjGE/JKAAVFafqQthTRVMUoukM6xoJx78dcMeB0cafAU8NekR0Fs56SlM9Tai3LPmRZqr6C1V+DKOcXRQMKlBiwoh0NbI8G0wIGESkt2CGYTkuf+wXXTLQF8Njv5JuH9mlkje6313evrwxo/rr3WfnbAOecEAIChPtYNAABAGAEAzBFGAABzhBEAwBxhBAAwRxgBAMwRRgAAc4QRAMAcYQQAMEcYAQDM9ZgwWrlypa677jr1799fBQUFevfdd61b6nLPPPOMAoFAzDJ69GjrtrrEtm3bdMcddygnJ0eBQEAbNmyI2e6c05IlS5Sdna0BAwaouLhY+/fvt2m2E11qHObOnXveOTJ9+nSbZjtReXm5Jk6cqJSUFGVkZGjmzJmqqamJ2aelpUWlpaUaPHiwrr76as2aNUsNDQ1GHXeOzzMORUVF550TDz/8sFHHF9YjwujVV1/V4sWLtXTpUr333nvKz8/XtGnTdOzYMevWutyYMWN09OjR6LJ9+3brlrpEc3Oz8vPztXLlyg63L1++XM8//7xWrVqlnTt36qqrrtK0adPU0tLSxZ12rkuNgyRNnz495hxZt25dF3bYNaqqqlRaWqodO3borbfeUmtrq6ZOnarm5uboPosWLdIbb7yh1157TVVVVTpy5Ijuuusuw64T7/OMgyTNmzcv5pxYvny5UccX4XqASZMmudLS0ujrtrY2l5OT48rLyw276npLly51+fn51m2Yk+TWr18ffd3e3u6ysrLcD3/4w+i6EydOuGAw6NatW2fQYdf47Dg459ycOXPcjBkzTPqxdOzYMSfJVVVVOefO/v0nJye71157LbrPH/7wByfJVVdXW7XZ6T47Ds45d+utt7pvf/vbdk19Tt3+yuj06dPavXu3iouLo+v69Omj4uJiVVdXG3ZmY//+/crJydGIESN033336eDBg9Ytmaurq1N9fX3MORIKhVRQUHBFniOVlZXKyMjQjTfeqPnz5+v48ePWLXW6xsZGSVJaWpokaffu3WptbY05J0aPHq1hw4b16nPis+PwqZdfflnp6ekaO3asysrKdOrUKYv2LqqvdQOX8vHHH6utrU2ZmZkx6zMzM/XBBx8YdWWjoKBAa9as0Y033qijR49q2bJluuWWW7Rv3z6lpKRYt2emvr5ekjo8Rz7ddqWYPn267rrrLuXl5enAgQP6zne+o5KSElVXVyspKcm6vU7R3t6uhQsX6qabbtLYsWMlnT0n+vXrp0GDBsXs25vPiY7GQZLuvfdeDR8+XDk5Odq7d6+efPJJ1dTU6PXXXzfs9nzdPoxwTklJSfTP48ePV0FBgYYPH65f/vKXevDBBw07Q3dx9913R/88btw4jR8/XiNHjlRlZaWmTJli2FnnKS0t1b59+66Y+6cXcqFxeOihh6J/HjdunLKzszVlyhQdOHBAI0eO7Oo2L6jbf0yXnp6upKSk856CaWhoUFZWllFX3cOgQYN0ww03qLa21roVU5+eB5wj5xsxYoTS09N77TmyYMECbdq0SVu3btXQoUOj67OysnT69GmdOHEiZv/eek5caBw6UlBQIEnd7pzo9mHUr18/TZgwQRUVFdF17e3tqqioUGFhoWFn9k6ePKkDBw4oOzvbuhVTeXl5ysrKijlHwuGwdu7cecWfI4cPH9bx48d73TninNOCBQu0fv16bdmyRXl5eTHbJ0yYoOTk5JhzoqamRgcPHuxV58SlxqEje/bskaTud05YP0HxebzyyisuGAy6NWvWuN///vfuoYcecoMGDXL19fXWrXWpRx991FVWVrq6ujr3m9/8xhUXF7v09HR37Ngx69Y6XVNTk3v//ffd+++/7yS5FStWuPfff9/96U9/cs459/3vf98NGjTIbdy40e3du9fNmDHD5eXluU8++cS488S62Dg0NTW5xx57zFVXV7u6ujr39ttvu6985Stu1KhRrqWlxbr1hJo/f74LhUKusrLSHT16NLqcOnUqus/DDz/shg0b5rZs2eJ27drlCgsLXWFhoWHXiXepcaitrXXPPvus27Vrl6urq3MbN250I0aMcJMnTzbu/Hw9Ioycc+4nP/mJGzZsmOvXr5+bNGmS27Fjh3VLXW727NkuOzvb9evXz1177bVu9uzZrra21rqtLrF161Yn6bxlzpw5zrmzj3c//fTTLjMz0wWDQTdlyhRXU1Nj23QnuNg4nDp1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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_train.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j518Lxp3QOrW",
        "outputId": "9b45972a-6600-4903-cad7-14c5e4e049bd"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(60000, 28, 28)"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_train_flattend = X_train.reshape(len(X_train),28*28)\n",
        "X_test_flattened = X_test.reshape(len(X_test),28*28)"
      ],
      "metadata": {
        "id": "lhPPJvedQYOu"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(X_train_flattend)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SMJSJlt5Q4OT",
        "outputId": "b2d38bc6-20e5-4ade-fb0e-54c4fbafc35b"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[0 0 0 ... 0 0 0]\n",
            " [0 0 0 ... 0 0 0]\n",
            " [0 0 0 ... 0 0 0]\n",
            " ...\n",
            " [0 0 0 ... 0 0 0]\n",
            " [0 0 0 ... 0 0 0]\n",
            " [0 0 0 ... 0 0 0]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_test_flattened.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UAlHojvxQ-6Z",
        "outputId": "3733d4a1-f75f-4bd2-8bec-b28852cda39e"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(10000, 784)"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model = keras.Sequential([\n",
        "    keras.layers.Dense(10,input_shape=(784,),activation='sigmoid')\n",
        "])\n",
        "\n",
        "model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])\n",
        "model.fit(X_train_flattend,y_train,epochs=5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fxQCOeedRH4c",
        "outputId": "624be9dd-9874-481e-93ce-0e7cc8c1e0c9"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/5\n",
            "1875/1875 [==============================] - 5s 2ms/step - loss: 9.7672 - accuracy: 0.8403\n",
            "Epoch 2/5\n",
            "1875/1875 [==============================] - 4s 2ms/step - loss: 6.0264 - accuracy: 0.8783\n",
            "Epoch 3/5\n",
            "1875/1875 [==============================] - 5s 3ms/step - loss: 5.6156 - accuracy: 0.8830\n",
            "Epoch 4/5\n",
            "1875/1875 [==============================] - 4s 2ms/step - loss: 5.5836 - accuracy: 0.8850\n",
            "Epoch 5/5\n",
            "1875/1875 [==============================] - 4s 2ms/step - loss: 5.2984 - accuracy: 0.8865\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<keras.src.callbacks.History at 0x7875b920a200>"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_predicted = model.predict(X_test_flattened)\n",
        "y_predicted[0]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0q4qOKvrT9Jb",
        "outputId": "0a29c4e2-e623-4d9c-9a72-af2f5b092e38"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "313/313 [==============================] - 1s 3ms/step\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([2.4674849e-01, 0.0000000e+00, 4.1772881e-01, 1.0000000e+00,\n",
              "       7.0051542e-14, 1.0000000e+00, 0.0000000e+00, 1.0000000e+00,\n",
              "       1.0000000e+00, 1.0000000e+00], dtype=float32)"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "np.argmax(y_predicted[1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4vsYmmn5UMwm",
        "outputId": "9510d196-c345-4eac-abec-4fd7e3b62a07"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cm = tf.math.confusion_matrix(labels=y_test,predictions=y_predicted)\n",
        "cm"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 355
        },
        "id": "Vck8IEzaUbDi",
        "outputId": "6a167b50-1ff5-4c4c-c06e-d3afa375fe23"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "error",
          "ename": "InvalidArgumentError",
          "evalue": "{{function_node __wrapped__Pack_N_2_device_/job:localhost/replica:0/task:0/device:CPU:0}} Shapes of all inputs must match: values[0].shape = [10000] != values[1].shape = [10000,10] [Op:Pack] name: stack",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mInvalidArgumentError\u001b[0m                      Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-26-9582371e1b01>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mcm\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconfusion_matrix\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0my_test\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mpredictions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0my_predicted\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mcm\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/tensorflow/python/util/traceback_utils.py\u001b[0m in \u001b[0;36merror_handler\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    151\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    152\u001b[0m       \u001b[0mfiltered_tb\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_process_traceback_frames\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__traceback__\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 153\u001b[0;31m       \u001b[0;32mraise\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwith_traceback\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfiltered_tb\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    154\u001b[0m     \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    155\u001b[0m       \u001b[0;32mdel\u001b[0m \u001b[0mfiltered_tb\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/tensorflow/python/framework/ops.py\u001b[0m in \u001b[0;36mraise_from_not_ok_status\u001b[0;34m(e, name)\u001b[0m\n\u001b[1;32m   5881\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mraise_from_not_ok_status\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mNoReturn\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   5882\u001b[0m   \u001b[0me\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmessage\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;34m\" name: \"\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mname\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mname\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0;34m\"\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 5883\u001b[0;31m   \u001b[0;32mraise\u001b[0m \u001b[0mcore\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_status_to_exception\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m  \u001b[0;31m# pylint: disable=protected-access\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   5884\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   5885\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mInvalidArgumentError\u001b[0m: {{function_node __wrapped__Pack_N_2_device_/job:localhost/replica:0/task:0/device:CPU:0}} Shapes of all inputs must match: values[0].shape = [10000] != values[1].shape = [10000,10] [Op:Pack] name: stack"
          ]
        }
      ]
    }
  ]
}
