import discord
from discord.ext import bridge, commands
from chef_bot.api import get_nutrients


class Nutrition(commands.Cog):
    def __init__(self, bot: bridge.Bot):
        self.bot = bot

    @bridge.bridge_command()
    async def nutrition(self, ctx: bridge.BridgeContext, food: str):
        """Find the nutrients for food.

        ex. `!nutrition banana`,
        for a multiple word type `!nutrition "white sauce pasta"`
        """
        # Add `defer` to add `bot is thinking msg` for long running tasks.
        await ctx.defer()
        nutrients = get_nutrients(food)

        title = f"No results found for {food}"
        embed = discord.Embed(title=title, color=discord.Color.og_blurple())
        if foods := nutrients.get("foods"):
            nutrient = foods[0]
            embed.title = f"You searched for food {food}."
            embed.description = f"Nutrients result found **{nutrient['food_name']}**. {nutrient['serving_qty']} serving per {nutrient['serving_unit']}."
            if (
                nutrient["photo"]
                and (
                    image_url := nutrient["photo"].get("highres")
                    or nutrient["photo"].get("thumb")
                )
                and image_url
                != "https://d2eawub7utcl6.cloudfront.net/images/nix-apple-grey.png"
            ):
                embed = embed.set_image(url=image_url)

            respone_keys = {
                "serving_weight_grams": {"title": "Service weight", "unit": "gm"},
                "nf_calories": {"title": "Calories", "unit": "kcal"},
                "nf_total_fat": {"title": "Total Fat", "unit": "gm"},
                "nf_saturated_fat": {"title": "Saturated Fat", "unit": "gm"},
                "nf_cholesterol": {"title": "Cholesterol", "unit": "mg"},
                "nf_total_carbohydrate": {"title": "Total Carbohydrate", "unit": "gm"},
                "nf_dietary_fiber": {"title": "Dietary Fiber", "unit": "gm"},
                "nf_sugars": {"title": "Sugars", "unit": "gm"},
                "nf_protein": {"title": "Protein", "unit": "gm"},
                "nf_sodium": {"title": "Sodium", "unit": "mg"},
                "nf_potassium": {"title": "Potassium", "unit": "mg"},
            }

            for key in respone_keys.keys():
                embed = embed.add_field(
                    name=respone_keys[key]["title"],
                    value=f"{nutrient[key]} ({respone_keys[key]['unit']})",
                )
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Nutrition(bot))
