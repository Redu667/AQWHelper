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
    ClassDef('Acolyte'),
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
    ClassDef('Alpha Pirate'),
    ClassDef('Antique Hunter'),
    ClassDef(
        'Arachnomancer',
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
    ClassDef('Arcane Dark Caster'),
    ClassDef(
        'ArchFiend',
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
    ClassDef('Archivist of Temporis'),
    ClassDef(
        'Archivist of Time',
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
    ClassDef('Assassin'),
    ClassDef('Barber'),
    ClassDef(
        'Bard',
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
    ClassDef('Battle Bard'),
    ClassDef('Battle Healer'),
    ClassDef('Battle Warrior'),
    ClassDef('BattleMage'),
    ClassDef('BattleMage of Love'),
    ClassDef('Beast Warrior'),
    ClassDef('BeastMaster'),
    ClassDef(
        'Berserker',
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
    ClassDef('Beta Berserker'),
    ClassDef('BladeMaster'),
    ClassDef('BladeMaster Assassin'),
    ClassDef(
        'Blaze Binder',
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
    ClassDef('Blood Ancient'),
    ClassDef('Blood Sorceress'),
    ClassDef(
        'Blood Titan',
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
    ClassDef('Brutal Berserker'),
    ClassDef('CardClasher'),
    ClassDef(
        'Chaos Avenger',
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
    ClassDef('Chaos Avenger Member Preview'),
    ClassDef('Chaos Champion Prime'),
    ClassDef(
        'Chaos Shaper',
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
    ClassDef('Chaos Slayer Berserker'),
    ClassDef('Chaos Slayer Cleric'),
    ClassDef('Chaos Slayer Mystic'),
    ClassDef('Chaos Slayer Thief'),
    ClassDef('Chrono Assassin'),
    ClassDef(
        'Chrono Chaorruptor',
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
    ClassDef('Chrono DragonKnight'),
    ClassDef('Chrono ShadowHunter'),
    ClassDef(
        'Chrono ShadowSlayer',
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
    ClassDef('ChronoCommander'),
    ClassDef('ChronoCorruptor'),
    ClassDef(
        'Chronomancer',
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
    ClassDef('Chronomancer Prime'),
    ClassDef(
        'Chunin',
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
    ClassDef('Classic Alpha Pirate'),
    ClassDef('Classic Barber'),
    ClassDef('Classic Defender'),
    ClassDef('Classic DoomKnight'),
    ClassDef('Classic Dragonlord'),
    ClassDef('Classic Exalted Soul Cleaver'),
    ClassDef('Classic Guardian'),
    ClassDef('Classic Legion DoomKnight'),
    ClassDef(
        'Classic Ninja',
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
    ClassDef('Classic Paladin'),
    ClassDef('Classic Pirate'),
    ClassDef('Classic Soul Cleaver'),
    ClassDef('ClawSuit'),
    ClassDef('Continuum Chronomancer'),
    ClassDef('Corrupted Chronomancer'),
    ClassDef(
        'Cryomancer',
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
    ClassDef('Cryomancer Mini Pet Coming Soon'),
    ClassDef('Daimon'),
    ClassDef('Dark BattleMage'),
    ClassDef('Dark Caster'),
    ClassDef('Dark Chaos Berserker'),
    ClassDef('Dark Cryomancer'),
    ClassDef('Dark Glaceran Warlord'),
    ClassDef('Dark Harbinger'),
    ClassDef('Dark Legendary Hero'),
    ClassDef(
        'Dark Lord',
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
    ClassDef('Dark Master of Moglins'),
    ClassDef('Dark Metal Necro'),
    ClassDef('Dark Ultra OmniNight'),
    ClassDef(
        'Darkblood StormKing',
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
    ClassDef('Darkside'),
    ClassDef('DeathKnight'),
    ClassDef(
        'DeathKnight Lord',
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
    ClassDef('Debris Highlord'),
    ClassDef('Defender'),
    ClassDef(
        'Doom Metal Necro',
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
    ClassDef('DoomKnight'),
    ClassDef('DoomKnight OverLord'),
    ClassDef(
        'Draco Knight',
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
    ClassDef('Dragon Knight'),
    ClassDef(
        'Dragon of Time',
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
    ClassDef('Dragon Shinobi'),
    ClassDef('Dragonlord'),
    ClassDef(
        'Dragonslayer',
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
    ClassDef('DragonSoul Shinobi'),
    ClassDef('Drakel Warlord'),
    ClassDef('Drakkar Knight'),
    ClassDef('Elemental Dracomancer'),
    ClassDef(
        'Empyrean Chronomancer',
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
    ClassDef('Enchanted Vampire Lord'),
    ClassDef(
        'Enforcer',
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
    ClassDef('Eternal Chronomancer'),
    ClassDef(
        'Eternal Inversionist',
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
    ClassDef('Evolved ClawSuit'),
    ClassDef('Evolved Dark Caster'),
    ClassDef('Evolved Leprechaun'),
    ClassDef('Evolved Pumpkin Lord'),
    ClassDef('Evolved Shaman'),
    ClassDef('Exalted Harbinger'),
    ClassDef('Exalted Soul Cleaver'),
    ClassDef('FireLord Summoner'),
    ClassDef('Flame Dragon Warrior'),
    ClassDef(
        'Frost SpiritReaver',
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
    ClassDef('Frostblood Titan'),
    ClassDef(
        'Frostval Barbarian',
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
    ClassDef('Giftbox'),
    ClassDef(
        'Glaceran Warlord',
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
    ClassDef('Glacial Berserker Test'),
    ClassDef('Glacial Warlord'),
    ClassDef(
        'Great Thief',
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
    ClassDef('Grim Necromancer'),
    ClassDef('Grunge Rocker'),
    ClassDef(
        'Guardian',
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
    ClassDef('Healer'),
    ClassDef('Heavy Metal Necro'),
    ClassDef('Heavy Metal Rockstar'),
    ClassDef('Heroic Naval Commander'),
    ClassDef('HighSeas Commander'),
    ClassDef('Hobo Highlord'),
    ClassDef('Hollowborn No-Class'),
    ClassDef(
        'Hollowborn Vindicator',
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
    ClassDef('Hollowborn Vindicator Member Preview'),
    ClassDef('Horc Evader'),
    ClassDef('Immortal Chronomancer'),
    ClassDef(
        'Immortal Dark Caster',
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
    ClassDef('Imperial Chunin'),
    ClassDef('Infinite Dark Caster'),
    ClassDef(
        'Infinite Legion Dark Caster',
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
    ClassDef('Infinity Hero'),
    ClassDef(
        'Infinity Knight',
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
    ClassDef('Infinity Titan'),
    ClassDef('Interstellar Knight'),
    ClassDef('Kathool Adept'),
    ClassDef(
        "King's Echo",
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
    ClassDef('Legendary Elemental Warrior'),
    ClassDef(
        'Legendary Hero',
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
    ClassDef('Legendary Naval Commander'),
    ClassDef('Legion BladeMaster Assassin'),
    ClassDef(
        'Legion DoomKnight',
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
    ClassDef('Legion DoomKnight Tester'),
    ClassDef('Legion Evolved Dark Caster'),
    ClassDef(
        'Legion Paladin',
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
    ClassDef('Legion Paladin Member Trial'),
    ClassDef(
        'Legion Revenant',
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
    ClassDef('Legion Revenant Member Test'),
    ClassDef(
        'Legion SwordMaster Assassin',
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
    ClassDef('LightCaster Test'),
    ClassDef('LightMage'),
    ClassDef(
        'Lord Of Order',
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
    ClassDef('Love Caster'),
    ClassDef(
        'Lycan',
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
    ClassDef('Mage'),
    ClassDef(
        'Martial Artist',
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
    ClassDef('Master Martial Artist'),
    ClassDef(
        'Master of Moglins',
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
    ClassDef('Mystical Dark Caster'),
    ClassDef('Mythic Elemental Warrior'),
    ClassDef(
        'Naval Commander',
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
    ClassDef('Nechronomancer'),
    ClassDef('Necromancer'),
    ClassDef(
        'Necrotic Chronomancer',
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
    ClassDef('Neo Metal Necro'),
    ClassDef(
        'Ninja',
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
    ClassDef('Ninja Warrior'),
    ClassDef('No Class'),
    ClassDef(
        'Northlands Monk',
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
    ClassDef('NOT A MOD'),
    ClassDef('Nu Metal Necro'),
    ClassDef('Obsidian No Class'),
    ClassDef('Obsidian Paladin Chronomancer'),
    ClassDef('Oracle'),
    ClassDef('Overworld Chronomancer'),
    ClassDef(
        'Paladin',
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
    ClassDef('Paladin Highlord'),
    ClassDef('PaladinSlayer'),
    ClassDef('Phantasm Chronomancer'),
    ClassDef(
        'Phantom Chronomancer',
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
    ClassDef('Pink Romancer'),
    ClassDef('Pinkomancer'),
    ClassDef('Pirate'),
    ClassDef('Prismatic ClawSuit'),
    ClassDef('ProtoSartorium'),
    ClassDef(
        'Psionic MindBreaker',
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
    ClassDef('Pumpkin Lord'),
    ClassDef('PvP Test - Bard'),
    ClassDef('PvP Test - Healer'),
    ClassDef('Pyromancer'),
    ClassDef(
        'Quantum Chronomancer',
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
    ClassDef('Ranger'),
    ClassDef('Renegade'),
    ClassDef('Rogue'),
    ClassDef(
        'Royal BattleMage',
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
    ClassDef('Royal Vampire Lord'),
    ClassDef('Rustbucket'),
    ClassDef('Sakura Cryomancer'),
    ClassDef('Savage Glaceran Warlord'),
    ClassDef(
        'Scarlet Sorceress',
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
    ClassDef('Shadow Dragon Shinobi'),
    ClassDef('Shadow Ripper'),
    ClassDef('Shadow Rocker'),
    ClassDef('ShadowFlame DragonLord'),
    ClassDef(
        'ShadowScythe General',
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
    ClassDef('ShadowStalker of Time'),
    ClassDef(
        'ShadowWalker of Time',
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
    ClassDef('ShadowWeaver of Time'),
    ClassDef(
        'Shaman',
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
    ClassDef('Silver Paladin'),
    ClassDef('Simple Class'),
    ClassDef('SkyCharged Grenadier'),
    ClassDef('SkyGuard Grenadier'),
    ClassDef('Sorcerer'),
    ClassDef(
        'Soul Cleaver',
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
    ClassDef('Sovereign of Storms'),
    ClassDef('Star Captain'),
    ClassDef('StarLord'),
    ClassDef(
        'StoneCrusher',
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
    ClassDef('The Collector'),
    ClassDef('Thief of Hours'),
    ClassDef(
        'TimeKeeper',
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
    ClassDef('TimeKiller'),
    ClassDef(
        'Timeless Chronomancer',
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
    ClassDef('Troll Spellsmith'),
    ClassDef('Troubador of Love'),
    ClassDef('Ultra Elemental Warrior'),
    ClassDef(
        'Ultra OmniKnight',
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
    ClassDef('Umbra'),
    ClassDef('Unchained Rocker'),
    ClassDef('Unchained Rockstar'),
    ClassDef(
        'Undead Goat',
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
    ClassDef('Undead Leperchaun'),
    ClassDef('UndeadSlayer'),
    ClassDef('Underworld Chronomancer'),
    ClassDef('Unlucky Leperchaun'),
    ClassDef('Unundead Goat'),
    ClassDef('Vampire'),
    ClassDef('Vampire Lord'),
    ClassDef(
        'Verus DoomKnight',
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
    ClassDef('Vindicator Of They'),
    ClassDef(
        'Void Highlord',
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
    ClassDef('Void Highlord Tester'),
    ClassDef('Warlord'),
    ClassDef('Warrior'),
    ClassDef('WarriorScythe General'),
    ClassDef('Witch'),
    ClassDef(
        'Yami no Ronin',
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
