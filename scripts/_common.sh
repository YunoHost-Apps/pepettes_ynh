#!/bin/bash

#=================================================
# COMMON VARIABLES AND CUSTOM HELPERS
#=================================================

cron_path="/etc/cron.daily/warn-about-attacks-on-donation"

print_price_ids() {
    IFS=',' read -ra prices_array <<< "$prices"

    for price in "${prices_array[@]}"; do
        IFS='/' read -ra price_info <<< "$price"
        frequency="${price_info[0]}"
        currency="${price_info[1]}"
        price_id="${price_info[2]}"
        echo "DONATION['$frequency']['$currency'] = '$price_id'"
    done
}

build_python() {
    pushd "$install_dir"
        ynh_exec_as_app python3 -m venv venv
        ynh_exec_as_app venv/bin/pip install --upgrade pip
        ynh_exec_as_app venv/bin/pip install -r sources/requirements.txt
        ynh_exec_as_app venv/bin/pip install gunicorn
        ynh_hide_warnings ynh_exec_as_app venv/bin/pybabel compile -d sources/locales/
    popd
}
