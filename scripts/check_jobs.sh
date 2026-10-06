#!/bin/bash
# One-off, read-only status check of the redo runs. The user runs this on the Mac whenever they
# want a status. It opens one SSH session and only calls squeue, sacct, grep, tail and wc; it
# starts nothing on the cluster. Agents may run it on a schedule, at most once every 30 minutes
# (../../what_agents_need_to_know/andromeda_cluster.md, rule changed by the user 2026-09-28).
# Needs the SSH control connection: ssh -o ControlMaster=auto -o ControlPersist=8h \
#   -o ControlPath=/tmp/ssh-jlens_mm liucfe@andromeda.bc.edu true
set -euo pipefail
SOCK=${SOCK:-/tmp/ssh-jlens_mm}
ssh -o ControlPath="$SOCK" liucfe@andromeda.bc.edu 'cd /scratch/liucfe/jlens_redo
date
echo "=== running"
squeue -u liucfe -h -t RUNNING -o "%.9i %.34j %.10M %R"
echo "=== pending, by reason (DependencyNeverSatisfied = an earlier job in the chain failed)"
squeue -u liucfe -h -t PENDING -o "%R" | sort | uniq -c
echo "=== failed, timed out, out of memory or node failure in the last 12 h (cancellations not shown)"
sacct -u liucfe -X -n -S now-12hours -E now -s F,TO,OOM,NF -o JobID,JobName%34,State,Elapsed || true
echo "=== latest progress of each running job"
for id in $(squeue -u liucfe -h -t RUNNING -o %i); do
  logs=$(ls slurm/logs/*_"$id".out slurm/logs/*_"$id".err 2>/dev/null || true)
  [ -n "$logs" ] || continue
  echo "--- $(squeue -h -j "$id" -o %j) ($id)"
  grep -h -m1 "response limit" $logs || true
  grep -h -E "items \(|judged:|transcripts \(|parts \(" $logs | tail -1 || true
  grep -h -E "FATAL|Traceback|Error" $logs | tail -3 || true
done
echo "=== samples so far"
for m in qwen3_6_27b gpt_oss_20b gemma_3_27b_it gemma_3_12b_it; do
  f=runs/$m/samples.jsonl
  if [ -f "$f" ]; then printf "%-16s %s\n" "$m" "$(wc -l < "$f")"; else printf "%-16s none yet\n" "$m"; fi
done'
