#!/usr/bin/env python3
# sng.py
# A utility that helps create serial numbers for various enterprises
import random as r
import sys, os
symbols='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
cut='''
=========================
'''
def cl():
    os.system('cls'if os.name=='nt'else 'clear')
def hello():
    cl()
    print(f'''
===== W E L C O M E =====
========== T O ==========
========= S N G =========

           the
 serial_number_generator
''')
    cl()
    input(f'\nPress ENTER to start... ')
hello()
def main():
    try:
        while True:
            cl()
            t=0
            srl=''
            try:
                usr_lng=int(input(f'LENGTH of the SERIAL NUMBER [1 - 9999]: '))
            except ValueError:
                continue
            if usr_lng<=0 or usr_lng>9999:
                continue
            else:
                pass
            try:
                usr_nmb=int(input(f'NUMBER of the SERIAL NUMBERS [1 - 9999]: '))
            except ValueError:
                continue
            if usr_nmb<=0 or usr_nmb>9999:
                continue
            else:
                pass
            print(cut)
            while True:
                x=r.choice(symbols)
                if len(srl)==usr_lng:
                    print(f'{t+1}. {srl}')
                    t+=1
                    srl=''
                else:
                   srl+=x
                if t==usr_nmb:
                   print(cut)
                   usr_cnt=input(f'[A]gain / [Q]uit? ').strip().lower()
                   if usr_cnt=='a':
                       cl()
                       break
                   else:
                       sys.exit()
    except KeyboardInterrupt:
        print(f'\nSNG has been stopped... ')
    except Exception as e:
        print(f'\n[ERROR] -> {e} ')
main()
