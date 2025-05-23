# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under both the MIT license found in the
# LICENSE-MIT file in the root directory of this source tree and the Apache
# License, Version 2.0 found in the LICENSE-APACHE file in the root directory
# of this source tree.

# pyre-strict


from typing import List

from buck2.tests.e2e_util.api.buck import Buck
from buck2.tests.e2e_util.asserts import expect_failure
from buck2.tests.e2e_util.buck_workspace import buck_test


async def build_target_with_different_platforms_and_verify_output_paths_are_identical(
    buck: Buck,
    target: str,
    args: List[str] | None = None,
) -> None:
    if args is None:
        args = []
    result1 = await buck.build(
        target,
        "--target-platforms",
        "root//:p_default",
        "--show-output",
        *args,
    )
    result2 = await buck.build(
        target,
        "--target-platforms",
        "root//:p_cat",
        "--show-output",
        *args,
    )

    path1 = result1.get_target_to_build_output().get(target)
    path2 = result2.get_target_to_build_output().get(target)

    assert path1 is not None
    assert "output_artifact" not in path1
    assert path1 == path2


@buck_test()
async def test_write_with_content_based_path(buck: Buck) -> None:
    target = "root//:write_with_content_based_path"
    await build_target_with_different_platforms_and_verify_output_paths_are_identical(
        buck, target
    )


@buck_test()
async def test_write_macro_with_content_based_path(buck: Buck) -> None:
    target = "root//:write_macro_with_content_based_path"
    await build_target_with_different_platforms_and_verify_output_paths_are_identical(
        buck, target
    )


@buck_test()
async def test_write_json_with_content_based_path(buck: Buck) -> None:
    target = "root//:write_json_with_content_based_path"
    await build_target_with_different_platforms_and_verify_output_paths_are_identical(
        buck, target
    )


@buck_test()
async def test_run_remote_with_content_based_path(buck: Buck) -> None:
    target = "root//:run_remote_with_content_based_path"
    await build_target_with_different_platforms_and_verify_output_paths_are_identical(
        buck,
        target,
        ["--remote-only"],
    )


@buck_test()
async def test_copy_with_content_based_path(buck: Buck) -> None:
    target = "root//:copy_with_content_based_path"
    await build_target_with_different_platforms_and_verify_output_paths_are_identical(
        buck, target
    )


@buck_test()
async def test_symlink_with_content_based_path(buck: Buck) -> None:
    target = "root//:symlink_with_content_based_path"
    await build_target_with_different_platforms_and_verify_output_paths_are_identical(
        buck, target
    )


@buck_test()
async def test_copied_dir_with_content_based_path(buck: Buck) -> None:
    target = "root//:copied_dir_with_content_based_path"
    await build_target_with_different_platforms_and_verify_output_paths_are_identical(
        buck, target
    )


@buck_test()
async def test_symlinked_dir_with_content_based_path(buck: Buck) -> None:
    target = "root//:symlinked_dir_with_content_based_path"
    await build_target_with_different_platforms_and_verify_output_paths_are_identical(
        buck, target
    )


@buck_test()
async def test_cas_artifact_with_content_based_path(buck: Buck) -> None:
    await build_target_with_different_platforms_and_verify_output_paths_are_identical(
        buck, "root//:empty_cas_artifact_with_content_based_path"
    )


@buck_test()
async def test_download_with_content_based_path(buck: Buck) -> None:
    await build_target_with_different_platforms_and_verify_output_paths_are_identical(
        buck, "root//:download_with_content_based_path"
    )


@buck_test()
async def test_validation_with_content_based_path(buck: Buck) -> None:
    await expect_failure(
        buck.build(
            "root//:failing_validation_with_content_based_path",
            "--target-platforms",
            "root//:p_default",
            "--show-output",
        ),
        stderr_regex="This is a failing validation",
    )


@buck_test()
async def test_dynamic_with_content_based_path(buck: Buck) -> None:
    await build_target_with_different_platforms_and_verify_output_paths_are_identical(
        buck, "root//:dynamic_with_content_based_path"
    )


@buck_test()
async def test_dynamic_new_with_content_based_path(buck: Buck) -> None:
    await build_target_with_different_platforms_and_verify_output_paths_are_identical(
        buck, "root//:dynamic_new_with_content_based_path"
    )
