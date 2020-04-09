# Description

A tool for communicating between devices simply by using file cloud storage services.

Communication is a matter of writing and reading files in the cloud.

# Purpose

I initially wrote it for my personal use. It can be very helpful to do anything in your PC from anywhere!

# How it Works

You run Wakeel alongside another applications for syncing your files (most cloud storage providers have file sync. applications). Wakeel must be configured to listen to files in a synced folder and write responses to anoother synced folder. 

You communicate with Wakeel by writing files containing commands, and waiting for responses. 

# Usage

* Wakeel does not sync your device with the cloud, so you need to install an application for file synchronization. Most providers have sync tools.
1. Run Wakeel
   
   * Wakeel will try to locate the sync directory for: Google drive, Dropbox, or One Drive. It will ask you to put two paths manually (one for the requests directory and one for the responses directory) if it didn't find any.

2. Now write files in the configured folder from anywhere (web, mobile app).
   
   - See the **Request File Structure** section to know how to write commands prooperly.

3- Wait for responses in the configured responses folder. The response file will have the same name as the request file.

# Request File Structure

A normal txt file with a single line.  The line starts by the name of the command, followed by a list of parameters. The parameters list is seperatetd by ','.

The general structure is:

    command param1, param2...paramN

Parameters depend on the command that precedes them. Some commands don't have any prameter.

# Commands List

- `list root`
  
  - Lists all the files in your PC, starting from `root`.



## TODO:

* `shell command`
  
  * Executes `command` in the shell.

* `copy path1 path2`
  
  * Copies the file in `path1` to `path2`.

* `upload path`
  
  * Uploads the file in `path`.

* `find file_name`
  
  * Searches for the file named `file_name`.

# Possible Enhancements

* More commands

* GUI

* Installation option

* Should be standalone (should not depend on sync applications)
