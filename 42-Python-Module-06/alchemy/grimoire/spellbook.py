def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    # this is a late import... yeah refer to the cirular_curse to know

    res = validate_ingredients(ingredients)
    if "VALID" in res:
        return f"Spell recorded: {spell_name} ({res})"
    return f"Spell rejected: {spell_name} ({res})"
