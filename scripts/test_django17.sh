reset
./scripts/uninstall.sh
./scripts/install_django17.sh
#cd ..
python examples/simple/manage.py test fobi --settings=settings_bootstrap3_theme_django17 --traceback -v 3
#cd scripts