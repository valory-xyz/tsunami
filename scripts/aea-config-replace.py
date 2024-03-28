#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2024 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------


"""Updates fetched agent with correct config"""
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv


def main() -> None:
    """Main"""
    load_dotenv()

    with open(Path("tsunami", "aea-config.yaml"), "r", encoding="utf-8") as file:
        config = list(yaml.safe_load_all(file))

        config[1]["config"][
            "farcaster_mnemonic"
        ] = f"${{str:{os.getenv('FARCASTER_MNEMONIC')}}}"

        config[5]["config"]["ledger_apis"]["ethereum"][
            "address"
        ] = f"${{str:{os.getenv('ETHEREUM_LEDGER_RPC')}}}"
        config[5]["config"]["ledger_apis"]["gnosis"][
            "address"
        ] = f"${{str:{os.getenv('GNOSIS_LEDGER_RPC')}}}"

        config[7]["models"]["params"]["args"][
            "twitter_credentials"
        ] = f"${{str:{os.getenv('TWITTER_CREDENTIALS')}}}"

        config[7]["models"]["params"]["args"][
            "initial_block_ethereum"
        ] = f"${{int:{int(os.getenv('INITIAL_BLOCK_ETHEREUM'))}}}"  # type: ignore

        config[7]["models"]["params"]["args"][
            "initial_block_gnosis"
        ] = f"${{int:{int(os.getenv('INITIAL_BLOCK_GNOSIS'))}}}"  # type: ignore

    with open(Path("tsunami", "aea-config.yaml"), "w", encoding="utf-8") as file:
        yaml.dump_all(config, file, sort_keys=False)


if __name__ == "__main__":
    main()
