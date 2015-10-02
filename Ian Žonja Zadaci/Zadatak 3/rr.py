{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": ""
   },
   "outputs": [],
   "source": [
    "import ravnina\n",
    "import argparse"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": ""
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vektor(0, -1)\n",
      "Vektor(-2, -5)\n",
      "Vektor(-2, -6)\n",
      "Vektor(16, 12)\n"
     ]
    }
   ],
   "source": [
    "a = ravnina.Vektor(-1,-3)\n",
    "b = ravnina.Vektor(1,2)\n",
    "c = ravnina.Vektor(4,3)\n",
    "\n",
    "print (a + b)\n",
    "print (a - b)\n",
    "print(a * 2)\n",
    "print(c * 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": ""
   },
   "outputs": [],
   "source": [
    "def Main():\n",
    "    parse = argparse.ArgumentParser()\n",
    "    group = parser.add_mutually_exclusive_group()\n",
    "    group.add_argument(\"--add\",action = \"store_true\")\n",
    "    group.add_argument(\"--verbose\", action = \"store_true\")\n",
    "    parse.add_argument(\"list1\", type = list)\n",
    "    parse.add_argument(\"list2\", type = list)\n",
    "    \n",
    "    args1 = parse.parse_args(\"list1\")\n",
    "    args2 = pare.parse_args(\"list2\")\n",
    "    \n",
    "    pom1 = args1[0]\n",
    "    pom2 = args1[1]\n",
    "    pom3 = args2[0]\n",
    "    pom4 = args2[1]\n",
    "    \n",
    "    a = ravnina.Vektor(pom1,pom2)\n",
    "    b = ravnina.Vektor(pom3,pom4)\n",
    "    \n",
    "    if args1.add & args2.add:\n",
    "        print(a+b)\n",
    "    else:\n",
    "        print(\"qwert\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": ""
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "usage: __main__.py [-h] [--add] list1 list2\n",
      "__main__.py: error: unrecognized arguments: s t 1\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "2",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 2\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "To exit: use 'exit', 'quit', or Ctrl-D.\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    Main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.4.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
