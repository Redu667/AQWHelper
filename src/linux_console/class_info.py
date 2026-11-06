from linux_console.class_format import ClassDef, Mode, Skill, Slot
from linux_console.platform_utils import get_star_chars

# Get platform-appropriate star characters
_FILLED_STAR, _HOLLOW_STAR = get_star_chars()

# Add a class by appending a ClassDef entry; only fill what you know.
#
# ClassDef(
#     "Example Class",
#     model="Power Melee",
#     description="Text with [bold #ca7a34]colored[/] parts.",
#     skills=(Skill("Skill 1", "Info"), Skill("Skill 2", "Info")),   # up to 5
#     passives=(Skill("Passive 1", "Info"),),                        # 2 or 3
#     base=Mode(
#         cls=Slot(best="Lucky", alternative="Wizard", base="Wizard"),
#         helm=Slot(best="Lucky"),
#         weapon=Slot(best="Lucky Mana Vamp"),
#         cape=Slot(best="Lucky"),
#         tonic="Sage Tonic", elixir="Malevolence Elixir", potion="Felicitous Philtre",
#     ),
#     solo=Mode(...), group=Mode(...), special=Mode(...),
# )
#
# A class that is a duplicate of another reuses its data:
#     ClassDef("Other Name", same_as="Example Class")
# Fields given explicitly still override the inherited ones.

