import os
import random
from os import system
from glob import glob
import csv
import argparse
from subprocess import run
import logging

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

EMAILTAG = "CSC337_CW3_papers"
PAPERDIR = "/home/tom/Documents/teaching/CSC337/1920_TB2/coursework_3/cw3_papers"
PAPERLISTFILE = "/home/tom/Documents/teaching/CSC337/1920_TB2/coursework_3/assigned_papers.csv"

class PaperAssignments(object):
  def __init__(self, fname):
    self.datafile = fname
    self.fieldlist = ['email', 'doi']
    self.assignments = dict()
    # initialize by reading from fname
    self._read()

  def _read(self):
    with open(self.datafile) as csvfile:
      r = csv.DictReader(csvfile)
      for row in r:
        self.assignments[row['email']] = row

  def _write(self):
    # save everything
    for v in self.assignments.values():
      for k in v.keys():
        if k not in self.fieldlist:
          self.fieldlist.append(k)
    logging.debug(f"new fieldlist: {self.fieldlist}")
    with open(self.datafile, 'w') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=self.fieldlist)
      writer.writeheader()
      for email,v in self.assignments.items():
        v['email'] = email
        writer.writerow(v)

  def assign(self, email, paper):
    logging.debug(paper)
    # assign the paper to the student
    info = self.assignments.get(email, {})
    info['doi'] = paper.doi
    self.assignments[email] = info

    # save the assignments when done
    self._write()

  def __len__(self):
    return len(self.assignments)

  def __setitem__(self, key, value):
    self.assign(key, value)

  def __contains__(self, item):
    return item in self.assignments

class Paper(object):
  def __init__(self, path):
    self.path = path
    self.fname = path.split("/")[-1]
    self.doi = self.fname.replace('.pdf', '').replace('_', '/')
    # It would be nice to look up the other information

  @property
  def citation(self):
    return "none right now"

def getemails():
  proc = run(["notmuch", "address", "--output=address", f"tag:{EMAILTAG}"], capture_output=True)
  logging.debug(proc.stdout)
  stdout = proc.stdout.decode("utf-8")
  for email in stdout.split("\n"):
    email = email.strip()
    if email != '': yield email

def getpapers():
  for paper in glob(f"{PAPERDIR}/*"):
    yield Paper(paper)

def papers(start):
  paperlist = list(getpapers())
  logging.debug(f"papers: {[p.doi for p in paperlist]}")

  if start == 0:
    start = random.randint(0, len(paperlist))
  start = start % len(paperlist) # make sure paper index doesn't 
                                 # go off the end of the array

  logging.debug(f"start idx: {start}")
  while True:
    # use Alma's idea
    ids = list(range(len(paperlist)))
    ids.remove(start)
    i = random.choice(ids)
    start = i # don't select this paper again

    np = paperlist[i]
    logging.debug(f"next paper: {np.doi}")
    yield np

def sendmail(msg):
  with open('/tmp/sendmsg', 'w') as m:
    m.write(str(msg))
  toaddr = msg['To']
  system(f"cat /tmp/sendmsg | msmtp -a work {toaddr}")

def papermail(email, paper):
  msg = MIMEMultipart()
  msg['From'] = "t.d.torsney-weir@swansea.ac.uk"
  #msg['To'] = "torsneyt@gmail.com"
  msg['To'] = email
  msg['Subject'] = "CSC337/CSCM37 paper assignment"

  body = f"""
  Hello,

  Your assigned paper can be found at the url: https://dx.doi.org/{paper.doi}. It is also available on blackboard under Course Documents and Content -> CW3 papers (https://bb.swan.ac.uk/webapps/blackboard/content/listContentEditable.jsp?content_id=_3208757_1&course_id=_59066_1&content_id=_3572645_1).

  Please let me know if you have difficulty downloading the paper. 

  Best,
  Tom
  """
  msg.attach(MIMEText(body))
  #with open(paper.path, 'rb') as fb:
    #part = MIMEApplication(fb.read(), Name=paper.fname)
  #part['Content-Disposition'] = f'attachment; filename="{paper.fname}"'
  #msg.attach(part)

  return msg

def sendemail(email, paper):
  msg = papermail(email, paper)
  logging.debug(str(msg))
  sendmail(msg)

def assignpapers(tag, paperdir, paperlistfile):
  assignments = PaperAssignments(paperlistfile)
  logging.debug(f"num assignments: {len(assignments)}")
  mypapers = papers(len(assignments))
  for email in getemails():
    logging.debug(f"checking {email}")
    # only assign new students papers
    if email not in assignments:
      paper = next(mypapers)
      assignments[email] = paper
      sendemail(email, paper)
      logging.info("assigned %s to %s", paper.doi, email)

if __name__ == '__main__':
  # configure logger
  scriptname = os.path.basename(__file__)
  parser = argparse.ArgumentParser(scriptname)
  levels = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
  parser.add_argument('--log-level', default='INFO', choices=levels)
  options = parser.parse_args()
  
  logging.basicConfig(level=options.log_level,
                      format='%(levelname)s %(message)s')

  assignpapers(EMAILTAG, PAPERDIR, PAPERLISTFILE)

