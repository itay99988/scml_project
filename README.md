SCML 2021 Agent Skeleton
========================

This skeleton contains the following folders:

1. myagent: This folder contains one main module: 
   - *YIYAgent.py* : Our agent.
  
2. report: A folder with latex and docx files that you can use to write 
   your 2-4 pages report. Please remember to submit a `pdf` version of the 
   report. A sample PDF is also provided for reference.

Using the Skeleton
==================

To develop your agent, the only required steps are the following:

1. [recommended] create a virtual environment
  - Install venv

    > python3 -m venv .venv
  
  - Activate the virtual environment:
  
    - On linux  

      > source .venv/bin/activate
  
    - On windows (power shell)  

      > call .venv\bin\activate.bat

2. [required] **Install scml**  
    > pip install scml

3. [recommended] Test the installation by running a simple simulation  
    > scml run2020 --steps=10

4. [recommended] Change the name of the agent class from `MyAgent' to 
   your-agent-name.
5. Change the implementation of whatever functions you need in the provided 
   factory manager
6. [recommended] Modify the name of either ``../report/myagent.tex`` or 
   ``../report/myagent.docx`` to ``../report/your-agent-name.tex`` or 
   ``../report/your-agent-name.docx`` as appropriate and use it to write your
   report.
7. [recommended] You can run a simple tournament of your agent against basic
   strategies by either running ``myagent.py`` from the command line   
    > python myagent.py

   or using the CLI as described in the documentation
8. [required] **Submit your agent**: After developing your agent, 
  zip ``your-agent-name`` folder into ``your-team-name_your-agent-name.zip`` 
  (with the pdf or the report included)  and submit it along with 
  ``your-agent-name.pdf`` (after generating it from the tex or docx file). 
  This is the only file you need to submit. 

*Submissions start on February 15th 2020 at https://scml.cs.brown.edu*
  
Agent Information
-----------------

  - Agent Name: YIYAgent
  - Team Name: Team 78
  - Contact Email: itay.cohen5@live.biu.ac.il
  - Affiliation: Bar Ilan University, Computer Science
  - Country: Israel
  - Team Members:
    1. Yoel Benabou - yoel.benabou@gmail.com
    2. Yehoshua Stern - shukistern@gmail.com
    3. Itay Cohen - itay.cohen5@live.biu.ac.il