CLASSES: tuple[ClassDef, ...] = (
    ClassDef("Abyssal Angel",
        model="Power Caster",
        description="\n   [b]Roles: [#fbea55]Farming[#ffffff] / [#32ef89]Dodge[#ffffff]\b",
        base=Mode(
            cls=Slot(best='Lucky', base="Wizard"),
            weapon=Slot(best='Lucky', base="Wizard"),
            helm=Slot(best='Lucky', base="Wizard"),
            cape=Slot(best='Lucky', base="Wizard"),
            tonic='Sage Tonic',
            elixir='Malevolece Elixir',
            potion='Felicitous Philtre',
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lacerate', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef("Abyssal Angel's Shadow", same_as="Abyssal Angel"),
    ClassDef('Acolyte', model="Defensive Caster"),
    ClassDef('Alpha DOOMmega',
        model="Tank Melee",
        description="[#fbea55]Solo[#ffffff] / [#32ef89]DPS[#ffffff]\n",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky', alternative='', base=''),
            helm=Slot(best='Thief', alternative='', base=''),
            cape=Slot(best='Thief', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Smite', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
    ),
    ClassDef(
        'Alpha Omega',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky', alternative='', base=''),
            helm=Slot(best='Thief', alternative='', base=''),
            cape=Slot(best='Thief', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Smite', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
    ),
    ClassDef('Alpha Pirate', model="Luck Hybrid"),
    ClassDef('Antique Hunter', same_as="Artifact Hunter"),
    ClassDef(
        'Arachnomancer',
        model="Dodge Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Mana Vamp', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef(
        'Arcana Invoker',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Awe Blast', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Mana Vamp', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Penitence', alternative='', base=''),
        ),
    ),
    ClassDef('Arcane Dark Caster', same_as="Timeless Dark Caster"),
    ClassDef(
        'ArchFiend',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Health Vamp', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Archivist of Temporis', model="Offensive Caster"),
    ClassDef(
        'Archivist of Time',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef(
        'ArchMage',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Acheron', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Absolution', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Awe Blast', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
    ),
    ClassDef(
        'ArchPaladin',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef(
        'Artifact Hunter',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Awe Blast', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Assassin', model="Dodge Melee"),
    ClassDef('Barber', model="Tank Melee"),
    ClassDef(
        'Bard',
        model="Defensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Awe Blast', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Absolution', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Battle Bard', model="Defensive Caster"),
    ClassDef('Battle Healer', model="Defensive Caster"),
    ClassDef('Battle Warrior', model="Tank Melee"),
    ClassDef('BattleMage', same_as="Royal BattleMage"),
    ClassDef('BattleMage of Love', same_as="Royal BattleMage"),
    ClassDef('Beast Warrior', same_as="Warrior"),
    ClassDef('BeastMaster', model="Dodge Melee"),
    ClassDef(
        'Berserker',
        model="Power Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Beta Berserker', same_as="Berserker"),
    ClassDef('BladeMaster', same_as="SwordMaster"),
    ClassDef('BladeMaster Assassin', same_as="SwordMaster Assassin"),
    ClassDef(
        'Blaze Binder',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Mana Vamp', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Blood Ancient', model="Dodge Melee"),
    ClassDef('Blood Sorceress', model="Offensive Caster"),
    ClassDef(
        'Blood Titan',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Fighter', alternative='', base=''),
            helm=Slot(best='Fighter', alternative='', base=''),
            cape=Slot(best='Fighter', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Hearty', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Hearty', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Hearty', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Brutal Berserker', same_as="Berserker"),
    ClassDef('CardClasher', model="Luck Hybrid"),
    ClassDef(
        'Chaos Avenger',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lacerate', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Penitence', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Penitence', alternative='', base=''),
        ),
    ),
    ClassDef('Chaos Avenger Member Preview', same_as="Berserker"),
    ClassDef('Chaos Champion Prime', same_as="Chaos Slayer Berserker"),
    ClassDef(
        'Chaos Shaper',
        model="Luck Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Mana Vamp', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Chaos Slayer Berserker', model="Full Hybrid"),
    ClassDef('Chaos Slayer Cleric', same_as="Chaos Slayer Berserker"),
    ClassDef('Chaos Slayer Mystic', same_as="Chaos Slayer Berserker"),
    ClassDef('Chaos Slayer Thief', same_as="Chaos Slayer Berserker"),
    ClassDef('Chrono Assassin', model="Dodge Melee"),
    ClassDef(
        'Chrono Chaorruptor',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef(
        'Chrono Commandant',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef(
        'Chrono DataKnight',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Chrono DragonKnight', model="Offensive Caster"),
    ClassDef('Chrono ShadowHunter', model="Luck Hybrid"),
    ClassDef(
        'Chrono ShadowSlayer',
        model="Luck Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Thief', alternative='', base=''),
            cape=Slot(best='Thief', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Arcana's Concerto", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Awe Blast', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('ChronoCommander', model="Tank Melee"),
    ClassDef('ChronoCorruptor', model="Full Hybrid"),
    ClassDef(
        'Chronomancer',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Chronomancer Prime', model="Full Hybrid"),
    ClassDef(
        'Chunin',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Mana Vamp', alternative='', base=''),
            helm=Slot(best='Thief', alternative='', base=''),
            cape=Slot(best='Thief', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('Classic Alpha Pirate', same_as="Rogue"),
    ClassDef('Classic Barber', same_as="Rogue"),
    ClassDef('Classic Defender', model="Tank Melee"),
    ClassDef('Classic DoomKnight', same_as="DoomKnight"),
    ClassDef('Classic Dragonlord', model="Power Melee"),
    ClassDef('Classic Exalted Soul Cleaver', model="Full Hybrid"),
    ClassDef('Classic Guardian', model="Full Hybrid"),
    ClassDef('Classic Legion DoomKnight'),
    ClassDef(
        'Classic Ninja',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Mana Vamp', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Classic Paladin', model="Full Hybrid"),
    ClassDef('Classic Pirate', same_as="Rogue"),
    ClassDef('Classic Soul Cleaver', model="Full Hybrid"),
    ClassDef('ClawSuit', model="Tank Melee"),
    ClassDef('Continuum Chronomancer', model="Full Hybrid"),
    ClassDef('Corrupted Chronomancer', same_as="Timeless Chronomancer"),
    ClassDef(
        'Cryomancer',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Cryomancer Mini Pet Coming Soon', same_as="Warrior"),
    ClassDef('Daimon', model="Offensive Caster"),
    ClassDef('Dark BattleMage', same_as="Royal BattleMage"),
    ClassDef('Dark Caster', same_as="Immortal Dark Caster"),
    ClassDef('Dark Chaos Berserker', same_as="Chaos Slayer Berserker"),
    ClassDef('Dark Cryomancer', same_as="Cryomancer"),
    ClassDef('Dark Glaceran Warlord', same_as="Glaceran Warlord"),
    ClassDef('Dark Harbinger', same_as="Soul Cleaver"),
    ClassDef('Dark Legendary Hero', model="Tank Melee"),
    ClassDef(
        'Dark Lord',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('Dark Master of Moglins', same_as="Master of Moglins"),
    ClassDef('Dark Metal Necro', same_as="Doom Metal Necro"),
    ClassDef('Dark Ultra OmniNight', same_as="Ultra OmniKnight"),
    ClassDef(
        'Darkblood StormKing',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Mana Vamp', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Darkside', model="Offensive Caster"),
    ClassDef('DeathKnight', model="Tank Melee"),
    ClassDef(
        'DeathKnight Lord',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('Debris Highlord', same_as="Void Highlord"),
    ClassDef('Defender', model="Defensive Caster"),
    ClassDef(
        'Doom Metal Necro',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Penitence', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Penitence', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Penitence', alternative='', base=''),
        ),
    ),
    ClassDef('DoomKnight', model="Tank Melee"),
    ClassDef('DoomKnight OverLord'),
    ClassDef(
        'Draco Knight',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Dragon Knight', same_as="Draco Knight"),
    ClassDef(
        'Dragon of Time',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Healer', alternative='', base=''),
            weapon=Slot(best='Healer Awe Blast', alternative='', base=''),
            helm=Slot(best='Healer', alternative='', base=''),
            cape=Slot(best='Healer', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Hearty', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Dragon Shinobi', same_as="DragonSoul Shinobi"),
    ClassDef('Dragonlord', model="Power Melee"),
    ClassDef(
        'Dragonslayer',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Fighter', alternative='', base=''),
            helm=Slot(best='Fighter', alternative='', base=''),
            cape=Slot(best='Fighter', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Forge', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef(
        'Dragonslayer General',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('DragonSoul Shinobi', model="Dodge Melee"),
    ClassDef('Drakel Warlord', model="Tank Melee"),
    ClassDef('Drakkar Knight', same_as="Draco Knight"),
    ClassDef('Elemental Dracomancer', model="Offensive Caster"),
    ClassDef(
        'Empyrean Chronomancer',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Enchanted Vampire Lord', same_as="Vampire Lord"),
    ClassDef(
        'Enforcer',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Eternal Chronomancer', same_as="Empyrean Chronomancer"),
    ClassDef(
        'Eternal Inversionist',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lacerate', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Evolved ClawSuit', model="Full Hybrid"),
    ClassDef('Evolved Dark Caster', same_as="Infinite Legion Dark Caster"),
    ClassDef('Evolved Leprechaun', model="Luck Hybrid"),
    ClassDef('Evolved Pumpkin Lord', model="Power Melee"),
    ClassDef('Evolved Shaman', model="Power Caster"),
    ClassDef('Exalted Harbinger', same_as="Soul Cleaver"),
    ClassDef('Exalted Soul Cleaver', same_as="Soul Cleaver"),
    ClassDef('FireLord Summoner', same_as="Blaze Binder"),
    ClassDef('Flame Dragon Warrior', model="Tank Melee"),
    ClassDef(
        'Frost SpiritReaver',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Lacerate', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Penitence', alternative='', base=''),
        ),
    ),
    ClassDef('Frostblood Titan', same_as="Blood Titan"),
    ClassDef(
        'Frostval Barbarian',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Fighter Awe Blast', alternative='', base=''),
            helm=Slot(best='Fighter', alternative='', base=''),
            cape=Slot(best='Fighter', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Absolution', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Giftbox', model="Tank Melee"),
    ClassDef(
        'Glaceran Warlord',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef(
        'Glacial Berserker',
        model="Power Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Glacial Berserker Test', same_as="Warrior"),
    ClassDef('Glacial Warlord', same_as="Glaceran Warlord"),
    ClassDef(
        'Great Thief',
        model="Luck Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Arcana's Concerto", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Grim Necromancer', model="Offensive Caster"),
    ClassDef('Grunge Rocker', same_as="Nu Metal Necro"),
    ClassDef(
        'Guardian',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Awe Blast', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('Healer', model="Defensive Caster"),
    ClassDef('Heavy Metal Necro', same_as="Doom Metal Necro"),
    ClassDef('Heavy Metal Rockstar', same_as="Doom Metal Necro"),
    ClassDef('Heroic Naval Commander', same_as="Naval Commander"),
    ClassDef('HighSeas Commander', model="Offensive Caster"),
    ClassDef('Hobo Highlord', same_as="No Class"),
    ClassDef('Hollowborn No-Class', same_as="No Class"),
    ClassDef(
        'Hollowborn Vindicator',
        model="Defensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Penitence', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Penitence', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Penitence', alternative='', base=''),
        ),
    ),
    ClassDef('Hollowborn Vindicator Member Preview', same_as="Healer"),
    ClassDef('Horc Evader', model="Dodge Melee"),
    ClassDef('Immortal Chronomancer', same_as="Empyrean Chronomancer"),
    ClassDef(
        'Immortal Dark Caster',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Imperial Chunin', same_as="Chunin"),
    ClassDef('Infinite Dark Caster', same_as="Infinite Legion Dark Caster"),
    ClassDef(
        'Infinite Legion Dark Caster',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Smite', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Infinity Hero', model="Tank Melee"),
    ClassDef(
        'Infinity Knight',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Awe Blast', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Acheron', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Infinity Titan', model="Defensive Caster"),
    ClassDef('Interstellar Knight', model="Offensive Caster"),
    ClassDef('Kathool Adept', model="Defensive Caster"),
    ClassDef(
        "King's Echo",
        model="Power Caster",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Legendary Elemental Warrior', same_as="Ultra Elemental Warrior"),
    ClassDef(
        'Legendary Hero',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('Legendary Naval Commander', same_as="Naval Commander"),
    ClassDef('Legion BladeMaster Assassin', model="Dodge Melee"),
    ClassDef(
        'Legion DoomKnight',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Legion DoomKnight Tester', same_as="Warrior"),
    ClassDef('Legion Evolved Dark Caster', same_as="Infinite Legion Dark Caster"),
    ClassDef(
        'Legion Paladin',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('Legion Paladin Member Trial', same_as="Warrior"),
    ClassDef(
        'Legion Revenant',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Acheron', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Penitence', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Arcana's Concerto", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('Legion Revenant Member Test', same_as="Warrior"),
    ClassDef(
        'Legion SwordMaster Assassin',
        model="Dodge Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Awe Blast', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Leprechaun'),
    ClassDef(
        'Lich',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef(
        'LightCaster',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('LightCaster Test', model="Offensive Caster"),
    ClassDef('LightMage', model="Offensive Caster"),
    ClassDef(
        'Lord Of Order',
        model="Defensive Caster",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Awe Blast', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Healer', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Absolution', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Arcana's Concerto", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Absolution', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Awe Blast', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Absolution', alternative='', base=''),
        ),
    ),
    ClassDef('Love Caster', same_as="Elemental Dracomancer"),
    ClassDef(
        'Lycan',
        model="Power Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Mage', model="Offensive Caster"),
    ClassDef(
        'Martial Artist',
        model="Dodge Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Master Martial Artist', same_as="Martial Artist"),
    ClassDef(
        'Master of Moglins',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef(
        'Master Ranger',
        model="Dodge Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Health Vamp', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Health Vamp', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
    ),
    ClassDef(
        'MechaJouster',
        model="Power Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef(
        'MindBreaker',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('Mystical Dark Caster', same_as="Timeless Dark Caster"),
    ClassDef('Mythic Elemental Warrior', same_as="Ultra Elemental Warrior"),
    ClassDef(
        'Naval Commander',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Nechronomancer', model="Power Melee"),
    ClassDef('Necromancer', model="Offensive Caster"),
    ClassDef(
        'Necrotic Chronomancer',
        model="Power Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Health Vamp', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Neo Metal Necro', same_as="Nu Metal Necro"),
    ClassDef(
        'Ninja',
        model="Dodge Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Ninja Warrior', model="Dodge Melee"),
    ClassDef('No Class', model="Tank Melee"),
    ClassDef(
        'Northlands Monk',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('NOT A MOD', model="Dodge Melee"),
    ClassDef('Nu Metal Necro', model="Tank Melee"),
    ClassDef('Obsidian No Class', same_as="No Class"),
    ClassDef('Obsidian Paladin Chronomancer', model="Full Hybrid"),
    ClassDef('Oracle', model="Power Caster"),
    ClassDef('Overworld Chronomancer', same_as="Timeless Chronomancer"),
    ClassDef(
        'Paladin',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef(
        'Paladin Chronomancer',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Fighter Mana Vamp', alternative='', base=''),
            helm=Slot(best='Fighter', alternative='', base=''),
            cape=Slot(best='Fighter', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Fighter Mana Vamp', alternative='', base=''),
            helm=Slot(best='Hearty', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Fighter Mana Vamp', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Absolution', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Fighter Mana Vamp', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Absolution', alternative='', base=''),
        ),
    ),
    ClassDef('Paladin Highlord', model="Full Hybrid"),
    ClassDef('PaladinSlayer', model="Full Hybrid"),
    ClassDef('Phantasm Chronomancer', model="Power Caster"),
    ClassDef(
        'Phantom Chronomancer',
        model="Power Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Acheron', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Pink Romancer', model="Offensive Caster"),
    ClassDef('Pinkomancer', model="Offensive Caster"),
    ClassDef('Pirate', model="Luck Hybrid"),
    ClassDef('Prismatic ClawSuit', model="Full Hybrid"),
    ClassDef('ProtoSartorium', model="Full Hybrid"),
    ClassDef(
        'Psionic MindBreaker',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('Pumpkin Lord', same_as="Warrior"),
    ClassDef('PvP Test - Bard'),
    ClassDef('PvP Test - Healer'),
    ClassDef('Pyromancer', model="Offensive Caster"),
    ClassDef(
        'Quantum Chronomancer',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Health Vamp', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Smite', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('Ranger', model="Dodge Melee"),
    ClassDef('Renegade', same_as="Rogue"),
    ClassDef('Rogue', model="Dodge Melee"),
    ClassDef(
        'Royal BattleMage',
        model="Power Caster",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('Royal Vampire Lord', same_as="Vampire Lord"),
    ClassDef('Rustbucket', model="Full Hybrid"),
    ClassDef('Sakura Cryomancer', same_as="Cryomancer"),
    ClassDef('Savage Glaceran Warlord', same_as="Glaceran Warlord"),
    ClassDef(
        'Scarlet Sorceress',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef(
        'Scion of Flames',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Absolution', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Absolution', alternative='', base=''),
        ),
    ),
    ClassDef(
        'Sentinel',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Shadow Dragon Shinobi', same_as="DragonSoul Shinobi"),
    ClassDef('Shadow Ripper', same_as="Doom Metal Necro"),
    ClassDef('Shadow Rocker', same_as="Nu Metal Necro"),
    ClassDef('ShadowFlame DragonLord', same_as="Dragonslayer General"),
    ClassDef(
        'ShadowScythe General',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('ShadowStalker of Time', same_as="ShadowWalker of Time"),
    ClassDef(
        'ShadowWalker of Time',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Mana Vamp', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Smite', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('ShadowWeaver of Time', same_as="ShadowWalker of Time"),
    ClassDef(
        'Shaman',
        model="Power Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Mana Vamp', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Avarice', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Silver Paladin', model="Full Hybrid"),
    ClassDef('Simple Class', same_as="No Class"),
    ClassDef('SkyCharged Grenadier', model="Tank Melee"),
    ClassDef('SkyGuard Grenadier'),
    ClassDef('Sorcerer', model="Offensive Caster"),
    ClassDef(
        'Soul Cleaver',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Sovereign of Storms', model="Offensive Caster"),
    ClassDef('Star Captain', model="Tank Melee"),
    ClassDef('StarLord', model="Dodge Melee"),
    ClassDef(
        'StoneCrusher',
        model="Defensive Caster",
        base=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best='Fighter Awe Blast', alternative='', base=''),
            helm=Slot(best='Fighter', alternative='', base=''),
            cape=Slot(best='Fighter', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Fighter', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Absolution', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Hybrid', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Absolution', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Praxis', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef(
        'SwordMaster',
        model="Dodge Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Mana Vamp', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Smite', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef(
        'SwordMaster Assassin',
        model="Dodge Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Awe Blast', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Awe Blast', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('The Collector', same_as="Vindicator Of They"),
    ClassDef('Thief of Hours', model="Dodge Melee"),
    ClassDef(
        'TimeKeeper',
        model="Dodge Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Awe Blast', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lacerate', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
    ),
    ClassDef('TimeKiller', model="Dodge Melee"),
    ClassDef(
        'Timeless Chronomancer',
        model="Full Hybrid",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Penitence', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef(
        'Timeless Dark Caster',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Wizard', alternative='', base=''),
            cape=Slot(best='Wizard', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Wizard', alternative='', base=''),
            weapon=Slot(best='Wizard Spiral Carve', alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Pneuma', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Troll Spellsmith', model="Offensive Caster"),
    ClassDef('Troubador of Love', model="Defensive Caster"),
    ClassDef('Ultra Elemental Warrior', model="Full Hybrid"),
    ClassDef(
        'Ultra OmniKnight',
        model="Offensive Caster",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Mana Vamp', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Elysium', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Examen', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Umbra', model="Tank Melee"),
    ClassDef('Unchained Rocker', same_as="Nu Metal Necro"),
    ClassDef('Unchained Rockstar', same_as="Doom Metal Necro"),
    ClassDef(
        'Undead Goat',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Mana Vamp', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Undead Leperchaun', same_as="Unlucky Leperchaun"),
    ClassDef('UndeadSlayer', model="Tank Melee"),
    ClassDef('Underworld Chronomancer', same_as="Timeless Chronomancer"),
    ClassDef('Unlucky Leperchaun', model="Luck Hybrid"),
    ClassDef('Unundead Goat', model="Tank Melee"),
    ClassDef('Vampire', same_as="Vampire Lord"),
    ClassDef('Vampire Lord', model="Full Hybrid"),
    ClassDef(
        'Verus DoomKnight',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Awe Blast', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Vindicator Of They', model="Offensive Caster"),
    ClassDef(
        'Void Highlord',
        model="Tank Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Awe Blast', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Lament', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Ravenous', alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
    ClassDef('Void Highlord Tester', same_as="Warrior"),
    ClassDef('Warlord', same_as="Warrior"),
    ClassDef('Warrior', model="Tank Melee"),
    ClassDef('WarriorScythe General', same_as="Warrior"),
    ClassDef('Witch', model="Defensive Caster"),
    ClassDef(
        'Yami no Ronin',
        model="Dodge Melee",
        base=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lucky Spiral Carve', alternative='', base=''),
            helm=Slot(best='Lucky', alternative='', base=''),
            cape=Slot(best='Lucky', alternative='', base=''),
        ),
        solo=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Lacerate', alternative='', base=''),
            helm=Slot(best='Forge', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        group=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best="Hero's Valiance", alternative='', base=''),
            helm=Slot(best='Vim', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
        special=Mode(
            cls=Slot(best='Lucky', alternative='', base=''),
            weapon=Slot(best='Dauntless', alternative='', base=''),
            helm=Slot(best='Anima', alternative='', base=''),
            cape=Slot(best='Vainglory', alternative='', base=''),
        ),
    ),
)


# ======================================================================
# Class models
# Description text for each class model, shown on the Stats page.
# ======================================================================
CLASS_MODEL_DESCRIPTIONS = {
    "Power Melee": (
        "   [b #fca5a5]STR[/b #fca5a5] [b #eac43c]★★★[/b #eac43c]"
        "\n   Attack Power [#5eff00]↑↑[#ffffff]"
        "\n   Crit Chance [#5eff00]↑↑[#ffffff]"
        
        "\n\n   [b #86efac]DEX[/b #86efac] [b #eac43c]★★☆[/b #eac43c]"
        "\n   Dodge [#5eff00]↑↑[#ffffff]"
        "\n   Haste [#5eff00]↑↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"

        "\n\n   [b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Health [#78a849]↑[#ffffff]"

        "\n\n   [b #93c5fd]INT[/b #93c5fd] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Spell Power [#5eff00]↑↑[#ffffff]"
        "\n   Magical Resistance [#78a849]↑[#ffffff]"

        "\n\n   [b #fde68a]WIS[/b #fde68a] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Dodge [#78a849]↑[#ffffff]"

        "\n\n   [b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\n   Critical Damage [#5eff00]↑↑[#ffffff]"
        "\n   Critical Chance [#78a849]↑[#ffffff]"
        "\n   Attack Power [#78a849]↑[#ffffff]"
        "\n   Dodge [#78a849]↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"
    ),
    "Dodge Melee": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★★☆[/b #eac43c]"
        "\n   Attack Power [#5eff00]↑↑[#ffffff]"
        "\n   Crit Chance [#78a849]↑[#ffffff]"
        
        "\n\n   [b #86efac]DEX[/b #86efac] [b #eac43c]★★☆[/b #eac43c]"
        "\n   Dodge [#5eff00]↑↑[#ffffff]"
        "\n   Haste [#5eff00]↑↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"

        "\n\n   [b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Health [#78a849]↑[#ffffff]"

        "\n\n   [b #93c5fd]INT[/b #93c5fd] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Spell Power [#5eff00]↑↑[#ffffff]"
        "\n   Magical Resistance [#78a849]↑[#ffffff]"

        "\n\n   [b #fde68a]WIS[/b #fde68a] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Dodge [#78a849]↑[#ffffff]"

        "\n\n   [b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\n   Critical Damage [#5eff00]↑↑[#ffffff]"
        "\n   Critical Chance [#78a849]↑[#ffffff]"
        "\n   Attack Power [#78a849]↑[#ffffff]"
        "\n   Dodge [#78a849]↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"
    ),
    "Tank Melee": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★★☆[/b #eac43c]"
        "\n   Attack Power [#5eff00]↑↑[#ffffff]"
        "\n   Crit Chance [#78a849]↑[#ffffff]"
        
        "\n\n   [b #86efac]DEX[/b #86efac] [b #eac43c]★★☆[/b #eac43c]"
        "\n   Dodge [#78a849]↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"

        "\n\n   [b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Health [#78a849]↑[#ffffff]"

        "\n\n   [b #93c5fd]INT[/b #93c5fd] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Spell Power [#5eff00]↑↑[#ffffff]"
        "\n   Magical Resistance [#78a849]↑[#ffffff]"

        "\n\n   [b #fde68a]WIS[/b #fde68a] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Dodge [#78a849]↑[#ffffff]"

        "\n\n   [b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\n   Critical Damage [#5eff00]↑↑[#ffffff]"
        "\n   Critical Chance [#78a849]↑[#ffffff]"
        "\n   Attack Power [#78a849]↑[#ffffff]"
        "\n   Dodge [#78a849]↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"
    ),
    "Power Caster": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Attack Power [#5eff00]↑↑[#ffffff]"
        
        "\n\n   [b #86efac]DEX[/b #86efac] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Dodge [#78a849]↑[#ffffff]"

        "\n\n   [b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Health [#78a849]↑[#ffffff]"

        "\n\n   [b #93c5fd]INT[/b #93c5fd] [b #eac43c]★★★[/b #eac43c]"
        "\n   Spell Power [#5eff00]↑↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Magical Boost [#78a849]↑[#ffffff]"
        "\n   Magical Resistance [#78a849]↑[#ffffff]"

        "\n\n   [b #fde68a]WIS[/b #fde68a] [b #eac43c]★★☆[/b #eac43c]"
        "\n   Dodge [#78a849]↑[#ffffff]"
        "\n   Crit Chance [#78a849]↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"

        "\n\n   [b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\n   Critical Damage [#5eff00]↑↑[#ffffff]"
        "\n   Critical Chance [#78a849]↑[#ffffff]"
        "\n   Spell Power [#78a849]↑[#ffffff]"
        "\n   Dodge [#78a849]↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"
    ),
    "Offensive Caster": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Attack Power [#5eff00]↑↑[#ffffff]"
        
        "\n\n   [b #86efac]DEX[/b #86efac] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Dodge [#78a849]↑[#ffffff]"

        "\n\n   [b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Health [#78a849]↑[#ffffff]"

        "\n\n   [b #93c5fd]INT[/b #93c5fd] [b #eac43c]★★★[/b #eac43c]"
        "\n   Spell Power [#5eff00]↑↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Magical Boost [#78a849]↑[#ffffff]"
        "\n   Magical Resistance [#78a849]↑[#ffffff]"

        "\n\n   [b #fde68a]WIS[/b #fde68a] [b #eac43c]★★☆[/b #eac43c]"
        "\n   Dodge [#78a849]↑[#ffffff]"
        "\n   Crit Chance [#5eff00]↑↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"

        "\n\n   [b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\n   Critical Damage [#5eff00]↑↑[#ffffff]"
        "\n   Critical Chance [#78a849]↑[#ffffff]"
        "\n   Spell Power [#78a849]↑[#ffffff]"
        "\n   Dodge [#78a849]↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"
    ),
    "Defensive Caster": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Attack Power [#5eff00]↑↑[#ffffff]"
        
        "\n\n   [b #86efac]DEX[/b #86efac] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Dodge [#78a849]↑[#ffffff]"

        "\n\n   [b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Health [#78a849]↑[#ffffff]"

        "\n\n   [b #93c5fd]INT[/b #93c5fd] [b #eac43c]★★★[/b #eac43c]"
        "\n   Spell Power [#78a849]↑↑[#ffffff]"
        "\n   Haste [#5eff00]↑↑[#ffffff]"
        "\n   Magical Boost [#78a849]↑[#ffffff]"
        "\n   Magical Resistance [#78a849]↑[#ffffff]"

        "\n\n   [b #fde68a]WIS[/b #fde68a] [b #eac43c]★★☆[/b #eac43c]"
        "\n   Dodge [#78a849]↑[#ffffff]"
        "\n   Crit Chance [#78a849]↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"

        "\n\n   [b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\n   Critical Damage [#5eff00]↑↑[#ffffff]"
        "\n   Critical Chance [#78a849]↑[#ffffff]"
        "\n   Spell Power [#78a849]↑[#ffffff]"
        "\n   Dodge [#78a849]↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"
    ),
    "Full Hybrid": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★★☆[/b #eac43c]"
        "\n   Attack Power [#5eff00]↑↑[#ffffff]"
        "\n   Crit Chance [#78a849]↑[#ffffff]"
        
        "\n\n   [b #86efac]DEX[/b #86efac] [b #eac43c]★★☆[/b #eac43c]"
        "\n   Dodge [#5eff00]↑↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"

        "\n\n   [b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Health [#78a849]↑[#ffffff]"

        "\n\n   [b #93c5fd]INT[/b #93c5fd] [b #eac43c]★★☆[/b #eac43c]"
        "\n   Spell Power [#5eff00]↑↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Magical Boost [#78a849]↑[#ffffff]"
        "\n   Magical Resistance [#78a849]↑[#ffffff]"

        "\n\n   [b #fde68a]WIS[/b #fde68a] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Dodge [#78a849]↑[#ffffff]"

        "\n\n   [b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\n   Critical Damage [#5eff00]↑↑[#ffffff]"
        "\n   Critical Chance [#78a849]↑[#ffffff]"
        "\n   Attack Power [#78a849]↑[#ffffff]"
        "\n   Spell Power [#78a849]↑[#ffffff]"
        "\n   Dodge [#78a849]↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"
    ),
    "Luck Hybrid": (
        "[b #fca5a5]STR[/b #fca5a5] [b #eac43c]★★☆[/b #eac43c]"
        "\n   Attack Power [#78a849]↑[#ffffff]"
        "\n   Crit Chance [#78a849]↑[#ffffff]"
        
        "\n\n   [b #86efac]DEX[/b #86efac] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Dodge [#78a849]↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"

        "\n\n   [b #e9a8f4]END[/b #e9a8f4] [b #eac43c]★☆☆[/b #eac43c]"
        "\n   Health [#78a849]↑[#ffffff]"

        "\n\n   [b #93c5fd]INT[/b #93c5fd] [b #eac43c]★★☆[/b #eac43c]"
        "\n   Spell Power [#78a849]↑[#ffffff]"
        "\n   Haste [#78a849]↑[#ffffff]"
        "\n   Magical Boost [#78a849]↑[#ffffff]"
        "\n   Magical Resistance [#78a849]↑[#ffffff]"

        "\n\n   [b #fde68a]WIS[/b #fde68a] [b #eac43c]★★★[/b #eac43c]"
        "\n   Dodge [#78a849]↑[#ffffff]"
        "\n   Crit Chance [#78a849]↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"

        "\n\n   [b #f7b176]LUK[/b #f7b176] [b #eac43c]★★★[/b #eac43c]"
        "\n   Critical Damage [#78a849]↑[#ffffff]"
        "\n   Critical Chance [#5eff00]↑↑[#ffffff]"
        "\n   Attack Power [#5eff00]↑↑[#ffffff]"
        "\n   Spell Power [#5eff00]↑↑[#ffffff]"
        "\n   Dodge [#5eff00]↑↑[#ffffff]"
        "\n   Haste [#5eff00]↑↑[#ffffff]"
        "\n   Hit Chance [#78a849]↑[#ffffff]"
    ),
}

# Replace Unicode stars with platform-appropriate characters on Windows
if _FILLED_STAR != "★":
    CLASS_MODEL_DESCRIPTIONS = {
        key: value.replace("★", _FILLED_STAR).replace("☆", _HOLLOW_STAR)
        for key, value in CLASS_MODEL_DESCRIPTIONS.items()
    }
