[![](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white)]()
[![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)]()
[![](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)]()
# <img src="project-img/ethbox_icon.svg" alt="drawing" width="20"/>  Eth-Box 

---
**A Blockchain-Based Solution For Efficient And Secure Video-KYC**

## How to start locally
  *if you want to run the blockchain in real Ethereum network else you can run a local blockchain using Ganache and skip the Infura setup.*
  
### Infura Setup 
- Go to [infura](https://infura.io/) and create a new project, this will give you an endpoint by which you can connect with Ethereum network. 
- Create a wallet and encrypt the wallet using password. [Tutorial](https://youtu.be/SAi5rYFh7yw)
- Save the infura endpoint and password in `secret.json` file like below:
```JSON
{
    "url": "infura-end-point-url",
    "pass":"wallet-password",
    "contract_address": "deployed-contract-address"
}
```
- Save the wallet with name of `wallet.json`

### Ganache Setup
- Download the Ganache software and install. [Download](https://trufflesuite.com/ganache/)
- Switch to Ganache branch
``` bash 
git checkout ganache
```

### Run Web Server 
- Install all requirements 
```bash 
pip install -r requirements.txt
```
- Run the django server 
```bash
python3 manage.py runserver
```

### App
Landing page
<img src="project-img/landing.png" alt="drawing">

<br>

Dashboard
<img src="project-img/dashboard.png" alt="drawing">

<br>

Client Login
<img src="project-img/dash_login.png" alt="drawing">

<br>

Admin page
<img src="project-img/admin.png" alt="drawing">

<br>

Admin login
<img src="project-img/admin_login.png" alt="drawing">