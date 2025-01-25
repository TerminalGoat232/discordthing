#!/bin/bash
let check_for_setup_req_tools=`python -c "import importlib.util; a = [(1 if importlib.util.find_spec(p) else 0) for p in ['pipreqs','piptools']];print(a[0] and a[1])"`
if [[ $check_for_setup_req_tools -ne 1 ]]; then 
  echo "seem like you forgot to install pipreqs or piptools, lemme do it for ya..."
  pip install pipreqs pip-tools 
  echo "done!"
fi 
echo "generating requirements.txt.."
pipreqs --savepath=requirements.in && pip-compile
echo "install packages required in requirements.txt? [y/n]"
read option
case $option in 
  "y") pip install -r requirements.txt ;;
  "n") echo "ok nvm";;
esac 



