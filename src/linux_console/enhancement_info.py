# Shared enhancement descriptions, as plain text keyed by name.


ENHANCEMENT_INFO: dict[str, str] = {
    "Forge": (
        "+(12~38) STR\n"
        "+(12~38) INT\n"
        "+(23~76) LUK\n"
        "Generic, safe helm. One step up from base Lucky Helm"
    ),
    "Vim": (
        "+(11~15)   STR\n"
        "+(137~198) DEX\n"
        "+(53~76)   LUK\n"
        "-(94~137)  END\n"
        "Mana Cost Reduction +33%\n"
        "Great for Dodge and Haste on Melee and Hybrid classes"
    ),
    "Examen": (
        "+(11~15)    INT\n"
        "+(137~198)  WIS\n"
        "+(53~76)    LUK\n"
        "-(94~137)   END\n"
        "Mana Cost Reduction +33%\n"
        "Great for Dodge and Crit Chance on Caster and Lucky Hybrid classes"
    ),
    "Anima": (
        "+(141~204) STR\n"
        "+(17~24)   INT\n"
        "+(25~36)   DEX\n"
        "+(17~24)   WIS\n"
        "-(94~136)  END\n"
        "+10% Hit Chance\n"
        "Great for raw Attack Power and Crit Chance for Melees and Full Hybrids"
    ),
    "Pneuma": (
        "+(25~37)   STR\n"
        "+(124~179) INT\n"
        "+(25~36)   DEX\n"
        "+(25~36)   WIS\n"
        "-(94~136)  END\n"
        "+10% Hit Chance\n"
        "Great for raw Spell Power and Haste for Casters and Full Hybrids"
    ),
    "Hearty": (
        "-(14~17)   STR\n"
        "-(14~18)   INT\n"
        "-(14~18)   DEX\n"
        "-(14~18)   WIS\n"
        "-(14~18)   LUK\n"
        "+(190~241) END\n"
        "Paladin Chronomancer"
    ),
    "Absolution": (
        "+(27~30)  STR\n"
        "+(27~30)  INT\n"
        "+(55~61)  LUK\n"
        "+50% Healing done\n"
        "-20% Physical Damage"
    ),
    "Vainglory": (
        "+(27~30)  STR\n"
        "+(27~30)  INT\n"
        "+(55~61)  LUK\n"
        "+15% Damage Boost\n"
        "-50% Healing received"
    ),
    "Avarice": (
        "+(27~30)  STR\n"
        "+(27~30)  INT\n"
        "+(55~61)  LUK\n"
        "+10% Haste\n"
        "-35% Damage Resistance"
    ),
    "Penitence": (
        "+(27~30)  STR\n"
        "+(27~30)  INT\n"
        "+(55~61)  LUK\n"
        "+25% Damage Resistance\n"
        "-25% Damage over Time dealt"
    ),
    "Lament": (
        "+(27~30)  STR\n"
        "+(27~30)  INT\n"
        "+(55~61)  LUK\n"
        "+20% Crit Chance\n"
        "-5% Haste"
    ),
    "Lacerate": (
        "+(20~50)  STR\n"
        "+(20~50)  INT\n"
        "+(40~100) LUK\n"
        "\n"
        "Applies on [Skill 2]\n"
        "2s Cooldown\n"
        "\n"
        "Applies Lacerate to target for 15s:\n"
        "-10% Dodge\n"
        "-10% Hit Chance\n"
        "-10% Haste\n"
        "\n"
        "Always hits and crits\n"
        "80% Attack Power\n"
        "Deals physical damage\n"
        "\n"
        "Maximum of 1 target"
    ),
    "Smite": (
        "+(30~50)  STR\n"
        "+(30~50)  INT\n"
        "+(60~100) LUK\n"
        "\n"
        "Applies on [Skill 5]\n"
        "15s Cooldown\n"
        "\n"
        "500% Attack and Spell Power\n"
        "Deals physical damage\n"
        "\n"
        "Maximum of 1 target"
    ),
    "Praxis": (
        "+(30~50)  STR\n"
        "+(30~50)  INT\n"
        "+(60~100) LUK\n"
        "\n"
        "Applies on [Skill 2]\n"
        "4s Cooldown\n"
        "\n"
        "Applies Spinning Dragon to the target for 2s:\n"
        "The next hit deals 0 damage\n"
        "\n"
        "Applies Praxis to the target for 8s:\n"
        "-5% Dodge\n"
        "Prevents Spinning Dragon\n"
        "\n"
        "70% +10% Per Praxis stack Attack and Spell Power\n"
        "Deals physical damage\n"
        "\n"
        "Maximum of 1 target"
    ),
    "Acheron": (
        "+(80~100) INT\n"
        "+(80~100) LUK\n"
        "\n"
        "Applies on [Skill 3]\n"
        "No cooldown\n"
        "\n"
        "Applies Stygian to the user for 6s:\n"
        "Receives a stacking Max Health DoT\n"
        "+30% Damage Boost\n"
        "+30% Hit Chance\n"
        "\n"
        "Always hits and crits\n"
        "80% Spell Power\n"
        "Deals magical damage\n"
        "\n"
        "Maximum of 2 targets\n"
        "Gains a stack for every target hit"
    ),
    "Hero's Valiance": (
        "+50  STR\n"
        "+50  INT\n"
        "+100 LUK\n"
        "\n"
        "Applies on Basic Attack\n"
        "10s Cooldown\n"
        "\n"
        "Applies Valiance to the user for 20s:\n"
        "+30% STR\n"
        "+30% INT\n"
        "+30% DEX\n"
        "+30% WIS\n"
        "+30% END\n"
        "+15% LUK\n"
        "\n"
        "Always hits and deals no damage"
    ),
    "Elysium": (
        "+100 INT\n"
        "+40  WIS\n"
        "+20  END\n"
        "+40  LUK\n"
        "\n"
        "Applies on [Skill 3]\n"
        "No Cooldown\n"
        "\n"
        "Applies Elysian to the user for 8s:\n"
        "Receives a stacking HoT (max 3)\n"
        "+10% Damage Boost\n"
        "Recover 4 mana per second\n"
        "\n"
        "Always hits and never crits\n"
        "500~2250% Attack Power (based on missing mana)\n"
        "Deals magical damage\n"
        "\n"
        "Maximum of 2 targets"
    ),
    "Arcana's Concerto": (
        "+50  STR\n"
        "+50  INT\n"
        "+100 LUK\n"
        "\n"
        "Applies on Basic Attack\n"
        "No Cooldown\n"
        "50% Chance of applying\n"
        "\n"
        "Applies Arcana's Concerto to the target for 22s:\n"
        "-2% Physical Resistance\n"
        "-2% Magical Resistance\n"
        "Maximum of 11 stacks\n"
        "\n"
        "50% Attack and Spell Power\n"
        "Deals physical damage\n"
        "\n"
        "Maximum of 2 targets"
    ),
    "Dauntless": (
        "+88  STR\n"
        "+26  DEX\n"
        "+86  END\n"
        "\n"
        "Applies on [Skill 2]\n"
        "3s Cooldown\n"
        "\n"
        "Applies Dauntless to the user for 12s:\n"
        "+15% Crit Chance\n"
        "+25% Haste\n"
        "+50% Mana Cost Reduction\n"
        "\n"
        "Applies Decay to the user for 6s:\n"
        "Cannot Heal outside of Life Steal\n"
        "\n"
        "Life Steals for 10% Attack Power on activation\n"
        "\n"
        "Always hits and crits\n"
        "190~570% Attack Power (based on missing health)\n"
        "Deals physical damage\n"
        "\n"
        "Maximum of 1 target"
    ),
    "Ravenous": (
        "+50  STR\n"
        "+50  INT\n"
        "+100 LUK\n"
        "\n"
        "Applies on [Skill 3]\n"
        "No Cooldown\n"
        "\n"
        "Applies Ravenous to the user for 10s:\n"
        "+10% Damage Boost\n"
        "+25% Crit Chance\n"
        "\n"
        "Applies Consumed to the target for 10s:\n"
        "-10% -1% per stack Damage Boost (up 30)\n"
        "-10% -1% per stack Crit Chance (up 30)\n"
        "\n"
        "Always crits\n"
        "75~338% Attack and Spell Power\n"
        "Damage based on the target's missing health\n"
        "Deals physical damage\n"
        "\n"
        "Maximum of 1 target"
    ),
}


