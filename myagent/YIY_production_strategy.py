from negmas import Contract
from scml import NO_COMMAND
from scml.scml2020.components.production import ProductionStrategy

from typing import List
import numpy as np


class YIYProductionStrategy(ProductionStrategy):
    def is_supply(self):
        product_in_price = self.awi.catalog_prices[self.awi.my_input_product]
        product_out_price = self.awi.catalog_prices[self.awi.my_output_product]
        production_cost = np.max(self.awi.profile.costs[:, self.awi.my_input_product])
        if product_out_price / 2 > product_in_price / 2 + production_cost:
            return True
        return False

    def on_contracts_finalized(self, signed: List[Contract], cancelled: List[Contract],
                               rejectors: List[List[str]]):
        super().on_contracts_finalized(signed, cancelled, rejectors)
        for signed_contract in signed:
            is_seller = signed_contract.annotation["seller"] == self.id
            step = signed_contract.agreement["time"]
            earliest_production = self.awi.current_step
            latest = self.awi.n_steps - 2

            if self.is_supply():
                if is_seller:
                    continue
                # find the earliest time I can do anything about this contract
                if step > latest + 1 or step < earliest_production:
                    continue

                input_product = signed_contract.annotation["product"]

            else:
                if not is_seller:
                    continue
                if step > self.awi.n_steps - 1 or step < earliest_production:
                    continue

                output_product = signed_contract.annotation["product"]
                input_product = output_product - 1

            steps, _ = self.awi.schedule_production(
                process=input_product,
                repeats=signed_contract.agreement["quantity"],
                step=(earliest_production, step - 1),
                line=-1,
                partial_ok=True,
            )

            self.set_schedule_range(is_seller, signed_contract, steps)

    def set_schedule_range(self, is_seller, signed_contract, steps):
        self.schedule_range[signed_contract.id] = (
            min(steps) if len(steps) > 0 else -1,
            max(steps) if len(steps) > 0 else -1,
            is_seller,
        )

    def step(self):
        super().step()
        commands = NO_COMMAND * np.ones(self.awi.n_lines, dtype=int)
        inputs = min(self.awi.state.inventory[self.awi.my_input_product], len(commands))
        commands[:inputs] = self.awi.my_input_product
        commands[inputs:] = NO_COMMAND
        self.awi.set_commands(commands)