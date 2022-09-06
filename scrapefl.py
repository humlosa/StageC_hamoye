{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a3f6d685",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importing Libraries\n",
    "import requests\n",
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6c9bdc45",
   "metadata": {},
   "outputs": [],
   "source": [
    "#feeding url\n",
    "url = \"https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off\"\n",
    "page=requests.get(url)\n",
    "html=page.content"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9296772f",
   "metadata": {},
   "outputs": [],
   "source": [
    "response=requests.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2ecbf52f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Response [200]>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response #itworks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5d4203b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#finding data to extract\n",
    "soup=BeautifulSoup(response.text, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "87084b52",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "main_box=soup.find_all(\"a\", {\"class\":\"_1fQZEK\"})\n",
    "len(main_box)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "27b73b6b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<a class=\"_1fQZEK\" href=\"/lenovo-ideapad-3-chromebook-celeron-dual-core-4-gb-64-gb-emmc-storage-chrome-os-cb-11igl05-2/p/itmf18cb6b3a7e8e?pid=COMG6AKVN3KXNVY2&amp;lid=LSTCOMG6AKVN3KXNVY2LCOHHL&amp;marketplace=FLIPKART&amp;q=laptops&amp;store=6bo%2Fb5g&amp;srno=s_1_1&amp;otracker=search&amp;otracker1=search&amp;fm=organic&amp;iid=en_JJq%2BIIwSMtCD9wR3cuq%2F7f%2BvJA2RTxToYvFrd4JMOpuZyM1%2BYgquIMrNrtdH3ahcQ7Mt1NfWw0HWFENDClb8%2FQ%3D%3D&amp;ppt=None&amp;ppn=None&amp;ssid=zhqrh2wedc0000001662493667073&amp;qH=c06ea84a1e3dc3c6\" rel=\"noopener noreferrer\" target=\"_blank\"><div class=\"MIXNux\"><div class=\"_2QcLo-\"><div><div class=\"CXW8mj\" style=\"height:200px;width:200px\"><img alt=\"Lenovo IdeaPad 3 Chromebook Celeron Dual Core - (4 GB/64 GB EMMC Storage/Chrome OS) ideapad 3 cb 11igl...\" class=\"_396cs4 _3exPp9\" src=\"https://rukminim1.flixcart.com/image/312/312/ksyz8280/computer/9/p/s/cb-11igl05-thin-and-light-laptop-lenovo-original-imag6fh843twh7fh.jpeg?q=70\"/></div></div></div><div class=\"_3wLduG\"><div class=\"_3PzNI-\"><span class=\"f3A4_V\"><label class=\"_2iDkf8\"><input class=\"_30VH1S\" readonly=\"\" type=\"checkbox\"/><div class=\"_24_Dny\"></div></label></span><label class=\"_6Up2sF\"><span>Add to Compare</span></label></div></div><div class=\"_2hVSre _3nq8ih\"><div class=\"_36FSn5\"><svg class=\"_1l0elc\" height=\"16\" viewbox=\"0 0 20 16\" width=\"16\" xmlns=\"http://www.w3.org/2000/svg\"><path class=\"eX72wL\" d=\"M8.695 16.682C4.06 12.382 1 9.536 1 6.065 1 3.219 3.178 1 5.95 1c1.566 0 3.069.746 4.05 1.915C10.981 1.745 12.484 1 14.05 1 16.822 1 19 3.22 19 6.065c0 3.471-3.06 6.316-7.695 10.617L10 17.897l-1.305-1.215z\" fill=\"#2874F0\" fill-rule=\"evenodd\" opacity=\".9\" stroke=\"#FFF\"></path></svg></div></div></div><div class=\"_3pLy-c row\"><div class=\"col col-7-12\"><div class=\"_4rR01T\">Lenovo IdeaPad 3 Chromebook Celeron Dual Core - (4 GB/64 GB EMMC Storage/Chrome OS) ideapad 3 cb 11igl...</div><div class=\"gUuXy-\"><span class=\"_1lRcqv\" id=\"productRating_LSTCOMG6AKVN3KXNVY2LCOHHL_COMG6AKVN3KXNVY2_\"><div class=\"_3LWZlK\">3.5<img class=\"_1wB99o\" src=\"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==\"/></div></span><span class=\"_2_R_DZ\"><span><span>874 Ratings </span><span class=\"_13vcmD\">&amp;</span><span> 104 Reviews</span></span></span></div><div class=\"fMghEO\"><ul class=\"_1xgFaf\"><li class=\"rgWa7D\">Intel Celeron Dual Core Processor</li><li class=\"rgWa7D\">4 GB LPDDR4 RAM</li><li class=\"rgWa7D\">Chrome Operating System</li><li class=\"rgWa7D\">29.46 cm (11.6 Inch) Display</li><li class=\"rgWa7D\">1 Year Warranty</li></ul></div></div><div class=\"col col-5-12 nlI3QM\"><div class=\"_3tbKJL\"><div class=\"_25b18c\"><div class=\"_30jeq3 _1_WHN1\">₹16,990</div><div class=\"_3I9_wc _27UcVY\">₹<!-- -->24,840</div><div class=\"_3Ay6Sb\"><span>31% off</span></div></div><div class=\"_3tcB5a p8ucoS\"><div><div class=\"_2Tpdn3\" style=\"color:#000000;font-size:12px;font-weight:400\">Free delivery</div></div></div></div><div class=\"_13J9qT\"><img height=\"21\" src=\"//static-assets-web.flixcart.com/fk-p-linchpin-web/fk-cp-zion/img/fa_62673a.png\"/></div><div class=\"_2ZdXDB\"><div class=\"_3xFhiH\"><div class=\"_2Tpdn3 _18hQoS\" style=\"color:#000000;font-size:14px;font-style:normal;font-weight:400\">Upto </div><div class=\"_2Tpdn3 _18hQoS\" style=\"color:#000000;font-size:14px;font-style:normal;font-weight:700\">₹15,350</div><div class=\"_2Tpdn3 _18hQoS\" style=\"color:#000000;font-size:14px;font-style:normal;font-weight:400\"> Off on Exchange</div></div></div><div class=\"_2ZdXDB\"><div class=\"_3xFhiH\"><div class=\"_2Tpdn3 _18hQoS\" style=\"color:#26A541;font-size:14px;font-weight:700\">Bank Offer</div></div></div></div></div></a>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#reading data\n",
    "box=main_box[0]\n",
    "box"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "d6a9450f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lenovo IdeaPad 3 Chromebook Celeron Dual Core - (4 GB/64 GB EMMC Storage/Chrome OS) ideapad 3 cb 11igl... ₹16,990 3.5\n"
     ]
    }
   ],
   "source": [
    "#data extraction\n",
    "title=box.find(\"div\", {\"class\":\"_4rR01T\"}).text.strip()\n",
    "price=box.find(\"div\", {\"class\":\"_30jeq3 _1_WHN1\"}).text.strip()\n",
    "rating=box.find(\"div\", {\"class\":\"_3LWZlK\"}).text.strip()\n",
    "\n",
    "print(title,price,rating)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "405b25bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_list = []\n",
    "for box in main_box:\n",
    "    temp_dict={}\n",
    "    temp_dict ['Title'] = box.find(\"div\", {\"class\":\"_4rR01T\"}).text.strip()\n",
    "    temp_dict ['Price'] = box.find(\"div\", {\"class\":\"_30jeq3 _1_WHN1\"}).text.replace('₹', '').strip()\n",
    "    temp_dict ['Rating']= box.find(\"div\", {\"class\":\"_3LWZlK\"})\n",
    "    data_list.append(temp_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "e072f002",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>Title</th>\n",
       "      <th>Price</th>\n",
       "      <th>Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Lenovo IdeaPad 3 Chromebook Celeron Dual Core ...</td>\n",
       "      <td>16,990</td>\n",
       "      <td>[3.5, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>DELL Inspiron Pentium Silver - (8 GB/256 GB SS...</td>\n",
       "      <td>31,990</td>\n",
       "      <td>[4.1, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ASUS VivoBook K15 OLED Ryzen 7 Octa Core 5700U...</td>\n",
       "      <td>69,990</td>\n",
       "      <td>[4.3, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...</td>\n",
       "      <td>35,990</td>\n",
       "      <td>[4.3, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ASUS ROG Strix G15 Ryzen 7 Octa Core 4800H - (...</td>\n",
       "      <td>95,990</td>\n",
       "      <td>[4.8, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>HP Pavilion Ryzen 5 Hexa Core 5600H - (8 GB/51...</td>\n",
       "      <td>58,990</td>\n",
       "      <td>[4.5, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>ASUS Vivobook Ryzen 9 Octa Core 5900HX - (16 G...</td>\n",
       "      <td>1,24,990</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>DELL Inspiron Athlon Dual Core 3050U - (8 GB/2...</td>\n",
       "      <td>31,490</td>\n",
       "      <td>[4.2, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Lenovo IdeaPad 3 Ryzen 5 Hexa Core 5500U - (8 ...</td>\n",
       "      <td>47,990</td>\n",
       "      <td>[4.3, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...</td>\n",
       "      <td>55,990</td>\n",
       "      <td>[4.3, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>DELL Inspiron Ryzen 3 Dual Core 3250U - (8 GB/...</td>\n",
       "      <td>35,490</td>\n",
       "      <td>[4.3, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>DELL Ryzen 3 Dual Core 3250U - (8 GB/1 TB HDD/...</td>\n",
       "      <td>36,990</td>\n",
       "      <td>[4.4, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>DELL Inspiron Core i3 11th Gen - (8 GB/1 TB HD...</td>\n",
       "      <td>42,890</td>\n",
       "      <td>[4.3, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>acer Aspire 7 Ryzen 5 Hexa Core 5500U - (8 GB/...</td>\n",
       "      <td>52,990</td>\n",
       "      <td>[4.5, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>ASUS VivoBook 15 (2022) Core i5 10th Gen - (8 ...</td>\n",
       "      <td>43,990</td>\n",
       "      <td>[4.3, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>ASUS VivoBook 14 (2022) Ryzen 5 Quad Core 3500...</td>\n",
       "      <td>41,990</td>\n",
       "      <td>[4.4, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>ASUS VivoBook 14 (2021) Celeron Dual Core - (4...</td>\n",
       "      <td>25,990</td>\n",
       "      <td>[4.2, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>DELL Inspiron Core i3 11th Gen - (8 GB/1 TB HD...</td>\n",
       "      <td>38,690</td>\n",
       "      <td>[3.6, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...</td>\n",
       "      <td>38,990</td>\n",
       "      <td>[4.2, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>ASUS Vivobook 15 Core i3 10th Gen - (8 GB/256 ...</td>\n",
       "      <td>32,990</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>DELL Inspiron Core i5 11th Gen - (8 GB/1 TB HD...</td>\n",
       "      <td>67,390</td>\n",
       "      <td>[3.9, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>DELL Core i7 11th Gen - (16 GB/512 GB SSD/Wind...</td>\n",
       "      <td>1,02,990</td>\n",
       "      <td>[4.3, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>MSI Modern 14 Ryzen 5 Hexa Core 5500U - (8 GB/...</td>\n",
       "      <td>44,990</td>\n",
       "      <td>[4.4, []]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...</td>\n",
       "      <td>33,990</td>\n",
       "      <td>[4.3, []]</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                Title     Price     Rating\n",
       "0   Lenovo IdeaPad 3 Chromebook Celeron Dual Core ...    16,990  [3.5, []]\n",
       "1   DELL Inspiron Pentium Silver - (8 GB/256 GB SS...    31,990  [4.1, []]\n",
       "2   ASUS VivoBook K15 OLED Ryzen 7 Octa Core 5700U...    69,990  [4.3, []]\n",
       "3   ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...    35,990  [4.3, []]\n",
       "4   ASUS ROG Strix G15 Ryzen 7 Octa Core 4800H - (...    95,990  [4.8, []]\n",
       "5   HP Pavilion Ryzen 5 Hexa Core 5600H - (8 GB/51...    58,990  [4.5, []]\n",
       "6   ASUS Vivobook Ryzen 9 Octa Core 5900HX - (16 G...  1,24,990       None\n",
       "7   DELL Inspiron Athlon Dual Core 3050U - (8 GB/2...    31,490  [4.2, []]\n",
       "8   Lenovo IdeaPad 3 Ryzen 5 Hexa Core 5500U - (8 ...    47,990  [4.3, []]\n",
       "9   ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/5...    55,990  [4.3, []]\n",
       "10  DELL Inspiron Ryzen 3 Dual Core 3250U - (8 GB/...    35,490  [4.3, []]\n",
       "11  DELL Ryzen 3 Dual Core 3250U - (8 GB/1 TB HDD/...    36,990  [4.4, []]\n",
       "12  DELL Inspiron Core i3 11th Gen - (8 GB/1 TB HD...    42,890  [4.3, []]\n",
       "13  acer Aspire 7 Ryzen 5 Hexa Core 5500U - (8 GB/...    52,990  [4.5, []]\n",
       "14  ASUS VivoBook 15 (2022) Core i5 10th Gen - (8 ...    43,990  [4.3, []]\n",
       "15  ASUS VivoBook 14 (2022) Ryzen 5 Quad Core 3500...    41,990  [4.4, []]\n",
       "16  ASUS VivoBook 14 (2021) Celeron Dual Core - (4...    25,990  [4.2, []]\n",
       "17  DELL Inspiron Core i3 11th Gen - (8 GB/1 TB HD...    38,690  [3.6, []]\n",
       "18  Lenovo IdeaPad 3 Core i3 11th Gen - (8 GB/512 ...    38,990  [4.2, []]\n",
       "19  ASUS Vivobook 15 Core i3 10th Gen - (8 GB/256 ...    32,990       None\n",
       "20  DELL Inspiron Core i5 11th Gen - (8 GB/1 TB HD...    67,390  [3.9, []]\n",
       "21  DELL Core i7 11th Gen - (16 GB/512 GB SSD/Wind...  1,02,990  [4.3, []]\n",
       "22  MSI Modern 14 Ryzen 5 Hexa Core 5500U - (8 GB/...    44,990  [4.4, []]\n",
       "23  ASUS VivoBook 15 (2022) Core i3 10th Gen - (8 ...    33,990  [4.3, []]"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#saving lists in dataframe format\n",
    "df=pd.DataFrame(data_list)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "11dea056",
   "metadata": {},
   "outputs": [],
   "source": [
    "#storing data in csv format in said file\n",
    "df.to_csv('laptop.csv', index=False, encoding='utf-8')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71134f03",
   "metadata": {},
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
