# DIY RC Car (v1.0)

## Description
This project is a web app that is used to control a car remotely.

>[!important]
> Soldering is required to get this project working.

## Requirements

### Software
Python 3.10 or higher (May work on 3.8 and up, but was tested on 3.11).
flask
RPi.GPIO

### Hardware
- RC Kit Car 
- Raspberry Pi Zero 2W Kit
- L298N Motor Driver
- Jumper Wires
- Rechargable AA Batteries
- AA Battery Charger
- Power Bank
- Optional Parts:
  - Solderless Breadboard
  - Color LEDs(4)
  - 1k (1000) Ohm Resistors(4)
  - Buzzer

## Cost
- [RC Car Kit - $21.49](https://www.amazon.com/YIKESHU-Smart-Chassis-Encoder-Battery/dp/B075LD4FPN/ref=sr_1_17?crid=P7F1YDXU60SS&dib=eyJ2IjoiMSJ9.a6uay3wgxa3P_hqZefW2nRh-1822EJLgTajvlROkp-UXpm_f_uJ8JFyBP_cvU4Ish7fp7rLlDtLX8kUYsFF3TDIbvP8pKI-l3lWXKPXTXM7EOHY4Ob_k7FH5zj0MJb8IqqprcJ5qsLqlc0DDqMj6MCjVrfRkdbLVI0yRno65l5N0leQij26jC0s7huS7DX_Etd3IUY6xIyyGqMkWktXIYY8Ux1aYW7g5qcp11tci6eJjCnWdufEeaHpOC2N1-D2ZVy1NTNZaVvrLP2sIOO_mN8rNKmXsZMB7m9Ri2Kzrycw.af952jngF7K3BiIB5ZDfMLrZYwS958rjmDFfhBtMM5I&dib_tag=se&keywords=DIY+rc+car&qid=1721684613&sprefix=diy+rc+car%2Caps%2C131&sr=8-17)
- [Raspberry Pi Zero 2W Kit - $42.95](https://www.pishop.us/product/raspberry-pi-zero-w-budget-pack/)
- [L298N Motor Driver - $11.49](https://www.amazon.com/dp/B07BK1QL5T?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Jumper Wires - $6.98](https://www.amazon.com/Elegoo-EL-CP-004-Multicolored-Breadboard-arduino/dp/B01EV70C78/ref=sr_1_1_sspa?crid=1ISXMFRYGO4N4&dib=eyJ2IjoiMSJ9.tjHxIQLJsk16_0YVtUGN6ezmMKG-B29Sofx-GdLLKdxMvW06Nb1z_CeoJXYjxmhOT32H_F_YLCXyZaaRbCfYHTA6Sa2kAB-sTD-B6XRU8MN-Vhyck1lNRa_tZeff0i50nHc8j82LrBNqkQpW22aj9nQ2au01KkPy2gC9Dv4Nt-BoqvAiAe0CnvZkd_4sV1IVs9qWSAgGi9hFvYvXNgqqwkBKNDX0l0YRRWFeSSxWjIg.odukbWnYBlHim4_at38zqNBUEMDoYg6MrCiNRYh5lfs&dib_tag=se&keywords=breadboard+jumper+wires+dupont+assortment&qid=1721691799&sprefix=breadboard+jumper+wires+dupont+assortmen%2Caps%2C119&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
- [Rechargable AA Batteries(8-Pack) - $12.43](https://www.amazon.com/dp/B00CWNMV4G?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [AA Battery Charger - $14.25](https://www.amazon.com/dp/B00TOVTZ7K?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Power Bank - $17.99](https://www.amazon.com/gp/product/B07CZDXDG8/ref=ox_sc_act_title_1?smid=ATVPDKIKX0DER&th=1)
- Optional Parts:
  - [Solderless Breadboard(6-Pack) - $8.99](https://www.amazon.com/ELEGOO-Breadboard-Solderless-Breadboards-Electronics/dp/B0CYPVMK9J/ref=sr_1_1_sspa?crid=195T6ND7SQCMJ&dib=eyJ2IjoiMSJ9.X82Ju5tr9ZeC-NuAtMs1hzvAUTARhEbf1bJWDXm0GjWaLvtRZN97hoMSz19GbAm8JaFpzd1ZqpWU3tE_-2WP6JPyZGCIfXmg9Sy0-BAUnqXUMVM2WPfgX6PKahe1nvWkyq3EyBw5OXDA1hqChvBUw-GDh3cgQ1Uogwtpq58fmI_KYIz31QDwkHJvO5AGFBTtFTj8mZy2Ks77QL4iy3D48Xm1sDaeAVXicTtbGqbj10E.-hYgp8nj7zUNELluukTXR3A_2ZqqzKXLwgO5V3QfGh4&dib_tag=se&keywords=solderless+breadboard&qid=1721687354&sprefix=solderless+breadboar%2Caps%2C171&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
  - [Color LEDs - $9.99](https://www.amazon.com/Emitting-Assortment-Individual-Assorted-Breadboard/dp/B096JZHV6Y/ref=sr_1_1_sspa?crid=6J06I3I01P5V&dib=eyJ2IjoiMSJ9.h8EDJUvZcN1XiaYZZP4FKXTHr6n3C4lencVdqZ45ptsKx8zQv8wXGgdjpgSNJ6SvHdckWdiFCdC_zufNzazF322o382bhtSu568rvYcplwVnhEYEX26L_yDoyTfJb7XV4Ko5yvUIe-y7QUDAe8oOxXAVy0h1BeDeEIry4iGfInZCBRk5ncGiKbgx7DLIXGiNwuyA3lARmoOtHWt8UoVNMOTnbFy10AWcU42jO4ilT2Y.IfbhKq5mcOZNvCpRJvU_Q4quy4cc38cZMjorVToZDow&dib_tag=se&keywords=LED+assortment&qid=1721692489&sprefix=led+asso%2Caps%2C234&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
  - [Buzzer - $7.99](https://www.amazon.com/QMseller-Terminals-Raspberry-Electronic-Continous/dp/B07VRK7ZPF/ref=sr_1_2_sspa?crid=1L4LUN06YQBEQ&dib=eyJ2IjoiMSJ9.2DZYL68_ETB1dEvQEC3wyHWZKXYQK3AjwTasZzFVbd97PlCvaEWTTEdSXlNogF6SmoTHwsMrnSevEZhElsrVW-1nYlYHm7m5ae6Tq3O9sF4zKndBRxpmZAKuS_SpOjNHHUMbZgd0Pl2X2slgLO6q3ISYfPmWdA9sqh_OtavZTePQ2tb2z4rXdgonMTH4iKD8QwICmOclSOXRVtYC9ByKlTAMmHhTcP7O0TJdqqmgiL8yCDEYWogMm8Hmq_iULhjG0lNNsmYAtAf1HPJqY42HeukwrUftuQhBPhXAh-LaEhg.t46i5UWenAjkCpTgcYvO0YE_SSLQgwVycon2gRDNCjk&dib_tag=se&keywords=mini+buzzer&qid=1721692616&sprefix=mini+buzzr%2Caps%2C151&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
  - [1kOhm Resistors - $5.74](https://www.amazon.com/Projects-10EP5121K00-Ohm-Resistors-Pack/dp/B0185FK65K/ref=sr_1_5?crid=1R1ESCMVR73HU&dib=eyJ2IjoiMSJ9.XFEPFWdsYxLmpBQgQ5k8AFm_BkI_uogxILcRJZ34XAzxCU1WPdJLnC6ll142ybZSLHSIVBOjOHjFcVbcYbCtzkOdb2RoUzJY6KSE5cNiJ_nVvKaHCOjAohacKG7jiiBBqXtf_Wt8gqSP62fRl6jR9qPI_VeiJOSToVlPIuc1D2Ujp4vTz_icepkyrZudcxeR5jOBS5ltgIEDbX_pufzS5tQ2OsAzSNYW2pAOx7FJPK0.BQkCs2c6kxJ5kc5oMa7YiSNvrOi-uctrVwDf3jcS_K8&dib_tag=se&keywords=resistor+1kohm&qid=1721692789&sprefix=resistor+1kohm%2Caps%2C147&sr=8-5)

> [!Note]
> Prices are always changing and may differ from the listed prices.

## User Guide
### Getting Started
- Setup the Raspberry Pi Zero 2W:
  - [Install Raspberry Pi OS using Raspberry Pi Imager on your personal PC](https://www.raspberrypi.com/software)
  - Insert/connect the SD card to a personal computer.
  - Open the Imager and select "Operating System" > "Raspberry Pi OS (other)" > "Raspberry Pi OS Lite (64-bit)".
  - Then select "Choose Storage" and select the SD card that is installed.
  - Finally select "Write".
  - Once complete, insert the SD card into the Raspberry Pi.
  - Connect the Raspberry Pi to a monitor and connect a keyboard and mouse to the Raspberry Pi.
  - Power it on and once it is booted up, type `sudo raspi-config` to open the configuration page.
  - Setup WiFi by selecting "1 System Options" > "Wireless LAN" > enter network SSID then password.
  - Enable SSH by selecting "3 Interface Options" > "SSH" and select yes to enable.
  - reboot (`sudo shutdown -r now`).
  - If git is not installed on your PC, install it up now.
  - On your personal PC get the setup script to set up the Raspberry Pi by cloning it. From the terminal type `git clone https://github.com/KColagiovanni/RC_Car_v1_RPi_setup_script.git` into the desired directory.
  - From the command line navigate to the directory where the setup scrpit was cloned, and type `scp <RPi host name>@<RPi IP Address>:~ zero2w_setup.sh` to copy it to the Raspberry Pi.

### How to Use
1. Clone this project to any directory and make note of the path to it.
2. In a command prompt window, navigate to the directory where the project was cloned and go into that directory.
3. In a command prompt type `dir`, and verify that the “main.py”, “plot_data.py”, “process_and_train_data.py”, and “diabetes.csv” files are there, if any of those files are not present, go back to step 1.
4. If typing `python –version` in the command prompt window displays `Python 3.11.X`, continue to step 4a. If typing `python3 –version` in the command prompt window displays `Python 3.11.X`, continue to step 4b.
    - a. In a command prompt window, type: “python main.py” and ensure the applicationGUI is displayed.
    - b. In a command prompt window, type: “python3 main.py” and ensure the applicationGUI is displayed. 
5. Once the application is running:

## Credits/Resources
