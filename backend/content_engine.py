import os
import yaml

def get_manifest_path():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, 'content', 'manifest.yaml')

def get_manifest():
    manifest_path = get_manifest_path()
    if not os.path.exists(manifest_path):
        return None
    with open(manifest_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def get_lesson_content(node_id):
    manifest = get_manifest()
    if not manifest: return None

    target_node = None
    target_tier = None
    for tier in manifest.get('tiers', []):
        for node in tier.get('nodes', []):
            if node['id'] == node_id:
                target_node = node
                target_tier = tier
                break
        if target_node: break

    if not target_node: return None

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    content_dir = os.path.join(base_dir, 'content')

    exercises = []
    for drill in target_node.get('drills', []):
        starter_code = ""
        assertions = ""

        drill_dir = os.path.join(content_dir, target_tier['id'], target_node['id'])
        
        ex_path = os.path.join(drill_dir, drill.get('exercise_file', ''))
        test_path = os.path.join(drill_dir, drill.get('test_file', ''))

        if drill.get('exercise_file') and os.path.exists(ex_path):
            with open(ex_path, 'r', encoding='utf-8') as f:
                starter_code = f.read()

        if drill.get('test_file') and os.path.exists(test_path):
            with open(test_path, 'r', encoding='utf-8') as f:
                assertions = f.read()

        prd_markdown = None
        prd_path = os.path.join(drill_dir, drill.get('prd_file', ''))
        if drill.get('prd_file') and os.path.exists(prd_path):
            with open(prd_path, 'r', encoding='utf-8') as f:
                prd_markdown = f.read()

        exercises.append({
            "starter_code": starter_code,
            "assertions": assertions,
            "id": drill.get("id"),
            "description": drill.get("description", ""),
            "type": drill.get("type", "kata"),
            "prd_markdown": prd_markdown
        })

    if not exercises:
        exercises.append({
            "starter_code": "# No drills currently exist for this node.",
            "assertions": "assert True"
        })

    return {
        "title": target_node.get("name", "Unknown Node"),
        "markdown": f"{target_tier.get('name')} - {target_node.get('name')}\n\n{target_tier.get('description', '')}", 
        "exercises": exercises
    }

def list_lessons():
    manifest = get_manifest()
    if not manifest: return []

    lessons = []
    for tier in manifest.get('tiers', []):
        for node in tier.get('nodes', []):
            lessons.append({
                "id": node['id'],
                "title": f"{tier['name']} - {node['name']}"
            })
    return lessons

def get_dag():
    return get_manifest()
