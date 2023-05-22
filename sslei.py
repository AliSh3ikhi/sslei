#!/usr/bin/python3

######################################
## Author: AliSh3ikhi (~_^)         ##
## Date: 05/22/2023                 ##
## Modify: 05/22/2023 - v01         ##
## Usage: Run on all subs        :) ##
######################################

import subprocess
import argparse

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode == 0:
        print(output.decode('utf-8'))
    else:
        print(f"Error occurred during command execution.")
        print(error.decode('utf-8'))

def process_single_url(url, ssl_path):
    command = f'echo {url} | nuclei -t {ssl_path} -silent -json | jq -r \'.["extracted-results"][]\''
    run_command(command)

def process_url_list(file_path, ssl_path):
    command = f'cat {file_path} | nuclei -t {ssl_path} -silent -json | jq -r \'.["extracted-results"][]\''
    run_command(command)

def main():
    default_ssl_path = '~/nuclei-templates/Custom/ssl.yaml'
    
    parser = argparse.ArgumentParser(description='Process URLs using nuclei command')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', dest='single_url', help='Single URL to process')
    group.add_argument('-l', dest='file_path', help='File containing a list of URLs to process')
    parser.add_argument('-t', dest='ssl_path', default=default_ssl_path, help='Custom path for the -t option')
    args = parser.parse_args()

    if args.single_url:
        process_single_url(args.single_url, args.ssl_path)
    elif args.file_path:
        process_url_list(args.file_path, args.ssl_path)

if __name__ == '__main__':
    main()
