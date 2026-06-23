# PRD: Trajectory Auditor
Implement `audit_trajectory(log, illegal_transitions, mandatory_checkpoints) -> list[str]`.
Returns an error string if a mandatory checkpoint is not in the log, or if adjacent elements in the log form an illegal tuple.
