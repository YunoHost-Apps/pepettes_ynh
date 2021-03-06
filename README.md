# Pepettes app for YunoHost

[![Integration level](https://dash.yunohost.org/integration/pepettes.svg)](https://dash.yunohost.org/appci/app/pepettes) ![](https://ci-apps.yunohost.org/ci/badges/pepettes.status.svg) ![](https://ci-apps.yunohost.org/ci/badges/pepettes.maintain.svg)  
[![Install pepettes with YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=pepettes)

*[Lire ce readme en français.](./README_fr.md)*

> *This package allows you to install pepettes quickly and simply on a YunoHost server.  
If you don't have YunoHost, please consult [the guide](https://yunohost.org/#/install) to learn how to install it.*

## Overview
Pepettes is a donation form based on Stripe.

**Shipped version:** 1.0

## Screenshots

(none yet)

## Demo

* [Official demo](https://donate.yunohost.org)

## Configuration

How to configure this app: During the installation, or in `settings.py` after installation.

## Documentation

 * Official documentation: https://github.com/YunoHost/pepettes/blob/main/README.md
 * YunoHost documentation: -

## YunoHost specific features

#### Multi-user support

Are LDAP and HTTP auth supported? n/a
Can the app be used by multiple users? yes

#### Supported architectures

* x86-64 - [![Build Status](https://ci-apps.yunohost.org/ci/logs/pepettes%20%28Apps%29.svg)](https://ci-apps.yunohost.org/ci/apps/pepettes/)
* ARMv8-A - [![Build Status](https://ci-apps-arm.yunohost.org/ci/logs/pepettes%20%28Apps%29.svg)](https://ci-apps-arm.yunohost.org/ci/apps/pepettes/)

## Limitations

(none)

## Additional information

(none)

## Links

 * Report a bug: https://github.com/YunoHost-Apps/pepettes_ynh/issues
 * Upstream app repository: https://github.com/YunoHost/pepettes/
 * YunoHost website: https://yunohost.org/

---

## Developer info

Please send your pull request to the [testing branch](https://github.com/YunoHost-Apps/pepettes_ynh/tree/testing).

To try the testing branch, please proceed like that.
```
sudo yunohost app install https://github.com/YunoHost-Apps/pepettes_ynh/tree/testing --debug
or
sudo yunohost app upgrade pepettes -u https://github.com/YunoHost-Apps/pepettes_ynh/tree/testing --debug
```