DEFAULT_INFO: dict[str, str] = {
    "Fighter": (
        "High Health and Attack Power\n"
        "Does not offer many benefits\n"
        "Best for classes that deal Health damage\n"
    ),
    "Wizard": (
        "High Haste and Spell Power\n"
        "Gives some Critical Damage\n"
        "Great enhancement for Spell Power classes\n"
    ),
    "Healer": (
        "High Health and some Spell Power\n"
        "Terrible in every case\n"
    ),
    "Thief": (
        "Some Health and Attack Power\n"
        "Does give decent Haste and Dodge\n"
        "However it is never good\n"
    ),
    "Hybrid": (
        "Thief with INT\n"
        "It is almost never used\n"
        "Common on StoneCrusher class\n"
    ),
    "Spellbreaker": (
        "Healer tried to be Wizard and failed\n"
        "It sacrifices too much for WIS\n"
        "Not good enough to be used\n"
    ),
    "Lucky": (
        "Overall best enhancement\n"
        "LUK is great in almost every case\n"
        "Unless your class doesn't crit\n"
    ),
}


ADDON_INFO: dict[str, str] = {
    "Awe Blast": (
        "Applies on Basic Attack\n"
        "No Cooldown\n"
        "30% Chance of applying\n"
        "\n"
        "Applies Awe Blast to the target for 10s:\n"
        "-15% Crit Chance\n"
        "-10% Hit Chance\n"
        "-15% Damage Resistance\n"
        "\n"
        "100% Attack and Spell Power\n"
        "Deals physical damage\n"
        "\n"
        "Maximum of 2 targets"
    ),
    "Spiral Carve": (
        "Applies on Basic Attack\n"
        "No Cooldown\n"
        "15% Chance of applying\n"
        "\n"
        "Applies Spiral Carve to the user for 10s:\n"
        "+25% Crit Chance\n"
        "\n"
        "200% Attack and Spell Power\n"
        "Deals physical damage\n"
        "\n"
        "Maximum of 2 targets"
    ),
    "Mana Vamp": (
        "Applies on Basic Attack\n"
        "No Cooldown\n"
        "80% Chance of applying\n"
        "\n"
        "Recovers 10 mana\n"
        "\n"
        "50% Attack and Spell Power\n"
        "Deals true damage\n"
        "\n"
        "Maximum of 2 targets"
    ),
    "Health Vamp": (
        "Applies on Basic Attack\n"
        "No Cooldown\n"
        "50% Chance of applying\n"
        "\n"
        "Life Steals for 10% Attack Power\n"
        "\n"
        "80% Attack and Spell Power\n"
        "Deals true damage\n"
        "\n"
        "Maximum of 2 targets"
    ),
    "Powerword DIE": (
        "Applies on Basic Attack\n"
        "No Cooldown\n"
        "0.3% Chance of applying\n"
        "\n"
        "Deals 999999 true damage\n"
        "Maximum of 2 targets (?)"
    ),
}
