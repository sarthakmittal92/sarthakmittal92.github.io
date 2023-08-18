# midsem autograders

1. install required python packages using the following command (in the directory where this
README is present):
```sh
python3 -m pip install -r requirements.txt
```

2. for each activity, first download your VLab submission archive for the one you want to
evaluate

3. place this archive (should be named as <roll-number>@iitb.ac.in.tar.gz, for example,
200050129@iitb.ac.in.tar.gz) inside the "submission" folder within the activity folder
present here (for example, within a1-bash/submission, if you want to evaluate bash)

4. cd into the activity folder here (example: cd a1-bash) and then run the following:
```sh
bash run.sh <roll-number>
```
For example, "bash run.sh 200050129"

5. look at the output given by the autograder and accordingly fill in your issues

6. reach out to us in case of any other autograder related issues
