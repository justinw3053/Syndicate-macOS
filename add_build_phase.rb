#!/usr/bin/env ruby

require 'xcodeproj'

project_path = 'OpenForge.xcodeproj'
project = Xcodeproj::Project.open(project_path)
target = project.targets.first

# Check if script already exists to avoid duplicates
existing_phase = target.shell_script_build_phases.find { |p| p.name == 'Build Python Runtime' }

if existing_phase.nil?
  puts "Adding 'Build Python Runtime' phase..."
  phase = target.new_shell_script_build_phase('Build Python Runtime')
  phase.shell_script = "bash \"${SRCROOT}/scripts/build_python_runtime.sh\""
  
  # Ensure it runs before the Copy Bundle Resources phase
  target.build_phases.insert(0, target.build_phases.delete(phase))
  
  project.save
  puts "Successfully added build phase."
else
  puts "Build phase already exists."
end
