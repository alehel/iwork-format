# Fixtures

Sample documents from the experiments, for testing readers and writers. They are published as one zip per app release, attached to the repository's GitHub release `fixtures`, not committed: each zip holds the documents that release saved, under the paths listed here. `iwork-format-fixtures-16.0.zip` (366 documents), `iwork-format-fixtures-15.4.zip` (1,143 documents), `iwork-format-fixtures-14.5.zip` (359 documents). Built by `python3 -I fixtures/build.py`, which leaves out anything from Apple's templates or images, and anything holding a personal name except those whose comments, highlights or tracked changes name the project owner as their author. See [LICENSE.md](LICENSE.md).

1868 documents. Keynote presentations, under `keynote/`, were made with the project's test theme ([0291](../experiments/0291-test-theme.md), [0292](../experiments/0292-test-theme-reruns.md)). Documents were saved by the 15.4 apps unless their note names another release, such as 14.5. Under `release/16.0/` (and so on for later releases) is every sample a recipe can make on its own, made again with that release, Keynote with the test theme ([0473](../experiments/0473-every-scripted-sample-in-16-0.md)). Encrypted documents list their test password. A folder package's SHA-256 is taken over each of its files in path order, as the path, a zero byte and the contents.

| File | Experiment | Bytes | SHA-256 | Note |
| --- | --- | --- | --- | --- |
| `0001/empty-a.pages` | [0001: An empty document](../experiments/0001-empty-document.md) | 89,799 | `7c0028030a942e58e35e1162f9d45f1dee11790edc65e9528cf1889fc36fc899` | |
| `0001/empty-b.pages` | [0001: An empty document](../experiments/0001-empty-document.md) | 89,802 | `24f398004c8cd232b08cbb6653aec0a08ac1c9d2c967594fa7dd67133c226662` | |
| `0002/hello.pages` | [0002: One word](../experiments/0002-one-word.md) | 90,438 | `96db185563729e8d065f4825fb7763535b54571fa59d55d6eb351c7000f43349` | |
| `0002/hullo.pages` | [0002: One word](../experiments/0002-one-word.md) | 90,443 | `319eb22924d16505cdecdb4510fadf3baea7e89f6827b6d5d7c400dd53260e59` | |
| `0003/blabaer.pages` | [0003: A word that isn't ASCII](../experiments/0003-non-ascii-word.md) | 90,702 | `11f00df58346890d8895dfbcaba4fddc1613e3fb96f91e3544a1179db2e3d5d7` | |
| `0003/emoji.pages` | [0003: A word that isn't ASCII](../experiments/0003-non-ascii-word.md) | 90,401 | `e8d61308a26b35db7f8b2d9e443ac6a0e52a2ef02276aedfe00ac72916cd0c91` | |
| `0004/emoji-large.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 91,556 | `a9b6c65eb3a8592e38d90ff5de4b0312dc7f28244b76c07d8f84895ae229eedb` | |
| `0004/emoji-plain.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 90,946 | `517c01152e874a94180a021c452f1d20ce0605070af69b062745dc67019c1c1a` | |
| `0004/large.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 92,031 | `ebd5cb1027f043d344b4221b4fd4ea023a45b7989f6b12db8b318238ccc5b075` | |
| `0004/plain.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 91,041 | `6262b654a53adcf2145ead36152e0e5c97c04cc81be713896a3409fbb23f6397` | |
| `0005/one.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 90,590 | `0c8dd27d579b94cedaa7e813a1941657bd21bb24f1296369f841024e1a8c2157` | |
| `0005/three-cr.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 91,117 | `ba51715221c362b7dd1f77d39af69e785ce1274b3acfeade80731188fcc9e9de` | |
| `0005/two-cr.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 90,564 | `84814f3dcaa3bd87b9cc2f04e4a56dc1e42e1ddeda4ecafce36dd1f1ea8c967d` | |
| `0005/two-lf.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 90,565 | `bc1544ab1eee11cc1b5484a04196ca8203f879b5b90009c93e1b983f14bd52b8` | |
| `0006/heading-ui.pages` | [0006: Typing in Pages](../experiments/0006-typing-in-pages.md) | 91,286 | `d16bb40c2c6f3ac01b69d3b8f05ace790b0d518a4f145ecc4db0fcdd48987bdc` | |
| `0006/line-break-ui.pages` | [0006: Typing in Pages](../experiments/0006-typing-in-pages.md) | 90,662 | `5ed2900e7b61231f9c743f424df102ef484786779df145cf7990b5823aa8b534` | |
| `0006/return-ui.pages` | [0006: Typing in Pages](../experiments/0006-typing-in-pages.md) | 90,682 | `b37c70b46f9e2854a9303cf848a08f037cd0a1a5e2f13111dbd53e67de82a15d` | |
| `0007/bold-italic.pages` | [0007: Bold and italic](../experiments/0007-bold-and-italic.md) | 90,993 | `6e286c246f29be600ca7a133b72cf9e341166306ade5df8ac5cbbccd929fa89e` | |
| `0007/bold.pages` | [0007: Bold and italic](../experiments/0007-bold-and-italic.md) | 91,002 | `bac4991ee2be1d26521db72b1e2c91bf177759a096026b5c09b627df4b223def` | |
| `0007/italic.pages` | [0007: Bold and italic](../experiments/0007-bold-and-italic.md) | 90,965 | `4084f4329080da5b50bdde236a14757840bf2c020d1f413c795900bf9ad3083c` | |
| `0008/middle.pages` | [0008: Runs and shared styles](../experiments/0008-runs-and-shared-styles.md) | 91,290 | `a044f3cf3beea36b5303be8a659abc1ba680a0384e7798ae50c3e71e8eecbe41` | |
| `0008/two-words.pages` | [0008: Runs and shared styles](../experiments/0008-runs-and-shared-styles.md) | 91,347 | `8ed547ad9048f2019ac3926617279d67b6fc928694510e33117938fe62743713` | |
| `0008/unbold-middle.pages` | [0008: Runs and shared styles](../experiments/0008-runs-and-shared-styles.md) | 91,397 | `06bb0abe92077f452bbd7524e286d6966ab553de4d17c133c3f9b85214584e8d` | |
| `0009/capital.pages` | [0009: Autocorrection](../experiments/0009-autocorrection.md) | 90,970 | `62421e6e25c79042e81620f1f751fb23b20563995e3df0d1d25c8be03cfe699a` | |
| `0009/no-capital.pages` | [0009: Autocorrection](../experiments/0009-autocorrection.md) | 90,666 | `8a77a3ba69ae0632f2ebc7bb49b7281d1acd227e592530cc0683c4328117b897` | |
| `0010/center.pages` | [0010: Alignment](../experiments/0010-alignment.md) | 91,218 | `5fa04c6cc124ad99db5c0475740b06ceb877fd7ac999601e0ed1c1c4a45e5e6d` | |
| `0010/justify.pages` | [0010: Alignment](../experiments/0010-alignment.md) | 91,202 | `809e78e6156933beb2c6c7c5e7ac1479be7e5535b33c6d594be292991020eec4` | |
| `0010/right.pages` | [0010: Alignment](../experiments/0010-alignment.md) | 91,179 | `d3e876476cfc1e9443bd71eb4fa3f61d84cedade1c2e185ffb368814568facc0` | |
| `0011/center-then-left.pages` | [0011: Back to left](../experiments/0011-left-alignment.md) | 91,210 | `5a1040da21ac418cf662edb435eab8508e81cda68561c61cf476ed4be2246bbb` | |
| `0012/strikethrough.pages` | [0012: Underline and strikethrough](../experiments/0012-underline-and-strikethrough.md) | 91,216 | `82800f9a7ae107fbabebea613f9a37608ba97559a843934d20fa04650997a8f1` | |
| `0012/underline.pages` | [0012: Underline and strikethrough](../experiments/0012-underline-and-strikethrough.md) | 91,245 | `e4a020bc93cc5bc727a1ce1570c439086e129b34823f18f691742f5ca4ed3ffb` | |
| `0013/blue.pages` | [0013: Text colour](../experiments/0013-text-colour.md) | 91,370 | `6db71f8c75cc4c0833f26b9488c9e982b3aac91488ed1238c98e99f62f3ed97a` | |
| `0013/mixed.pages` | [0013: Text colour](../experiments/0013-text-colour.md) | 91,295 | `c10aa3f29d6fa1f04b6e09fde66c8e654d590e62a21262fae106e5a5d751a510` | |
| `0013/red.pages` | [0013: Text colour](../experiments/0013-text-colour.md) | 91,349 | `7b746bf322df8385367d7245fa1b1d52fcc6874bd2e17aba5cf94646f4298e99` | |
| `0014/dash-list.pages` | [0014: Lists](../experiments/0014-lists.md) | 91,627 | `54f31a3f97489b075cba0c55ce65d13f4f8471e7dbf38f07bc4838869c520ddd` | |
| `0014/numbered-list.pages` | [0014: Lists](../experiments/0014-lists.md) | 91,874 | `f4fef0162b49f9646f3340104da372164c634873f9f0c718785e9058d0393a5b` | |
| `0015/nested-list.pages` | [0015: List levels](../experiments/0015-list-levels.md) | 91,508 | `d9a5f544cc549c2222849ac8a08b5c061692e2a539ed5ec94a09bb893433cf0b` | |
| `0016/header.pages` | [0016: Header and footer](../experiments/0016-header-and-footer.md) | 91,781 | `f8da4c1f31563dca499dcd6a38754c39f75e84483c33b338197b56c2e37ff3fe` | |
| `0017/facing-pages.pages` | [0017: Section switches](../experiments/0017-section-switches.md) | 90,468 | `79f0b34066862da2b0591a0ba380d563183b5c979f63f9e6ec09a22934e1143d` | |
| `0017/hide-first.pages` | [0017: Section switches](../experiments/0017-section-switches.md) | 90,461 | `f576c12afe5a7d2676287a6e48ded9fe3704cb2d0947a46aa363d95d0021c5af` | |
| `0017/not-same-as-previous.pages` | [0017: Section switches](../experiments/0017-section-switches.md) | 90,462 | `3aca49ce1b6aaf5f45770ab968b9772496c4002034d2c56cf26f4d0fad877227` | |
| `0018/left-page-header.pages` | [0018: A page break and a left-page header](../experiments/0018-page-break-and-left-page.md) | 91,013 | `2668c87987342d6921d44d3916c13d47ee96fd74a0ff77fe16568a2735222ecd` | |
| `0019/left-right.pages` | [0019: Left and right pages](../experiments/0019-left-and-right-pages.md) | 91,358 | `84006b7f5a65341814d7059bcb187e097fbf9f6fae51a40e4ea01ace1df76e16` | |
| `0020/plain.pages` | [0020: A table](../experiments/0020-a-table.md) | 90,294 | `df4b593b34cff0cd22273bb3b75dd3c3a633b1f46359b2f030293b4bf4b1be0d` | |
| `0020/table.pages` | [0020: A table](../experiments/0020-a-table.md) | 109,537 | `35c583b3f068e769ad9ab06a3f720322fa37add9fd65ee31e975d0b983f9a4a0` | |
| `0021/cells.pages` | [0021: Table cells](../experiments/0021-table-cells.md) | 110,381 | `3668d809bf8832a31b859febda1a7cb77f9ba1f45279b6764dd090d70de02752` | |
| `0023/image.pages` | [0023: An image](../experiments/0023-an-image.md) | 91,240 | `8276979523a753a81dbe06c6e792abe0f549bad808593d5967cf7370e43f6b7a` | |
| `0023/plain.pages` | [0023: An image](../experiments/0023-an-image.md) | 90,295 | `2c60c3f35a3e6043815d942c3bd28f4a6e53b88c743e8bc500b44a5df33d2ea5` | |
| `0024/empty-a.numbers` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 136,901 | `3c2c6955b986c561649b6319319b21d7b9a5f1872fb3c4972f360eb0f47b645a` | |
| `0024/empty-b.numbers` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 136,901 | `f34aa6faa1ca25b0f1546ae708cc2d7339fadcd699d12c3f2233673beaf8be1d` | |
| `0026/cells.numbers` | [0026: Cells in Numbers](../experiments/0026-numbers-cells.md) | 137,554 | `8d91d4350e2188a540475b49b8f1a17140f20d2edce54a2fc37436dc3168fb54` | |
| `0026/empty.numbers` | [0026: Cells in Numbers](../experiments/0026-numbers-cells.md) | 136,901 | `3c2c6955b986c561649b6319319b21d7b9a5f1872fb3c4972f360eb0f47b645a` | |
| `0028/margins.pages` | [0028: Margins](../experiments/0028-margins.md) | 90,177 | `453e53b90b37dd41023d7e3a8e219a435bf10937853eb873c1f712182ebb37f7` | |
| `0030/row-300.numbers` | [0030: A second tile](../experiments/0030-tiles.md) | 170,385 | `d9e1aa9ced13dd95575f320068647b428c8fef41b9bb5508bcde252f3aedb26e` | |
| `0031/kinds.numbers` | [0031: Kinds of cell](../experiments/0031-cell-kinds.md) | 140,344 | `210c030fea871ee90dabd9a49c30461927f5244a89e3cd56d28fc9daea5913ce` | |
| `0034/mixed.pages` | [0034: Mixed paragraph styles](../experiments/0034-mixed-paragraph-styles.md) | 92,219 | `21bd97c9d046d0d10408656144da4ed6f5b317e81fe3ceadc98267da473c5d7e` | |
| `0035/formulas.numbers` | [0035: Cell references in formulas](../experiments/0035-formula-references.md) | 139,009 | `c2524d43edc3011ed57aa168b8fc446fb829e04d5775acd6bd5369971210a191` | |
| `0036/formats.numbers` | [0036: More cell formats](../experiments/0036-more-cell-formats.md) | 140,093 | `4a5b5a9b878da0dd896460f709162467287af1e5c76866a429c97f717e2d5f50` | |
| `0037/two-sheets.numbers` | [0037: A second sheet](../experiments/0037-second-sheet.md) | 145,624 | `6097ec4360217b5858be9265c95c434b4cd06c8b0e93a2d387b45a8b762728c9` | |
| `0040/section-break.pages` | [0040: A section break](../experiments/0040-section-break.md) | 91,326 | `934b337317c00731d3b6f6c0084c87a37223ebfb6e5b10e19e3127c385788008` | |
| `0041/footnote.pages` | [0041: A footnote](../experiments/0041-footnote.md) | 91,544 | `0ba243a9fa8cda7d9a681b4877c64d2e0efed1579e6f645162652d0536d162bf` | |
| `0043/styles.numbers` | [0043: Cell styles](../experiments/0043-cell-styles.md) | 140,026 | `b39d1a189e492ad89d612925030e408d60cf2ebdd151073aaedbf338d620a1f1` | |
| `0044/merged.numbers` | [0044: Merged cells](../experiments/0044-merged-cells.md) | 137,614 | `3cbb3e1a2c668655b7355a22ef1e1d67ef7ac40d4c67d4afe0e90323601f4a85` | |
| `0045/sizes.numbers` | [0045: Row and column sizes](../experiments/0045-row-and-column-sizes.md) | 135,040 | `d41c756a8fc71b9b1133607c781001eb3365d4689c75704b4e76250c0cf8ee78` | |
| `0047/two-tables.numbers` | [0047: A second table on a sheet](../experiments/0047-second-table.md) | 144,736 | `8caa08fca4b142998db4ca34c9791a7c09c0818aba72592bb5cc63bc3fb1af12` | |
| `0048/page-number.pages` | [0048: A page number field](../experiments/0048-page-number.md) | 90,756 | `8f4a98ae31e23af1758c6c29e9a7e461d7089158dade032145f83240ad3e35a2` | |
| `0049/text-box.pages` | [0049: A text box](../experiments/0049-text-box.md) | 91,269 | `95c51f646f50ce78a409199397d74727297afdeb122c5ffed0be0d92c49f7112` | |
| `0050/shape.pages` | [0050: A shape](../experiments/0050-shape.md) | 93,294 | `073c599f9de705c842d8f51311329a192d1e81f5fe307cf90eba39cb3892d1f9` | |
| `0051/line.pages` | [0051: A line](../experiments/0051-line.md) | 93,444 | `94f8045c2a8ab0d26bfab023dca69db2cf1967c699c071ff6bcd5fe482ed4ee7` | |
| `0052/table.pages` | [0052: A floating table](../experiments/0052-floating-table.md) | 104,566 | `297cce0043abee8aa4b6f6e08b2dcff563a8ca5097f818e5370429739a938f87` | |
| `0053/font.pages` | [0053: A different font](../experiments/0053-font.md) | 91,229 | `3cae827ea26e3691d80ad8e2a66314d7346f617c864af1f1c4423c07ddb146eb` | |
| `0054/sizes.pages` | [0054: Shared sizes](../experiments/0054-shared-sizes.md) | 91,875 | `d1a90ebd415e856279a52abe0ade3f9a4bdfea35d7edd8f7622281002802423f` | |
| `0055/size.pages` | [0055: Resizing an image](../experiments/0055-image-size.md) | 92,726 | `25b354dd19b41462eb62a9f92b64a36fb381c9fd87a6492aae3127446d3a4763` | |
| `0056/rotation.pages` | [0056: Rotating an image](../experiments/0056-image-rotation.md) | 91,286 | `5398666729bc92791743908c46ffc5935817ceb6394255f0d7b6ffbd33a773d3` | |
| `0057/opacity.pages` | [0057: An image's opacity](../experiments/0057-image-opacity.md) | 91,192 | `ba8d6e9a4fa020117ce69d46911deb538459e25e00159a08c0f2aabcc9a2a1b6` | |
| `0058/tab.pages` | [0058: A tab and a non-breaking space](../experiments/0058-tab-and-nbsp.md) | 90,445 | `5f3e09aac5e5c3d8d320e274463d7173933abcc379eac10cf7183c82e7ad6f7f` | |
| `0059/geometry.numbers` | [0059: A table's position and size](../experiments/0059-table-geometry.md) | 124,278 | `14d3e73a4f968fe9d7ea4662a9556f03b1ff119247315b8305cb5e9063700cca` | |
| `0060/headers.numbers` | [0060: Header and footer rows](../experiments/0060-header-rows.md) | 136,547 | `91e3222830507c393a6b4c980a9c0e650733853f08de77b856fdf6ca3e297869` | |
| `0061/center.numbers` | [0061: Centring a cell](../experiments/0061-cell-alignment.md) | 137,605 | `7efaaed22f221ce69bda14a14d6d8046b0f66413f52d81eb66fad534fa7d79bf` | |
| `0062/top-nowrap.numbers` | [0062: Text wrap in a cell](../experiments/0062-text-wrap.md) | 137,580 | `e1f92370a9a97cd50834cf74c0d004963cd5e91eb0be7ccd80c441d9cccfde5c` | |
| `0063/sparse.numbers` | [0063: Tiles for a sparse table](../experiments/0063-sparse-tiles.md) | 204,134 | `cd53931316a49664a1238736ab32705331da8fb63937712d790b432eccd5769a` | |
| `0064/functions.numbers` | [0064: Operators and functions](../experiments/0064-operators-and-functions.md) | 139,730 | `49139daabf1a6cf3e21e7fda1712969fb786b59c31a395b5c6a2d24318df593c` | |
| `0065/cross.numbers` | [0065: A reference to another table](../experiments/0065-cross-table-reference.md) | 145,776 | `35771d248fc0a79892958c269069782978c4c8293e0d80e4670c24d10aaf8b4c` | |
| `0066/if.numbers` | [0066: Comparisons and IF](../experiments/0066-comparisons-and-if.md) | 139,993 | `2b3a47839068774ffadbe6776a316a73ea5e7162f222bbc9935773c3b608c61a` | |
| `0076/package.pages` | [0076: The package format](../experiments/0076-package-format.md) | 89,444 | `02472f544887d708757f51680f5ceeba649fbbcc6b23dda4541d2036a8edcfcb` | a folder package |
| `0077/red-shape.pages` | [0077: A shape's fill](../experiments/0077-shape-fill.md) | 94,526 | `bedbfb8204a8d0eec9370f6d7a93689dd8e7f197a57e9479c4faa2146cb9b942` | |
| `0078/error.numbers` | [0078: A formula error](../experiments/0078-formula-error.md) | 137,142 | `d2168cfb37bc4e13a58af53e78fa002584e8adcf6b39e5d87ce6c0e01876edfd` | |
| `0103/round.numbers` | [0103: ROUND](../experiments/0103-round.md) | 138,598 | `10bfbfc0a497cd03f6b8b01b7f48e39b6d5c9eb27f220b01f3dbce883dc4fc8f` | |
| `0104/nested.numbers` | [0104: Nested functions](../experiments/0104-nested-functions.md) | 137,776 | `14562a3797519df4171c2cac2a9dcf333d8137993ba69f001e539fb7256421a9` | |
| `0105/whole-column.numbers` | [0105: A whole-column reference](../experiments/0105-whole-column.md) | 138,253 | `9f3fc61079693f0a327d8da0518128974cd358e14d08213b4d67a2b5c4a3cca7` | |
| `0106/mixed.numbers` | [0106: Mixed references](../experiments/0106-mixed-references.md) | 137,607 | `d1d8e93869a897dfb0e1e89705d73ec66f0423aeedd03a261c1733fcde575c62` | |
| `0107/other-sheet.numbers` | [0107: A reference to another sheet](../experiments/0107-other-sheet.md) | 147,000 | `19c8ea189e4c1b1c8a76faded092d944c68f8c89cdf4d3720886f407a0d55900` | |
| `0108/today.numbers` | [0108: TODAY](../experiments/0108-today.md) | 138,210 | `b1800eba064e4f5649acac95615857acf594fbc9baecdb02cea3b1c219858455` | |
| `0109/len.numbers` | [0109: A text literal](../experiments/0109-string-literal.md) | 137,584 | `53d89228098da569112fb3488c250e463dbb650e3c3e8d12fb701e2dd99f1447` | |
| `0110/join.numbers` | [0110: A text result](../experiments/0110-text-result.md) | 137,723 | `46ea836a65d2035b489d7a6320027d6c942e243b73bef3f8c1d1b8c3bae01c7b` | |
| `0111/percent.numbers` | [0111: A percentage literal](../experiments/0111-percent-literal.md) | 137,608 | `350957148c0e881f6d208766ca3d73932dabcf3148ac7d64e25573e856cc7c0a` | |
| `0112/minus.numbers` | [0112: Unary minus](../experiments/0112-unary-minus.md) | 137,613 | `172dfb32c1996c2622c38b07f58871b945d5c76781b35562d43cc9d4816411e1` | |
| `0113/samestring.numbers` | [0113: The same text twice](../experiments/0113-shared-string.md) | 137,639 | `a3150b0a6d2369d374c4d628777d66ce7cd36656433d4fcfcb881d6bf6088255` | |
| `0114/cleared.numbers` | [0114: A cleared cell](../experiments/0114-cleared-cell.md) | 136,887 | `a59a839dbd55ba1132cde094d03cbb4aee04627d5ea4eda3ec3165fcb4257bbd` | |
| `0115/newline.numbers` | [0115: A line break in a cell](../experiments/0115-line-break-in-cell.md) | 137,190 | `bfde5bfa0acf5981dce5673b556b3b78ac0434457902e54995392bd8fc567b29` | |
| `0116/extremes.numbers` | [0116: Very large and very small numbers](../experiments/0116-extreme-numbers.md) | 138,930 | `c25d7bbaa42ae46534e015d39143703cb836d0ce17a7231552f592f6acf02eab` | |
| `0117/dateonly.numbers` | [0117: A date without a time](../experiments/0117-date-only.md) | 138,119 | `63d0df9c147932546549d9b74b8f935ca988ce90474c3f0502deb8f07c4467c8` | |
| `0118/emoji.numbers` | [0118: An emoji in a cell](../experiments/0118-emoji-in-cell.md) | 136,851 | `56aace4439cc95ec68e2d531584e8cb500d0cc19c6b6e7bf81e0c5309fe1dba7` | |
| `0119/sort.numbers` | [0119: Sorting rows](../experiments/0119-sorted-rows.md) | 138,020 | `299ae4542b8410d0241a08286cb020322e008b6504fa50c0e01a3efd0eb8f35b` | |
| `0120/fewerrows.numbers` | [0120: Fewer rows](../experiments/0120-fewer-rows.md) | 103,029 | `a3f824bab98ae3e1539b34c4258a4ecee50b53915fdee345287a321be123f68d` | |
| `0121/emptyref.numbers` | [0121: A reference to an empty cell](../experiments/0121-reference-to-empty.md) | 137,201 | `dc7275fa3d1de56a80a0194d7dd561dc6a5adf456e3ea75b38606558fd68e3e6` | |
| `0122/tablename.numbers` | [0122: Renaming a table](../experiments/0122-table-name.md) | 136,716 | `37bc0d9832bad81c5a602582d49f1bca166df09ba0c5ad9ffd6b438e01baecfb` | |
| `0123/fewercols.numbers` | [0123: Fewer columns](../experiments/0123-fewer-columns.md) | 121,642 | `0a1fbe0a1a62f50e81b53c9b53fa9d886031445e2171912d74260bbd63dfe128` | |
| `0124/sheetname.numbers` | [0124: Renaming a sheet](../experiments/0124-sheet-name.md) | 136,478 | `a8fa6ed465fad3dcb20cd3a184ad31dd3f8f39e161d6195d7bc8a5084e103911` | |
| `0125/unfrozen.numbers` | [0125: Header rows not frozen](../experiments/0125-unfrozen-headers.md) | 136,593 | `09aa5cbe4a4070924a6dce904e3aca19e43f8b2acd24d81264dd46225ede8cb3` | |
| `0126/origin.numbers` | [0126: A table at the origin](../experiments/0126-table-at-origin.md) | 136,665 | `d4eec2212aeac21e3b8523a6a46fcedfd48087b817202d927476904e2ffc68e6` | |
| `0127/textbox.numbers` | [0127: A text box on a sheet](../experiments/0127-text-box-on-sheet.md) | 137,256 | `55f3da5bf5489ccf492a24bac530edb549dceae469c9d0143ebc37318af30acc` | |
| `0128/image.numbers` | [0128: An image on a sheet](../experiments/0128-image-on-sheet.md) | 137,380 | `5be0f52db66acb07ee1e372dc3960f7e93e953c1ebda60314da5c349ecb8a428` | |
| `0129/shape.numbers` | [0129: A shape on a sheet](../experiments/0129-shape-on-sheet.md) | 136,765 | `ca531ca29c534ca597a59489ded78f5bf9851b521a4f9c90fb634a3960e5f06c` | |
| `0130/longtext.numbers` | [0130: A long text in a cell](../experiments/0130-long-text.md) | 141,251 | `a112737c144e875dab32bda3983cbc1596bea21b826aaef19d2ba604cb070e9b` | |
| `0131/cells.pages` | [0131: Cells in a Pages table through AppleScript](../experiments/0131-pages-table-cells.md) | 108,479 | `31c552c1e1e598c304c85953862689ec3644d68251d5782b39a71938b871fe4e` | |
| `0132/formula.pages` | [0132: A formula in a Pages table](../experiments/0132-pages-table-formula.md) | 108,880 | `f19ec8f36080f813a6e7883e4eee94076b809a3133534a35368d56faea7ad9ca` | |
| `0133/merge.pages` | [0133: Merged cells in a Pages table](../experiments/0133-pages-merge.md) | 108,163 | `78baeb3d5dc524d8078a04b073227aeff30cdbd9642f04d12548360d44a55c89` | |
| `0136/headers.pages` | [0136: Header rows in a Pages table](../experiments/0136-pages-header-rows.md) | 107,117 | `0e9ae611fceb8260e03f1601e0c64a786c3bc2f582da3c421e878a731522432e` | |
| `0138/fill.pages` | [0138: A styled empty cell](../experiments/0138-empty-styled-cell.md) | 108,523 | `11e4c974eec1780258ea6cb62c153f1c3484e1edb6f9346912322743e3043a61` | |
| `0139/resaved.pages` | [0139: Saving an existing document again](../experiments/0139-resave.md) | 90,443 | `164956ba6e79fe5d86e110d7ec1198f37a9843398107dea7907b439164240604` | |
| `0140/edited.pages` | [0140: Editing and saving in place](../experiments/0140-edit-and-save.md) | 90,795 | `c76b2b0447c3d08a371f43114e7b9f090a300b914b6d58c1b4ec8ddc63bc47cc` | |
| `0141/big.pages` | [0141: A large body text](../experiments/0141-large-text.md) | 389,972 | `d0b8ff0a370f5b93cd6cee4ba3d138185b3d111d89ecb9df206e431a03107823` | |
| `0142/twice.pages` | [0142: The same image twice](../experiments/0142-same-image-twice.md) | 91,632 | `e918998e0f50f9ad220965dc4a1eb3be3e4fb48a67c693aa81401df09307306d` | |
| `0143/jpeg.pages` | [0143: A JPEG image](../experiments/0143-jpeg-image.md) | 91,933 | `1aab5753a61d5abb27479e64a2c513c97d3f29e0b5d72d73a76e8c5b6e48339b` | |
| `0144/odd-name.pages` | [0144: A file name with spaces and ø](../experiments/0144-non-ascii-file-name.md) | 91,240 | `a1705142553abc867c9c58e04e5cf37e407d531080e32f8d152fbdc881fb1e83` | |
| `0145/deleted.pages` | [0145: A deleted image](../experiments/0145-deleted-image.md) | 90,320 | `4f50d602134606eee8654aaf82fbd0acaa340897b17c8abecbe0f597d2855975` | |
| `0147/package.numbers` | [0147: Numbers in the package format](../experiments/0147-numbers-package.md) | 136,058 | `24149f49f47880fc38aba891595b79755735a410b50127b28bbf8357c5db5e54` | a folder package |
| `0148/large.pages` | [0148: A large image](../experiments/0148-large-image.md) | 1,820,787 | `02b2d229fc1ef0bf9f141b275d1c073bbc48a2523929752f165c02c6e4974b34` | |
| `0149/zwj.pages` | [0149: A family emoji](../experiments/0149-family-emoji.md) | 91,374 | `3cd83925698fbbd54b31ae3fbc825a53a8d0ec9501e6fb732f81845f05174e15` | |
| `0150/rtl.pages` | [0150: Arabic text](../experiments/0150-arabic-text.md) | 90,720 | `5947a1fdeb440c88ff1ffa9f513e7c2f691e7ebee0a9c8148337a31edca2763f` | |
| `0151/paras.pages` | [0151: A thousand paragraphs](../experiments/0151-thousand-paragraphs.md) | 122,055 | `cb4a0893fda5546bf52a822baa72373e069719067b90f23d968f8c475022886f` | |
| `0152/sizecolour.pages` | [0152: Size and colour on one word](../experiments/0152-size-and-colour.md) | 91,758 | `7f9c4deb975fe74ab04221249ee1addef4fdb09c502bc16406098c92ee23bfe2` | |
| `0153/defaultsize.pages` | [0153: Setting a size a word already has](../experiments/0153-same-size-again.md) | 91,157 | `b7d4b298e44e5545eead610e588213428fc5d6c458ec4a35a52ec443140b1ebb` | |
| `0154/replace.pages` | [0154: Replacing formatted text](../experiments/0154-replaced-text.md) | 90,742 | `ccad369b11dc31a02771bf11da4909e9d60d9af8007767222116fa50f32617db` | |
| `0155/landscape.pages` | [0155: The landscape template](../experiments/0155-landscape-template.md) | 84,704 | `df7e4db00af2ccf043c7ef73145ccee057338ad1625ee2fff8a95137e4e4b0b5` | |
| `0156/layout.pages` | [0156: The page layout template](../experiments/0156-page-layout-template.md) | 89,783 | `7335375993c4af5f039bf35923d796b858f79ca85a9a7b8a4c4ab88f7aa33921` | |
| `0157/black.pages` | [0157: The black template](../experiments/0157-black-template.md) | 82,601 | `27ef09892eab773a76567314d3314df97a8417786d50b8718d5d5fc6e0f0f2fd` | |
| `0169/checkfalse.numbers` | [0169: An unchecked checkbox](../experiments/0169-unchecked-checkbox.md) | 137,354 | `7d675da2e08f31fe01c3f301675bab0c1fe776163c6688db7f7b1d25834b3a0f` | |
| `0170/rating0.numbers` | [0170: A rating of zero](../experiments/0170-zero-rating.md) | 137,982 | `c4ae457ef797b6d6f07dc5c54e104dd0c567f080ab9e2b52a94c0d0ef170b10a` | |
| `0171/slider.numbers` | [0171: A slider](../experiments/0171-slider.md) | 137,369 | `84c0b21146e29a892cd6666af6bb13556313f330c1384ef2caaa1a757d013178` | |
| `0172/stepper.numbers` | [0172: A stepper](../experiments/0172-stepper.md) | 137,273 | `ac809deea3a67fa776df9a907b278e288e734f2e367b4c33be5e1366c5d7e4ce` | |
| `0173/popup.numbers` | [0173: A pop-up menu](../experiments/0173-pop-up-menu.md) | 137,163 | `078e5525a9cd3155bbc06f9fe9d27312465762329e5e29a26a5991c4f6af8b8b` | |
| `0174/negative.numbers` | [0174: A negative number](../experiments/0174-negative-number.md) | 137,230 | `6c4ff5a73ac9206b513eb4f6b820c850625b185e42415d895d380885855792d7` | |
| `0175/boolformula.numbers` | [0175: A formula with a boolean result](../experiments/0175-boolean-formula.md) | 137,577 | `873a427205d9831297d18ff52d577cdbb5a3077ae4258c355b574ac1b0f9f7cb` | |
| `0176/numtext.numbers` | [0176: A number typed as text](../experiments/0176-number-as-text.md) | 137,314 | `5c1d3a9cc677824464065cd8107e69fc833027d173f5742a3167be09f4bb9a60` | |
| `0177/described.pages` | [0177: An image description in Pages](../experiments/0177-pages-image-description.md) | 91,240 | `539be8674bfa5992582ea3973cf0a68568d01d84e93e68f8f43b9f24bbd1ee96` | |
| `0179/locked.pages` | [0179: A password](../experiments/0179-password.md) | 74,651 | `f3c9890b02bd7ff9f795091ede136586336e15dae5a89d0e8bbd52595ad15a94` | password `pw1234` |
| `0179/locked2.pages` | [0179: A password](../experiments/0179-password.md) | 74,667 | `9c2ac090fbabb1e2b621e453d8e7ed8164d137c679aa06ba151c36be0dca78bc` | password `pw1234` |
| `0179/plain.pages` | [0179: A password](../experiments/0179-password.md) | 90,296 | `fba6494794eac6e6b60bd0c200c443c3e94268398e1905f6e32fce5fe437bb12` | |
| `0179/unlocked.pages` | [0179: A password](../experiments/0179-password.md) | 90,297 | `4df562a14d61d3c42020874103afa8b70e73792a59c3ed04b2404d8cdfe19899` | |
| `0180/accent.pages` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 74,651 | `86035e2507a11b6360a7c07438065f4dec87af66b08a51ed0dce9227146412c8` | password `påss` |
| `0180/image.pages` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 75,359 | `a76a2f1b21893b4bb2ff2c618c8306485839d3ba7bf31197eba5c5a3697c8bd7` | password `pw1234` |
| `0180/locked.numbers` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 83,399 | `3f68cdf08e78a9ad812326894d1190bdf4a5429eba5082b644ab2793e4be667f` | password `pw1234` |
| `0181/numeral.numbers` | [0181: The numeral system format](../experiments/0181-numeral-system.md) | 137,220 | `dc1f9b0df7399fbea485003547013a78ff034f0dbab6aff27f1e605e43f3dea0` | |
| `0181/plain.numbers` | [0181: The numeral system format](../experiments/0181-numeral-system.md) | 136,926 | `48ec08a0d8a951a439736e25cf14b377d449690ca2d31cff65d56ef6fa062799` | |
| `0182/transpose.numbers` | [0182: A transposed table](../experiments/0182-transposed-table.md) | 105,287 | `84088072197652e4b35ab5c42d5e85811fb4dcd3b5d9a61c640a096c54da889b` | |
| `0183/frozencols.numbers` | [0183: Unfrozen header columns](../experiments/0183-unfrozen-header-columns.md) | 136,590 | `8ba3a0c2fb891b855df42242d8f5dac7d4968f612457a3bc09e4b07339644aa3` | |
| `0184/footer.numbers` | [0184: A footer row](../experiments/0184-footer-row.md) | 137,439 | `731709bbcaf95831a13517280a49aa7d2e68c304e1482048e49497e193152f33` | |
| `0188/movie.pages` | [0188: Media in Pages and Numbers](../experiments/0188-media-in-pages-and-numbers.md) | 95,571 | `9a8ebadb08d3371e26b00a9feecedc643f469b478d825d5a336696619183e436` | |
| `0188/sound.numbers` | [0188: Media in Pages and Numbers](../experiments/0188-media-in-pages-and-numbers.md) | 142,757 | `700658b09c2470b1c2e890ad2b3906a6a21905ef8330f6241d64892b88504c0f` | |
| `0189/link.pages` | [0189: A web link](../experiments/0189-web-link.md) | 90,396 | `7c28df6d409974c61f6c1d96486b812670906a77ebd1f3b83b74c15ea27e9f23` | |
| `0190/email.pages` | [0190: Email and phone links](../experiments/0190-email-and-phone-links.md) | 90,395 | `e834212e75cd38e218988e18ff1906f1e3c5d2ac0abff3cfbef161258e4d6442` | |
| `0190/phone.pages` | [0190: Email and phone links](../experiments/0190-email-and-phone-links.md) | 90,400 | `fbadcb0a949c17da3e55fc7381500312fd85a97cc7d49c13f2b837c4b1ed2b6b` | |
| `0191/bookmark.pages` | [0191: A bookmark](../experiments/0191-bookmark.md) | 90,344 | `7c802193ee4893af738f96ec3e6fa25997bb31496f9d10828f490f173fe1e19a` | |
| `0192/bookmark-link.pages` | [0192: A link to a bookmark](../experiments/0192-link-to-bookmark.md) | 90,821 | `241881ca339ca09787aceee9fe0a38ec0a4623bf88561521948910769f31fcdf` | |
| `0193/empty-comment.pages` | [0193: A tracked insertion](../experiments/0193-tracked-insertion.md) | 90,301 | `4af1e5817a56bcf21e67f0b65de14007307500783f40a4a35899e91b78f92e1a` | |
| `0193/tracked.pages` | [0193: A tracked insertion](../experiments/0193-tracked-insertion.md) | 90,954 | `8c091a38124ae34ba5e702d6fe1efd2fe7ea0f6c4ccb921f0ef75569751976ba` | names its author |
| `0194/deleted.pages` | [0194: A tracked deletion](../experiments/0194-tracked-deletion.md) | 90,932 | `eecbe112ce8fb4e10e1880f5dff21bde5d8261f12c29e14c3da67ee6f0cd9380` | names its author |
| `0198/book.pages` | [0198: The blank book template](../experiments/0198-book-template.md) | 84,808 | `adf41653f330ee70767183ca00f9b47e7f889a09a2bcbac981df9f866fa1e233` | |
| `0200/highlight.pages` | [0200: A highlight](../experiments/0200-highlight.md) | 90,590 | `ddacfc01c1f916ceee3ab1506b0f6fdb22cf49ca368a875260eee25db045d5fb` | names its author |
| `0201/page-count.pages` | [0201: A page count field](../experiments/0201-page-count.md) | 90,516 | `8982c44b270e92d44e3e7fc1d6d5d90f9cdd85140b4b9b4cb8a7ded528af4c73` | |
| `0202/toc.pages` | [0202: A table of contents](../experiments/0202-table-of-contents.md) | 92,330 | `b22d0740745cce16a5ccae294d5037860f31c475e8234010f3be124fe79c6d49` | |
| `0203/superscript.pages` | [0203: Superscript](../experiments/0203-superscript.md) | 90,557 | `f67f0c1b009e0ca477acf3eb40c4e297f1f77761db0c2cac342c5a60a44b911d` | |
| `0204/subscript.pages` | [0204: Subscript](../experiments/0204-subscript.md) | 90,634 | `749db3c095bc17f0754e10aeedc4fa127f0d592a18e3c5eaa3e333876250a8ad` | |
| `0205/small-caps.pages` | [0205: Small caps](../experiments/0205-small-caps.md) | 90,798 | `68192f69e6143e5529ffd5542e45c22024ed64f712cba0026ac3968df0726dce` | |
| `0206/all-caps.pages` | [0206: All caps](../experiments/0206-all-caps.md) | 90,989 | `f72dbc4e4b2a9e1319007e729e297a4ae5d760a1d782dbb23459a5a97ccc9f75` | |
| `0207/looser.pages` | [0207: Looser letter spacing](../experiments/0207-looser-letter-spacing.md) | 90,765 | `817857e9ac824d378ba3c17a630637e18bb561aba0bbdfaab06137d497e6aff9` | |
| `0208/no-ligatures.pages` | [0208: No ligatures](../experiments/0208-no-ligatures.md) | 90,772 | `7068ac4faa1ddcdb1af4e57464de5ff41fbdde1be9862fe1677861fcad462f3c` | |
| `0209/raised.pages` | [0209: A raised baseline](../experiments/0209-raised-baseline.md) | 90,744 | `f8e3df0ee3168408d23f956fcb1113865c3e3c6580e5df2da92062ef64e03d85` | |
| `0210/column-break.pages` | [0210: A column break](../experiments/0210-column-break.md) | 90,458 | `2e269d63681d95ee3ef9dc6a5be46936d3d0a812dda01988e4f1342dc76f198e` | |
| `0211/date.pages` | [0211: A date field](../experiments/0211-date-field.md) | 92,940 | `430659fab08556c8fc151734402e46f2ab93e04ee0017cb6699c715e9d43358c` | |
| `0212/placeholder.pages` | [0212: Placeholder text of my own](../experiments/0212-placeholder-text.md) | 90,778 | `67f0aba65e0983244760c7e3f0cf049e2c8c756148300052fb5be85bef130f7a` | |
| `0213/flipped.pages` | [0213: A horizontally flipped shape](../experiments/0213-flipped-shape.md) | 92,369 | `e2b80097d57d933b7c2974ee845548a5134eb8325507fea45ad7388601c47a40` | |
| `0213/plain-shape.pages` | [0213: A horizontally flipped shape](../experiments/0213-flipped-shape.md) | 92,381 | `2cfedb21087e089187adb53f48797bd950d7d1b0d0461f57c70520d55150a335` | |
| `0214/flipped-vertically.pages` | [0214: A vertically flipped shape](../experiments/0214-vertically-flipped-shape.md) | 92,378 | `18d5ef7a8508d90df2246b1948a6cc7ebaf1375f5f82cb3e41274d8f7f1962d0` | |
| `0215/blue-style.pages` | [0215: Another shape style preset](../experiments/0215-shape-style-preset.md) | 95,552 | `6d6311ec79353e445e997c2508a35c0f33adc2685b354bae32bb6f63548846ba` | |
| `0216/group.pages` | [0216: A group](../experiments/0216-group.md) | 95,683 | `72e61cca97a09c558136236e056ae441237a9260e93bb92af8113dfee7894d1e` | |
| `0217/editable.pages` | [0217: An editable shape](../experiments/0217-editable-shape.md) | 92,412 | `de99366e91bc2f0d79452dce9356273f1f52eb4efc396644eb076415a3d8a81d` | |
| `0218/oval.pages` | [0218: An oval](../experiments/0218-oval.md) | 93,910 | `afa0f2763c220f2fad55bba7bc90f7498b966ea095f621c5291f65adcec41d53` | |
| `0219/polygon.pages` | [0219: A rounded rectangle and a polygon](../experiments/0219-scalar-path-shapes.md) | 93,769 | `d831f68d75efb62ce86d9d5770bae0c42aabb3a00837191ca7a40b66fbf037bd` | |
| `0219/rounded.pages` | [0219: A rounded rectangle and a polygon](../experiments/0219-scalar-path-shapes.md) | 92,905 | `144e563d2d4cde274d324aa5e2c35f84f92933fdb419b8378a4d8a9cc51ea8ce` | |
| `0220/arrow.pages` | [0220: A star and an arrow](../experiments/0220-point-path-shapes.md) | 93,593 | `1c6fa249f5b6e2f90486a0702e492d52599eed4a1afef1df45dbd37fbf779d90` | |
| `0220/star.pages` | [0220: A star and an arrow](../experiments/0220-point-path-shapes.md) | 94,222 | `596b52a287fad47a35e735f942ba126c85a15fd4dc067f7bc266efd5c5ab0ba3` | |
| `0221/bubble.pages` | [0221: A speech bubble](../experiments/0221-speech-bubble.md) | 94,101 | `d7f552eb4356c537a5ae2083a536422d738aa61f8f0c4b7eb76e610dabef92fa` | |
| `0222/column.pages` | [0222: A chart in Pages](../experiments/0222-pages-chart.md) | 112,835 | `68eae989982e320ef174dc1b0014376fc7f0027649b4e1d452453cf6edca9df7` | |
| `0223/ABS.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,121 | `a003ecb0b31aba4a8af02d3cf07297d2cc5cbbe320c47d456bf0a27c8736c542` | |
| `0223/AND.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,963 | `2382795612aaabe6eb2626a3c1fb1ccc6e800cf31af2545194b469f889a6371a` | |
| `0223/AVERAGEIF.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,750 | `919a0222a61c51b61f37fbef2663b2290aec21def534eabec1d799301b38de26` | |
| `0223/CHOOSE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,640 | `31dda8d8a81cd1a237e2ddd565bcb310ecafc13ff767b705f343c1c047e3350f` | |
| `0223/CONCATENATE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,723 | `316435161c7ab89b3598ba22dadb18aff95b2a521cda5daafe64a4c82e929d16` | |
| `0223/COUNTA.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,689 | `60819664d0145f13045d1890762f854c7238eca7af187f8bcafac889d47ff83f` | |
| `0223/COUNTIF.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,661 | `0674b2917f67265b9ddf5d0880d9175f94dedf0c42c0eddb3171754b6abb1e1c` | |
| `0223/DATE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,245 | `17f2bb1a4995da22746bde7a0f06343f5c33de5aef731c2ba170d790f5f6bce2` | |
| `0223/DAY.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,601 | `a4850e74d26b3b624d8e5edd0b5fb16da860a20019812606ba1de33bf89237ff` | |
| `0223/EXP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,151 | `d25a91c842f67069573961d703c6238eb0a7329058c0062e5affd41c647d0fc1` | |
| `0223/FALSE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,995 | `28f86d04c53df68c079dbfd9046ab275e7fb9d362b8ae68a5b8e75190c8a6718` | |
| `0223/IFERROR.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,370 | `4946b1a9d8f98e2aa6e650c43a1d2d57bb03d5f7f4bd457d9d02cdcd96bec88a` | |
| `0223/INDEX.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,777 | `256552233e2de114b749c464e5a54c5ca2b9b7c1e1cf88bf5480d8f6d24ceede` | |
| `0223/INT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,591 | `14cd57489262b96fe2a17420506213e2ae17aa8bef2a48f7ae369ecc86259369` | |
| `0223/LEFT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,624 | `4b11fab146d42594c46a5936ff70bcba198433b92a9e50f5313a084c60d8393a` | |
| `0223/LN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,016 | `4230bc8175882ded08b13456f997620d2ef19de362afb6a9e4f8cf0f25b0667e` | |
| `0223/LOG10.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,249 | `bfa07f87a0b04f6916aeadbe6df438d2aa5e519457361425d9a59b893be93d5f` | |
| `0223/LOWER.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,810 | `96392ab4b6927425a790aba8c1b610a127d47503e95e1bf4bed4e83e3ef2195d` | |
| `0223/MATCH.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,665 | `c5caed8727264fbaff391d2708461b1d52413f4c949c9e89edfeee470e31e8f5` | |
| `0223/MEDIAN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,600 | `aaa6e28196edd6272b6c311de056c3305f6923dbd18dfcb2414383361de36342` | |
| `0223/MID.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,643 | `d91c36edbabea63dd28cf3144dd5ebdbc508261934256b0f77e1c1e8b05dcd95` | |
| `0223/MOD.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,587 | `a7e2df2aa8591161684bf46b5dd91211e0a87888d29954b90f2c25e3c9e74a5b` | |
| `0223/MONTH.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,619 | `6405b10d7792f3f014c4a3d70117bf0f53dd87c636c2c7d8b80a74892b427748` | |
| `0223/NOT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,281 | `f334c0ba41c687639e5cf394dc7c699e0cc2535daed9e67905e15ea0c5a0ae99` | |
| `0223/NOW.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,629 | `977b5bc132d869753357f51bcb7cce95dc24d45bbbc39ea2442e4dbe3ae04e62` | |
| `0223/OR.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,963 | `bbe3cad2bb10cf91111c794456984d20c6a5f322b7c89477691b0ea68ab34a94` | |
| `0223/PI.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,763 | `efae2e425b6582850314e09e9674fb2f3fdd3ae24fadeff9b43b2830465e2c61` | |
| `0223/POWER.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,559 | `68287222f260f6b724760be1c42c14450a9939f11d9dd1a8dfe8d0e68f76d882` | |
| `0223/PRODUCT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,707 | `02d37fc875aa71ec1f17a29fca3baede7c58753a77501cd44309b96346a5bd5e` | |
| `0223/RAND.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,776 | `5c6690a8b76ad71bc52b207a3f34bdc638308ee7383e20c9dd0803034acc275c` | |
| `0223/RIGHT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,553 | `c957e31c844d1afd132af28812aff0752420857985a6e2d956ba2ade0356dd6a` | |
| `0223/ROUNDDOWN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,771 | `65f81efd368878443a6469b0633072469951a66031bf72b9d891b46e41f0137a` | |
| `0223/ROUNDUP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,459 | `4e0001f62cb1b50fdfcf8bfa726316fb4050b1ed1fc55edfca8b112d407cff33` | |
| `0223/SIGN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,560 | `4a0b25efd93b380b42867007d1b3479e69793c2e9b7e6ce296be24c19419ab24` | |
| `0223/SQRT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,222 | `e500028e29c280e7641dec24db59864e660c60834cf92ca1598cc2a67dcda5ad` | |
| `0223/STDEV.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,592 | `0375d7f314af76df78c32e92b793e7297f2d642669516102643652225dfdfa8d` | |
| `0223/SUMIF.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,575 | `1ef317c110a7b1689c1cfd39e58b036135320a113ab3bf6854d09c603177b213` | |
| `0223/TEXTJOIN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,757 | `5a024afa4feaec04e3e3e6b43164c9cdf36db0abb1dee6da8878ddb2896d4e91` | |
| `0223/TRIM.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,602 | `521dce6e32beca0c9c0d5ac0d02b96bb0a1e19059c39716d122673d4c90ea5bc` | |
| `0223/TRUE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,891 | `4c2f081db6329a0bdae4aac82f9fffd850f30fcf47a4de115943db2a99e31587` | |
| `0223/UPPER.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,834 | `73b020008368b0d7a7cd9cb29ab1162b8ac14de20dc90d4b59f9ec821d483e18` | |
| `0223/VLOOKUP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,803 | `6337407611bb57ac49f4811ab288422cbdd7721b0f6b43ccc884adc4f68c12c8` | |
| `0223/XLOOKUP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,769 | `2bd66492596c9864d84033b5eb3581b44d8daf939a1b108a64744e1bda0d0f4a` | |
| `0223/YEAR.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,548 | `84f324b3a13cc289153afa6d0eec9a7a0a3cd30a2a786cb75e561c46517e1866` | |
| `0224/bubble.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 109,028 | `4fd27ba380ef4950da85075dae7992c24ff6df82a096c93ca13b9b8b18e62a00` | |
| `0224/donut.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 117,360 | `e0b264282745859fed0bb98ff85af3c7a00991974b765c0e7908653c384b5e01` | |
| `0224/interactive-bar.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 110,824 | `34ccdcbe2281dff1798c0880de6a479a1d209d3926c9e799890e2ffb5fca5195` | |
| `0224/interactive-bubble.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 103,749 | `56cc9e7245c39273a8ae05577b41ea5e6273dce997cd6e884bbfa7c68e15931e` | |
| `0224/interactive-column.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 109,868 | `148b49967f75b983508ca12d4171ab1a13ba326d2a9802494e071539714837d4` | |
| `0224/interactive-scatter.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 102,700 | `15fb38de7fe3024f7a73ef6fea5cabe362a93d822a4a4cb03756fb2aa4653c28` | |
| `0224/mixed.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 113,371 | `c118eb6c6c8a1ca0ce63c053783dd0dbe7ee35d2b4e4aac74e02a40dbcd30a5d` | |
| `0224/radar.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 116,871 | `5b97826b481e09012e8a6792d5c944e7fffa34900be888e798f943120208e982` | |
| `0224/two-axis.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 115,009 | `9a069513c86e75803aaf9917de6d07893cba007e02c552410b30ca5493478bac` | |
| `0225/linked.numbers` | [0225: A chart in Numbers](../experiments/0225-numbers-chart.md) | 137,249 | `eb73722d82dfcd750b5c731cbd3113b240d96c618aefcb1fb5a6f2caf7568c78` | |
| `0226/category.numbers` | [0226: A category](../experiments/0226-category.md) | 146,960 | `d3effbe19f95289167edf7e259f581844b2dbf6e5ca8331fd09815db75d28616` | |
| `0226/plain.numbers` | [0226: A category](../experiments/0226-category.md) | 138,837 | `317c41bb605f4f3e2e492fdee400ab0f24f0989884239cee3a3f2ac7f2dcedd1` | |
| `0227/pivot.numbers` | [0227: A pivot table](../experiments/0227-pivot-table.md) | 152,905 | `7f094073fdadcfe4f9605a8efd89c80f136c1805e06df8e3a70bf38f59cfee3f` | |
| `0228/caption.pages` | [0228: A caption](../experiments/0228-caption.md) | 95,164 | `505e7e0e1ccba75b6de99762a65085c396621ccb9c38ff458a0c078b630989b1` | |
| `0229/title-and-caption.pages` | [0229: A title on an image](../experiments/0229-title.md) | 95,797 | `1e2d32b5862fca8695d33cdef37721474270d9924ff6b5ceb0839c7a0a46e6ba` | |
| `0230/alternating.numbers` | [0230: Alternating row colour](../experiments/0230-alternating-rows.md) | 136,512 | `d72dd5a41217d98936b0dd15975392a6fd19d12ebaf3919be52e48f274a2d4e5` | |
| `0230/plain.numbers` | [0230: Alternating row colour](../experiments/0230-alternating-rows.md) | 136,871 | `b71905108e18e1512041ef1ca35146078ccb812666fe8fc56770b955ca62c2e4` | |
| `0231/table-caption.numbers` | [0231: A table caption](../experiments/0231-table-caption.md) | 137,193 | `aa71474edebaa9f745cecd1d8c365ecd0828a00988b0b8f0722ad8d7d2b7c9f2` | |
| `0232/no-title.numbers` | [0232: A hidden table title](../experiments/0232-hidden-table-title.md) | 135,066 | `caa55f52aaed185bf9146dd486a0e552d2cd4eae90224404e769a9732c4921d8` | |
| `0233/title-border.numbers` | [0233: A border around the table title](../experiments/0233-title-border.md) | 138,627 | `f5fb42d1bdc0b552a473d9b63c70f7005b35f9e97d627008c483b80eaceffe5f` | |
| `0234/no-horizontal-lines.numbers` | [0234: Gridlines](../experiments/0234-gridlines.md) | 109,828 | `88ac2a760b5a5ee0a9b2e4b1abafd18e0b91908a9be145cd551d65921f6463a3` | |
| `0235/button2.numbers` | [0235: The other gridline buttons](../experiments/0235-other-gridlines.md) | 131,820 | `b6ff106d1061d5b29681767f2749eeadf6601f7de79c8bed06f6303d3ff6ef97` | |
| `0235/button3.numbers` | [0235: The other gridline buttons](../experiments/0235-other-gridlines.md) | 133,149 | `16f9110bdedb0d2285e71b00056509d66f33bd2f5d485b3144028eb2818cbfdb` | |
| `0235/button4.numbers` | [0235: The other gridline buttons](../experiments/0235-other-gridlines.md) | 136,715 | `e0c21b2ca3171e58f317d060429889772934aa37bc6dce56c19185f87fe5c549` | |
| `0235/button5.numbers` | [0235: The other gridline buttons](../experiments/0235-other-gridlines.md) | 136,871 | `9f3bda4cbcb6f5fc49d1469b3cd4247501747fa8aa5068fdcfcaadaf97c7b8c6` | |
| `0236/hyphenation.pages` | [0236: Hyphenation](../experiments/0236-hyphenation.md) | 90,351 | `7c735e2ae6fc500b2df55e657ed5bb4b8a47f9090711b3a63c5917478a97b378` | |
| `0236/plain.pages` | [0236: Hyphenation](../experiments/0236-hyphenation.md) | 90,350 | `da66cf898fa6788c5b738678f53d6180ab8f798467657badde5fb6c39a9f0bb0` | |
| `0237/no-ligatures.pages` | [0237: Ligatures off for the document](../experiments/0237-document-ligatures.md) | 90,350 | `a3e532df71cd8aac11d3566b325104608688545b0d2716631ef5b129e7b82ffc` | |
| `0238/no-header.pages` | [0238: No headers](../experiments/0238-no-header.md) | 90,352 | `6e6e9bdd299b5661041240d768557704dbb686f1d3feb082205c5b90b75e1288` | |
| `0239/no-footer.pages` | [0239: No footers](../experiments/0239-no-footer.md) | 90,354 | `a954cef2a22570cab4a0019a0f280dd69a5d15bdef899387b111112fb0d2e83f` | |
| `0240/no-document-body.pages` | [0240: No document body](../experiments/0240-no-document-body.md) | 89,806 | `b6f963b0cad955e3628292148efcf135a16a82adce0678c6298bcd8e37b54d36` | |
| `0241/zoom-200.pages` | [0241: The zoom level](../experiments/0241-zoom.md) | 90,328 | `3bae3226b3a37f0d1815e1c8657bc575f381f9f98cf6a6478720142dac137de2` | |
| `0242/two-pages.pages` | [0242: Two-page view](../experiments/0242-two-page-view.md) | 90,341 | `dac33911002f54ae42ebeacedeac567e903066bfd18bc9e5ce7ab5ae1029d56c` | |
| `0244/media-placeholder.pages` | [0244: A media placeholder](../experiments/0244-media-placeholder.md) | 93,939 | `882cb62e75a17d6b89c6c46a29e3da211d58905a90bc7389ee8b9a852e366590` | |
| `0245/oval-mask.pages` | [0245: An image masked with an oval](../experiments/0245-image-mask.md) | 95,114 | `fc157925e2fc4640ce7ba4b30a7c7ddf721dcc1d8394885750f818faa00883eb` | |
| `0246/no-repeat.pages` | [0246: Header rows repeated on each page](../experiments/0246-repeated-header-rows.md) | 109,485 | `1df2e30d0942464fa4d9339816f681772035b82532e1994162713ae29f676c92` | |
| `0246/plain-table.pages` | [0246: Header rows repeated on each page](../experiments/0246-repeated-header-rows.md) | 109,446 | `3bd8d763eba804becd046d479b5218e6c6b177deb7004fe0bba0f965de1febf3` | |
| `0248/ACOS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,606 | `be16cd8fb04f85770981ec1b4395936919b6af6d43f29729677161e05e23f497` | |
| `0248/ASIN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,016 | `3324a64cd496575bb142dff7a290a06807d0fb4cce11fcd8e2dd024caa5abe78` | |
| `0248/ATAN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,805 | `73d743e91851ffcb11f25d39bd14153902c86f0a4e46fac08e38c7d5d17300a0` | |
| `0248/AVERAGEIFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,755 | `37f1615619d63922a0830b7032794549782fe360329900a99dee6692a290bae8` | |
| `0248/CEILING.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,612 | `14145bc76918f846587a2385fb876a10aaa41ddfbd366688e8ae7f15a755a0ee` | |
| `0248/CHAR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,671 | `bd1788eda89763547aad2fd07aae4ecec431ce1151397bd87ceb8e28f3d3cdda` | |
| `0248/CODE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,703 | `a4720dfd647f3c245d6a05f5a90621bce90851d77cd637b5094a21bee17ce478` | |
| `0248/COLUMN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,205 | `68d8cbb1782ec7a7d3357ebb4adb0c426a74fb7d57641498cd0c62ca9e5ac315` | |
| `0248/COLUMNS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,754 | `405eae6e760dfb4715d93696c1a442d509b3a5d75dde90b71bedcb2a0ff94808` | |
| `0248/COS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,577 | `6e5f159cfb6bc3080da519c28fa9665f1aa95008bed8fe5316ab19897b6f704f` | |
| `0248/COUNTBLANK.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,714 | `d77e0775dc1c6905d9442c33312e847f31ee109c6032045c6e57421e0a895ede` | |
| `0248/COUNTIFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,726 | `2c05fc0496c985eb2b3083de28b003ca9758f6289c3d72ad3e69c524ced68859` | |
| `0248/DATEDIF.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 140,171 | `a747e7faa7bbb4ba6945eabfa1354fa3b0269521b7a7f90df2682dc51cd5b87c` | |
| `0248/DAYS360.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 139,059 | `fe52283aaad1f878c979b6f8d2fa5b4f41d0df9166006ffbdf36be1bec3aeab1` | |
| `0248/DEGREES.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,714 | `245c3c8eca03da68c22e6af7ea7648c0ca7082a3489c3306dfecb20b5baaefdd` | |
| `0248/EDATE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,239 | `05b5fde2e675fb47f69906a1b13073b927bf9afebddf0e4c1755dbc543c80b67` | |
| `0248/EOMONTH.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,251 | `415ae7a6142300b3aba0de30f81e992174fd894c208b7012e3c37b5160c591d1` | |
| `0248/EVEN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,130 | `1e6f477d483b553ef293eae1941a9c887ce46215d02beb169ca90d03dd6e7916` | |
| `0248/EXACT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,499 | `ee17fed12d908035cfd24932671d887b9073337114c7847da58d4f274e806510` | |
| `0248/FACT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,720 | `575059e7e571374ca850bb2ec42b10a9d2e6dfc2d7d448df05a4b474b4812db8` | |
| `0248/FIND.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,586 | `53f675c8b5de2c683f98aa44e8041271f4dbbc246fe7c8e72e050b15934cd397` | |
| `0248/FLOOR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,576 | `d58322f86126c62ff271438ecef19a239c18604ac972e349ed04f6a307ac030d` | |
| `0248/FV.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,248 | `ed512534f2bcfedacfd639b4c31004afdd0820f33ab43286d07c4d1ac3aa1dc7` | |
| `0248/GCD.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,371 | `66c5a18ca115822c00cc9cda1c3d9485421df33571a8594dc8eeb8f98f90cae1` | |
| `0248/HLOOKUP.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,805 | `934155104e37461872ca7814f8203cbe36ae212a14181d93f4b063c2d553df89` | |
| `0248/HOUR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,446 | `3e0f9c20bc051ad80b9d80a44e5c90a90b1fbd848853cedede99d15ffd0acb2f` | |
| `0248/IFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,659 | `fde6bf92f79a8cfb8ff438498ed943f9e902cc94d58fc3a7874736f688dec487` | |
| `0248/ISBLANK.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,436 | `a38ba7c65bbaa529b5575276d9947f8dcbfc79bb563ac49f03ea13c0862a9c3b` | |
| `0248/ISERROR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,940 | `a34f48043e0dbf73f1c569e925aaf95266d5ddb6ddf0663c9797afa2e8e949cf` | |
| `0248/ISEVEN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,902 | `b9f12e5cb04dd0b7f83ef921d99f37c2c6c4bc93b36e43fea50cc066617b7e43` | |
| `0248/ISNUMBER.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,557 | `c950c145695716ee037420ae8d1af1d7cfacd430644f78f149ae9a7345d8b70a` | |
| `0248/ISODD.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,282 | `2699cfbf8ab251869ee11bc8a7b0a34efd6bd7f3a7957b10c8dbec0488d0b930` | |
| `0248/ISTEXT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,313 | `9073593bb5cad5778fcfcac7021fb9f024f069b735f77bbcf7800655768dc052` | |
| `0248/LARGE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,726 | `73b54fd9cdc92c024894182bfd3025e062f188415f7b8fe7dcbed3d847a3949a` | |
| `0248/LCM.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,335 | `57bb6c3199186763777b08bc6afcf7cb36a8be82eff7b68859f036b6c4bee377` | |
| `0248/LOOKUP.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,660 | `16f46d7061a2d7c12b41f005cbd80da6cd0447e4a493d3606dd8fc5d824d2fd3` | |
| `0248/MINUTE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,714 | `20a908ff6897b82318059780714af41d932b96ce876cbd256d4e22d87613d5b9` | |
| `0248/MODE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,675 | `8a9c8d65a5cda6def9ca6b17bf3363c9f6405cc7aa45b54754e0d800f3f13d3d` | |
| `0248/NETWORKDAYS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 140,478 | `e338263b4ac74db4ec3e7ec6fbd12eb56ee5c6be7b97e586717503a8928150a7` | |
| `0248/NPV.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,654 | `9584628b0e5e413ed1268043bca3867af55ae8a6271f002a8db81b362a75ede3` | |
| `0248/ODD.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,041 | `647e30a25c9cd253272991ca0075aecdc5d0817ce5324f7492971d0a1ff52970` | |
| `0248/PMT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,203 | `44ab75a8884b692317800280e51f65f4304870f3ae5eb0029aed5a8df7016f22` | |
| `0248/PROPER.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,699 | `02105cbdcba8237cba725033c1e8ff33251cbfad4c263a3d3dc7084d4634a45b` | |
| `0248/PV.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,620 | `c7f0a47d390f3a01e989edc5fca59bd0c7ef0f83d4e2dc77175df76e50a997eb` | |
| `0248/QUOTIENT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,694 | `dacfe10d9ef2f0ec2a4f18efbc321c23fe7523bdcd7d801556fb0d18e5702014` | |
| `0248/RADIANS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,624 | `f4a41306c9245cd17e6a55f1bd7f745fced4b0ffcc53ff8be5b9b136dd1c23df` | |
| `0248/RANDBETWEEN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,607 | `fe9e2edacd6f6f30f1897ffb7ab3f1d4d58093e1e6ed24c16ebdb350ba7c181c` | |
| `0248/RANK.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,771 | `abc0404f1f1a2d04d13c07e889ece1ea3bad1debaa873f4822cb8d7a449603f5` | |
| `0248/REPLACE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,667 | `ffcac2704a389de2b34ed2af8ce77c3266c0997873a46b4e579385377ea86abc` | |
| `0248/REPT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,822 | `63035f7d27c5a4dd7ae66fe97af5d692514cb0343aa8c66cd90bd7ee7ff45070` | |
| `0248/ROW.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,559 | `bd8f0e036a52425d1d3b12cfbcbec84f79078b0daf9a8272b49bf7832c0f147b` | |
| `0248/ROWS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,668 | `08058f1b7ab09a985c6f7b60c2ce59e4bb15d3424bfb2dbb36a0dd215b7c0fa1` | |
| `0248/SEARCH.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,603 | `1b7b3315906c9c617bc88f11bc38644eda46186e695eed5fe174880a2f8788bf` | |
| `0248/SECOND.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,604 | `f87d2fec71954ac65b7ea4bcbf4386a629b9fbbdd31481147f81c3d72ed3f767` | |
| `0248/SIN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,016 | `3ea7eee04168282ddbf738a05b265a241c784bad500e3d1c9fcb9aa249ebd8eb` | |
| `0248/SMALL.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,706 | `671c620c41365a89c2348706821aefe2de9f5bd6c9a1f504b374d5614a259b3e` | |
| `0248/SUBSTITUTE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,837 | `be178926579fb40f90f6eade4a613b32e462b94cbd87d015983170c6657e3503` | |
| `0248/SUMIFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,764 | `307aeec56a9a2657ed3698be626a17017422bf7bcec08f9cda3192c0c36b3912` | |
| `0248/SUMPRODUCT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,971 | `9aabd9bd44a25c86b53b584908aba818bb377080c81265b844f1d5e3d4bc1ba3` | |
| `0248/SWITCH.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,573 | `31ad714231dbe9dcbfdd68b9dbb10112ac540362b51d112c4c34f03bc36b6649` | |
| `0248/TAN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,032 | `068fc53e0d43fa3b7a26377167887d3bbe25afbf55a69df179cadfcac2d3e551` | |
| `0248/TEXTBEFORE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,627 | `4ea592dfc7935dd3c13bc721c1f1800af30a15117a9cf10b2d32795b5b657ed6` | |
| `0248/TIME.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,361 | `7300c482552b72f50cc8ff5148b81b361dc8a1902cde062e2da67f2374203f48` | |
| `0248/TRUNC.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,602 | `87651fc05b724555a6a1c82ccd1c21019044f4638e32e7a45fd25c64fc8885d5` | |
| `0248/VALUE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,591 | `e8504824f783a94335fec1aa8bcee04c6ca5dc937fce6650924ddee9ed30a425` | |
| `0248/VAR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,598 | `ffe25f6963e31c1598243cdef7da8a99cd1c8bc9aea39de1a96289fa7ea511e4` | |
| `0248/WEEKDAY.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,609 | `5c110084c01133139b7e77358d15372ba6e10566f7d7b23d460d907171a9684a` | |
| `0248/WEEKNUM.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,715 | `ae1a42701c6a139c6ba08cbe7ee99b53c6630ddc41b6a2b847afe0c5c65bf695` | |
| `0248/WORKDAY.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,236 | `16e2322ebd855e5bd65393a341671c7d6386ec5fc436d336bd6cb3a2091003f1` | |
| `0248/XOR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,062 | `2ad8c6aef7633605186d1b980ec09946e74d2ecffb51ae1d93f3fc81d5e481ba` | |
| `0249/comment.pages` | [0249: A comment](../experiments/0249-comment.md) | 90,582 | `5d4fba777858429ebdc8d1346f121567eae763fea92463b5c0ede3d09db3a6e2` | names its author |
| `0250/border.pages` | [0250: A border on a shape](../experiments/0250-shape-border.md) | 92,690 | `e3a7c932d98aa3eb40dddc5b766e02ad57476978f315c0c66502bf44d9aecdf6` | |
| `0251/shadow.pages` | [0251: A shadow on a shape](../experiments/0251-shape-shadow.md) | 92,837 | `c889beb9716426f413a08944e617650123807279941676a0356ad0cd147c65bf` | |
| `0252/double.pages` | [0252: Double line spacing](../experiments/0252-line-spacing.md) | 90,415 | `d07d2ae268549c3c6794dac6cf17ceeb3929b486e60a52ffa52c5963070238ce` | |
| `0253/indents.pages` | [0253: Indents](../experiments/0253-indents.md) | 90,361 | `04e568200f23ec13746dca11021c9209221f99eb24e7fd8a9e17a9266157f807` | |
| `0254/two-columns.pages` | [0254: Two columns](../experiments/0254-columns.md) | 90,377 | `6734ca1f9182e8e32aa341519aa882c917988d3d724db7b1b069f392350d3bc5` | |
| `0255/tab-stop.pages` | [0255: A tab stop](../experiments/0255-tab-stop.md) | 90,409 | `aba6791d8dfe4e3b1e4746ce9f0b6fff171dfce718ad37ca03b4807f5a86c465` | |
| `0256/spacing.pages` | [0256: Space before and after a paragraph](../experiments/0256-paragraph-spacing.md) | 90,414 | `84336b3d7efc423c0f8f91c3bc3202c6a651d83d28ba1400095a07bf0fd30ad2` | |
| `0258/filter.numbers` | [0258: A filter](../experiments/0258-filter.md) | 101,831 | `af1efcd55da08324c4e63bde2ea166001c7d9440c47509ab728fcb220f9b764e` | |
| `0259/highlight.numbers` | [0259: Conditional highlighting](../experiments/0259-conditional-highlighting.md) | 140,220 | `92adee3afad6131393013c3e77656ad82a57caddfe8913b82aa3f1ea4e78891c` | |
| `0260/gradient.pages` | [0260: A gradient fill](../experiments/0260-gradient-fill.md) | 93,600 | `6122e8d9e9e0fb67a19d72fd2169117fda575f46047d1516e2c88c4d51d11566` | |
| `0261/drop-cap.pages` | [0261: A drop cap](../experiments/0261-drop-cap.md) | 91,348 | `305c79cd38226a3607b527cb8b6f54ad52780011bab04e26d04cfebab597f093` | |
| `0262/border.pages` | [0262: A paragraph border](../experiments/0262-paragraph-border.md) | 92,285 | `cdfecb2aeea41f079005617b8682cda23012e3b04b700c164de043db450e8a84` | |
| `0265/MINUTT.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 137,637 | `b76d77bd4cc319d51db4fbb57b050a60d7f5f46429581b40b093464334801c70` | |
| `0265/SUMMER.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 138,693 | `c345042c39fd24469cb8250658f9f50b8e5554113f81f9f1f9c4faa1694681b9` | |
| `0265/TID.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 138,267 | `b3502c21ecc9eb91b01feb3f6ce65735adbbc7b9ca841c148867bac8ee8974e0` | |
| `0265/TIMEVALUE.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 138,746 | `12531c3d851908ab9b15ffdc5f233f6deac75d6c9a2b1b9367b753ce914d6c3c` | |
| `0268/accepted.pages` | [0268: An accepted deletion](../experiments/0268-accepted-deletion.md) | 90,369 | `be53058be2314e609985bcf35f97b3828b713a69eef4597a992fb6a689dafacf` | names its author |
| `0269/rejected.pages` | [0269: A rejected insertion, and where tracking is turned on](../experiments/0269-rejected-insertion.md) | 90,360 | `19bd52003c7aa16d0171fcff1e513883bc6852065b408442127289b091d2fd45` | names its author |
| `0270/paused.pages` | [0270: Paused change tracking](../experiments/0270-paused-tracking.md) | 90,337 | `f0654702e180ebe16b0a8f032a940a8b11345be30a0083f0feebc8c274b1388d` | |
| `0270/tracking.pages` | [0270: Paused change tracking](../experiments/0270-paused-tracking.md) | 90,343 | `18e582bc7cb4f92c7140ab61c51ef5901ea380428ac846ef92f7a57f96479b08` | |
| `0273/all-edges.pages` | [0273: Which edges a paragraph border is on](../experiments/0273-border-edges.md) | 94,069 | `99d0a72394850a5a1a79cc0f5101cd4e5ca35f05e43d0b28e370663fbd1b4b6d` | |
| `0273/bottom-border.pages` | [0273: Which edges a paragraph border is on](../experiments/0273-border-edges.md) | 92,225 | `b80521959d39cef269c1033d67a706fd48cfd500602a21bfc20d3a0dd827ef57` | |
| `0274/dashed.pages` | [0274: A dashed border](../experiments/0274-dashed-border.md) | 95,709 | `93fd0722949837a282462118cb09c4a5e58adda6a4c135b55429e82483474700` | |
| `0275/radial.pages` | [0275: A radial gradient](../experiments/0275-radial-gradient.md) | 93,792 | `cb289716fed95f7790409b1006168a205b28569f719f59b1f8b68d355c604841` | |
| `0276/exactly.pages` | [0276: Exact line spacing](../experiments/0276-exact-line-spacing.md) | 90,397 | `8925dc6523d6d23bc5ec56b79233eecf12216ca5cc24b1be4371399a39a95068` | |
| `0277/right-tab.pages` | [0277: A right-aligned tab with a leader](../experiments/0277-right-tab.md) | 90,398 | `9ca4e7cff371899f6dbbd1e1fa68b7057b93cfe7c67fa1d57f1ff2371c6c053e` | |
| `0278/shadow-0.pages` | [0278: The shadow angle](../experiments/0278-shadow-angle.md) | 92,761 | `1e3a51340423e401dfaaeda72229bc977149f40f09b2af86fe61acd45930945d` | |
| `0278/shadow-45.pages` | [0278: The shadow angle](../experiments/0278-shadow-angle.md) | 92,814 | `15220012bea23db281d2ad7ae4e939594ad3b988a7e5cad9aa7f6721a34c7b70` | |
| `0279/average.numbers` | [0279: A pivot table that averages](../experiments/0279-pivot-average.md) | 153,044 | `111775ae8704e4a5c0bd2687e97cd8fd749ae2eb985acc7d74a3a8444121b017` | |
| `0279/sum.numbers` | [0279: A pivot table that averages](../experiments/0279-pivot-average.md) | 153,069 | `0645ae445578c670e9e654316fdec72ac55b4a92e87db17eb5782311f25ab785` | |
| `0280/two-rules.numbers` | [0280: Two highlighting rules](../experiments/0280-two-highlighting-rules.md) | 140,622 | `eb65578db3ebce92b3f3ed5acb71187649a5c68781d0435cb953e5cd60265c12` | |
| `0281/at-least.pages` | [0281: The other line spacing kinds](../experiments/0281-other-line-spacing-kinds.md) | 90,410 | `76ce92369f3d1f702de83566ec54d262cc8b55dee60d7db65c63844708be9b14` | |
| `0281/between.pages` | [0281: The other line spacing kinds](../experiments/0281-other-line-spacing-kinds.md) | 90,416 | `efcc428b850fe682657cbf2f1746edb1c8e9ebb45a04310d1f70924970f15003` | |
| `0282/centre-decimal.pages` | [0282: Centre and decimal tabs](../experiments/0282-centre-and-decimal-tabs.md) | 90,437 | `009c43f13f61da1a7679197b68197eefa22f280037a61c76aef650a6b6d87749` | |
| `0283/advanced-linear.pages` | [0283: An advanced linear gradient](../experiments/0283-advanced-linear-gradient.md) | 93,610 | `c3b968014e0a437d904585a39210471ea8865cbea8c9d764fa71788a9764c351` | |
| `0284/adjusted.pages` | [0284: Image adjustments](../experiments/0284-image-adjustments.md) | 94,686 | `42f06e68e685c72b827079aefb783aff87de2b97e6ea1b8b6a5fce3e5eef253c` | |
| `0285/no-background.pages` | [0285: A removed background](../experiments/0285-removed-background.md) | 93,074 | `948890228070b0395ab20285e14ce71a162ae1bab5c72cc7045f052442bd77ca` | |
| `0286/yellow-section.pages` | [0286: A section background](../experiments/0286-section-background.md) | 90,859 | `10ee2be005cf9df298a1535414fe3ea44b760947fe5824520fde188a29ee14e4` | |
| `0287/original.pages` | [0287: Rewriting a document](../experiments/0287-rewriting-a-document.md) | 90,350 | `da66cf898fa6788c5b738678f53d6180ab8f798467657badde5fb6c39a9f0bb0` | |
| `0287/resaved.pages` | [0287: Rewriting a document](../experiments/0287-rewriting-a-document.md) | 90,356 | `bb4d890eb1474279eeb39e8029b5768bc3aed8a8dc48b28945a92d05d06502f0` | |
| `0287/rewritten.pages` | [0287: Rewriting a document](../experiments/0287-rewriting-a-document.md) | 394,958 | `e818d55dfb043cfb5fed4497f2a030c6649bb41305241f23ca59034dfd9a48f1` | |
| `0288/hello-resaved.pages` | [0288: Writing new text](../experiments/0288-writing-new-text.md) | 91,855 | `df82cd76f9ed70a8617f55d692e606d62af4504782fad228ce99f5a59bbab3be` | |
| `0288/hello.pages` | [0288: Writing new text](../experiments/0288-writing-new-text.md) | 378,544 | `2c9f19010d7ea40641d369991657df648f896dea1a5280b28b1dd19f48725a44` | |
| `0289/with-run-resaved.pages` | [0289: Writing two paragraphs](../experiments/0289-writing-two-paragraphs.md) | 90,587 | `f397baa2e25b22dfb438d099280cf03834c0d872e6f7a8df92febe5a52bdb6c3` | |
| `0289/with-run.pages` | [0289: Writing two paragraphs](../experiments/0289-writing-two-paragraphs.md) | 80,281 | `49c3ad99419f7afe126e2e871e4ba3760875322d7523e51a712d3e3eda6d52f6` | |
| `0289/without-run-resaved.pages` | [0289: Writing two paragraphs](../experiments/0289-writing-two-paragraphs.md) | 90,776 | `c58501977456601cc6946f7e04d704b0e5a15b687ab50398a8098d8278cd1b10` | |
| `0289/without-run.pages` | [0289: Writing two paragraphs](../experiments/0289-writing-two-paragraphs.md) | 80,277 | `25d00d08b34b983dac28cbf5b3593a01218efdf0c62ebfdfd66bdecaa6a3672b` | |
| `0290/forty-two.numbers` | [0290: Writing a cell](../experiments/0290-writing-a-cell.md) | 86,733 | `182e18ee4185bf04cbfa8a3d2b81c1ebda98960bf1185cd4dc416a203767f10d` | |
| `0295/baseline.key` | [0295: A chart's title, legend, border and caption](../experiments/0295-chart-options.md) | 904,185 | `27a8cd0ff48f7f79557066f4a1fb33bf223d745953c10cf6d8a0c62836ee7699` | |
| `0295/border.key` | [0295: A chart's title, legend, border and caption](../experiments/0295-chart-options.md) | 915,879 | `add0935a376777fb0f877dd15f612da59fd78621ceee010391bc7bce0e58520d` | |
| `0295/caption.key` | [0295: A chart's title, legend, border and caption](../experiments/0295-chart-options.md) | 914,239 | `fd7a5d05c7fe008fa183fa40504f4668b6bbf431888a99115d1756b199aa0f0e` | |
| `0295/legend.key` | [0295: A chart's title, legend, border and caption](../experiments/0295-chart-options.md) | 915,844 | `68c6066a904f9cf4a08c11a43034843b5a93aba2ad0d30dd95376aefc075d455` | |
| `0295/title.key` | [0295: A chart's title, legend, border and caption](../experiments/0295-chart-options.md) | 915,586 | `6620bc1d477a7e117a945f59e4e252fcbecae88ec2ab271400ee95f0892a177c` | |
| `0296/axis-line.key` | [0296: A chart's value axis](../experiments/0296-chart-axis.md) | 914,552 | `38573dc480398ee19ed5747b4afaa171eae6f493ac36ea9fbb93f12a65e65bad` | |
| `0296/axis-title.key` | [0296: A chart's value axis](../experiments/0296-chart-axis.md) | 915,757 | `33b53cafe7e4e82a4bfa78f033fcb3ff5d6e277e0aa96381160b27499299bffa` | |
| `0296/baseline.key` | [0296: A chart's value axis](../experiments/0296-chart-axis.md) | 904,201 | `a595c00777b5da2f922d7efd0241ca7e46e3994814a45107dc0553b0576c080e` | |
| `0296/no-minimum.key` | [0296: A chart's value axis](../experiments/0296-chart-axis.md) | 913,663 | `a0effc2b98d684a70239f8deadab5e2d22d60300ae215ca5e68f38242d9c41c5` | |
| `0297/baseline.key` | [0297: A chart's category axis, series and text styles](../experiments/0297-chart-category-axis.md) | 904,185 | `a988fbe07c49f066e7d72b277110f27eb0fab4d0581d76be07ffad1fcf4e4438` | |
| `0297/x-axis-name.key` | [0297: A chart's category axis, series and text styles](../experiments/0297-chart-category-axis.md) | 916,680 | `56eda796b2caec1d481116c9d9d5eac31d3cc8914dedd9317c4371534cb72950` | |
| `0298/baseline.key` | [0298: Writing a chart's title and legend switches](../experiments/0298-writing-chart-switches.md) | 904,185 | `a988fbe07c49f066e7d72b277110f27eb0fab4d0581d76be07ffad1fcf4e4438` | |
| `0298/resaved.key` | [0298: Writing a chart's title and legend switches](../experiments/0298-writing-chart-switches.md) | 941,996 | `e3ada5af9e241f713d5dd5f48c4a18ef7ad19bc8bc22b9e4856c08a0a906ae6f` | |
| `0298/written.key` | [0298: Writing a chart's title and legend switches](../experiments/0298-writing-chart-switches.md) | 1,242,314 | `6071f10a9cdcb85c143b5421b6edf594f71c92d94917e22a29025955586cc31e` | |
| `0299/resaved.key` | [0299: Writing a skipped slide](../experiments/0299-writing-a-skipped-slide.md) | 919,847 | `e6706f9934453960afa1ab28932ef530ad7ee43cc675bc1678d86ee658f17638` | |
| `0299/second-skipped.key` | [0299: Writing a skipped slide](../experiments/0299-writing-a-skipped-slide.md) | 1,225,780 | `c2b0716e7f892fe5981629b3e2a24a1fc0429e7fff5990d798027209070cb29d` | |
| `0299/two-slides.key` | [0299: Writing a skipped slide](../experiments/0299-writing-a-skipped-slide.md) | 887,226 | `bb870b75de92baf4860b48c35b4713e52dd7279b9ea646a78fa434972c37ce40` | |
| `0300/facing-resaved.pages` | [0300: Writing document settings](../experiments/0300-writing-document-settings.md) | 90,443 | `1a413fa685dc43febbb954d26457d062310dfffc770e93cc10ba8d485f541c05` | |
| `0300/facing.pages` | [0300: Writing document settings](../experiments/0300-writing-document-settings.md) | 395,046 | `20b96ac68f2d18f237fa88076e5e529aca7d9be840f966bacf099ee8bda61905` | |
| `0300/loop-play-resaved.key` | [0300: Writing document settings](../experiments/0300-writing-document-settings.md) | 913,884 | `724f6d0bb599fe8d9726a94d28710f7d050dc29b4ec0d3d349b56fbd0c7925f2` | |
| `0300/loop-play.key` | [0300: Writing document settings](../experiments/0300-writing-document-settings.md) | 1,223,065 | `48d2c9f08e54b9aacfcc87e509339e2c12dafb3acf58755f8d37fbb584180e0d` | |
| `0301/headers-resaved.numbers` | [0301: Writing a table's header and footer rows](../experiments/0301-writing-header-rows.md) | 144,035 | `98ca20893b9419fcaab293bad0762e384ca12befc9c804a09601160fe70fb105` | |
| `0301/headers.numbers` | [0301: Writing a table's header and footer rows](../experiments/0301-writing-header-rows.md) | 457,167 | `97a153b0ecb39621dd86845b52afc17dca74b3977238cb75a351ef2f2bc83db8` | |
| `0302/original.key` | [0302: Writing a slide transition](../experiments/0302-writing-a-transition.md) | 881,923 | `205b36b80cb7119bc73fbb6abb5d291bbd6b91c92630e22bb238cebb33ecf1e0` | |
| `0302/resaved.key` | [0302: Writing a slide transition](../experiments/0302-writing-a-transition.md) | 906,426 | `9cbda2b9fd6dc78e4a98a833023f02a9144fb3fc1c91d82aea8fa9468284dd59` | |
| `0302/written.key` | [0302: Writing a slide transition](../experiments/0302-writing-a-transition.md) | 1,219,408 | `9cfeeae54c44dc3b82cdc3a0a23263cdf0a61d1a3b069b5c2f8bcd8c991ad682` | |
| `0303/original.key` | [0303: Writing an object's position, size, rotation and lock](../experiments/0303-writing-geometry.md) | 882,859 | `e13a4d931b293e7ef2e59dda6c3d3b7362882866a1692a6d15b8af3d8f2b07d9` | |
| `0303/resaved.key` | [0303: Writing an object's position, size, rotation and lock](../experiments/0303-writing-geometry.md) | 915,898 | `16813ecb2fc03f241b183c1066ef10d38eff5672a92d42ccf608b403ce877092` | |
| `0303/written.key` | [0303: Writing an object's position, size, rotation and lock](../experiments/0303-writing-geometry.md) | 1,220,401 | `4ddaa07ccd1e4af856bf01eb043ba751e2084794b51027c513e375598d42a0a1` | |
| `0304/original.key` | [0304: Writing an image's opacity and reflection](../experiments/0304-writing-opacity-and-reflection.md) | 882,974 | `5ce9c8dd8cbadbb9acf0b50b755ea645775ec3ff539f3f559e28815e012b5667` | |
| `0304/resaved.key` | [0304: Writing an image's opacity and reflection](../experiments/0304-writing-opacity-and-reflection.md) | 909,047 | `d9d1d7b99511a04218886ae30ea22743bbd6fc84ada08336ce3053aec102a174` | |
| `0304/written.key` | [0304: Writing an image's opacity and reflection](../experiments/0304-writing-opacity-and-reflection.md) | 1,220,531 | `88f34afbeb4eacb501786c91ccd8dcc8cde5b1871dfc49841c9ff76dfb332171` | |
| `0305/original.key` | [0305: Writing presenter notes, and the kinds of text storage](../experiments/0305-writing-presenter-notes.md) | 882,091 | `ddcdf332262622a443d14e4e3333955bb9a1e89afe403d579200a0c75875d69a` | |
| `0305/resaved.key` | [0305: Writing presenter notes, and the kinds of text storage](../experiments/0305-writing-presenter-notes.md) | 906,431 | `a37a3414fcceccdf3bdf790f21eb0dabe374e3297c78b699909852c5f5e052c1` | |
| `0305/written.key` | [0305: Writing presenter notes, and the kinds of text storage](../experiments/0305-writing-presenter-notes.md) | 1,219,429 | `0f00da7c8412a26771765c6effbf4b29a649dff495599e314448c99f97d80cee` | |
| `0306/original.numbers` | [0306: Writing a shared string](../experiments/0306-writing-a-shared-string.md) | 138,837 | `317c41bb605f4f3e2e492fdee400ab0f24f0989884239cee3a3f2ac7f2dcedd1` | |
| `0306/resaved.numbers` | [0306: Writing a shared string](../experiments/0306-writing-a-shared-string.md) | 144,646 | `2b5a535c31d5cefc84f864d3a1788c0db7d3fc19668ed57a78414f4ee1640f66` | |
| `0306/written.numbers` | [0306: Writing a shared string](../experiments/0306-writing-a-shared-string.md) | 457,170 | `1e22fdf91d05b01fe9598fa2e0b879d9a5ef5c39e5c0397862a4ef928b59ffe5` | |
| `0307/original.numbers` | [0307: Writing a cell format](../experiments/0307-writing-a-format.md) | 138,837 | `317c41bb605f4f3e2e492fdee400ab0f24f0989884239cee3a3f2ac7f2dcedd1` | |
| `0307/percent.numbers` | [0307: Writing a cell format](../experiments/0307-writing-a-format.md) | 457,165 | `f825c2e527c0517c05b0d51ded23c0c16aecbdf71d218465d9fc22c33330d9fe` | |
| `0307/resaved.numbers` | [0307: Writing a cell format](../experiments/0307-writing-a-format.md) | 145,350 | `5aac3448ed429690a3e9c6b3658e58230c86ee40fb717395f8459ce132e3220e` | |
| `0308/original.numbers` | [0308: Writing a row height and a column width](../experiments/0308-writing-row-and-column-sizes.md) | 135,040 | `d41c756a8fc71b9b1133607c781001eb3365d4689c75704b4e76250c0cf8ee78` | |
| `0308/resaved.numbers` | [0308: Writing a row height and a column width](../experiments/0308-writing-row-and-column-sizes.md) | 136,984 | `ba046d6f4efb3d737fc3e6a708f9fad4503567cda1bc93e3f27f461414f88d8e` | |
| `0308/written.numbers` | [0308: Writing a row height and a column width](../experiments/0308-writing-row-and-column-sizes.md) | 448,554 | `52613e7adc99473c7177924422c67166667f731c9fb3d6ed91b35a3c020d25b3` | |
| `0309/original.numbers` | [0309: Writing a cell's background colour, and the colour space](../experiments/0309-writing-a-cell-colour.md) | 140,026 | `b39d1a189e492ad89d612925030e408d60cf2ebdd151073aaedbf338d620a1f1` | |
| `0309/resaved.numbers` | [0309: Writing a cell's background colour, and the colour space](../experiments/0309-writing-a-cell-colour.md) | 141,040 | `6a4853b57aa2c4868d398f73aac422b8d3ea91c4908be407d7b9717e352d5982` | |
| `0309/written.numbers` | [0309: Writing a cell's background colour, and the colour space](../experiments/0309-writing-a-cell-colour.md) | 454,114 | `c7092d023d08ae51002c1867231783d0944533eff5ce36dc2361c59908a7a376` | |
| `0310/only46-resaved.numbers` | [0310: Writing a cell's font, size and text colour](../experiments/0310-writing-a-cell-text-style.md) | 141,206 | `ed31427a66d6b10b1586494e1c03deb86c325ce0502f7c6ff98a8a5db1bf3224` | |
| `0310/only46.numbers` | [0310: Writing a cell's font, size and text colour](../experiments/0310-writing-a-cell-text-style.md) | 454,114 | `aee9a6de79d8a674a360a26b624182ecaafb2a09bd99da1d9b699b2ba08f3138` | |
| `0310/original.numbers` | [0310: Writing a cell's font, size and text colour](../experiments/0310-writing-a-cell-text-style.md) | 140,026 | `b39d1a189e492ad89d612925030e408d60cf2ebdd151073aaedbf338d620a1f1` | |
| `0310/resaved.numbers` | [0310: Writing a cell's font, size and text colour](../experiments/0310-writing-a-cell-text-style.md) | 141,437 | `bb0bdc3fc6a5e550d3d682b6b5c4167bb0ea8061e47f0ad826ef41cea1127f8f` | |
| `0310/written.numbers` | [0310: Writing a cell's font, size and text colour](../experiments/0310-writing-a-cell-text-style.md) | 454,107 | `a45467dc8e183fdac068fe44c079d67dc0b8a363737eeb5a096ef643a0a05948` | |
| `0310/written2.numbers` | [0310: Writing a cell's font, size and text colour](../experiments/0310-writing-a-cell-text-style.md) | 454,107 | `c1025f0446433ccc7481861ebd3217f365b3469414ad05f74189f5535d1ba45e` | |
| `0311/original.pages` | [0311: Writing a paragraph style's character properties](../experiments/0311-writing-a-paragraph-style.md) | 90,438 | `96db185563729e8d065f4825fb7763535b54571fa59d55d6eb351c7000f43349` | |
| `0311/resaved.pages` | [0311: Writing a paragraph style's character properties](../experiments/0311-writing-a-paragraph-style.md) | 91,650 | `9d2a5bd3adec1255c1480242ca5d6ec194d5704bd4c9c229e38266ba424e988f` | |
| `0311/written.pages` | [0311: Writing a paragraph style's character properties](../experiments/0311-writing-a-paragraph-style.md) | 395,040 | `cd019b5eac6058d373a5605f0428facb8c19b0fdd66fc24439bf2f774a4e107b` | |
| `0312/original.key` | [0312: Writing a hidden body placeholder](../experiments/0312-writing-a-hidden-body.md) | 883,827 | `6652f65ac086803e925fbab1d4bf717811318407498444d20d45b8b4bd5c8520` | |
| `0312/resaved.key` | [0312: Writing a hidden body placeholder](../experiments/0312-writing-a-hidden-body.md) | 909,198 | `43ebc817433685ce90408467606613dddca5126870bc234ed9682b8f31e35424` | |
| `0312/written.key` | [0312: Writing a hidden body placeholder](../experiments/0312-writing-a-hidden-body.md) | 1,222,519 | `9c497d82c22f31e8e24452d6a7191d9f0be5d9789cb3b16faa42ecd810f730c8` | |
| `0313/center.numbers` | [0313: Writing a cell's alignment and text wrap](../experiments/0313-writing-alignment-and-wrap.md) | 137,605 | `7efaaed22f221ce69bda14a14d6d8046b0f66413f52d81eb66fad534fa7d79bf` | |
| `0313/nowrap.numbers` | [0313: Writing a cell's alignment and text wrap](../experiments/0313-writing-alignment-and-wrap.md) | 137,580 | `e1f92370a9a97cd50834cf74c0d004963cd5e91eb0be7ccd80c441d9cccfde5c` | |
| `0313/right-resaved.numbers` | [0313: Writing a cell's alignment and text wrap](../experiments/0313-writing-alignment-and-wrap.md) | 138,591 | `b192906a0209d79dc0223fa78574904847297224019fc5cf150a9e1786f92d39` | |
| `0313/right.numbers` | [0313: Writing a cell's alignment and text wrap](../experiments/0313-writing-alignment-and-wrap.md) | 451,287 | `a4eb99e1a10119d98ec2747b0511d5533182408719b9eaa79f8ad44648581f65` | |
| `0313/wrap-resaved.numbers` | [0313: Writing a cell's alignment and text wrap](../experiments/0313-writing-alignment-and-wrap.md) | 137,540 | `dc2223d909dd47879aa429d5f25228c2de696ef264f124c5744c75f85edfd616` | |
| `0313/wrap.numbers` | [0313: Writing a cell's alignment and text wrap](../experiments/0313-writing-alignment-and-wrap.md) | 451,260 | `f858a793ddb83ef048df802798a7a19196ef8679a8a59e8c08f2cd1b0293ff8c` | |
| `0314/original.key` | [0314: Writing the slide size](../experiments/0314-writing-slide-size.md) | 885,748 | `3e5e6327488684553880bebce619f933855b3727106f0e9f003c61b5c312a432` | |
| `0314/resaved.key` | [0314: Writing the slide size](../experiments/0314-writing-slide-size.md) | 920,956 | `87af52dd7f0f8717f1d3ae52d838f68c03f37386e93876d275bbbc1ad0701b6b` | |
| `0314/written.key` | [0314: Writing the slide size](../experiments/0314-writing-slide-size.md) | 1,223,065 | `b6c8cc834cbb39f5ec7610d41868c22dea59d2fe31e54e4d961dd934344173e4` | |
| `0315/original.numbers` | [0315: Writing the function a formula calls](../experiments/0315-writing-a-formula-function.md) | 137,776 | `14562a3797519df4171c2cac2a9dcf333d8137993ba69f001e539fb7256421a9` | |
| `0315/sum-resaved.numbers` | [0315: Writing the function a formula calls](../experiments/0315-writing-a-formula-function.md) | 137,847 | `03d3dd8c70c387a6e241c5f04d3ab6748ac53af301cf533977679a652c3b87a1` | |
| `0315/sum.numbers` | [0315: Writing the function a formula calls](../experiments/0315-writing-a-formula-function.md) | 451,676 | `719c427e716d6f4ae466d01e6b8bb7a26ae2286129375379c25a4c83f13847d0` | |
| `0317/original.key` | [0317: Writing a chart's data and type](../experiments/0317-writing-chart-data.md) | 904,185 | `a988fbe07c49f066e7d72b277110f27eb0fab4d0581d76be07ffad1fcf4e4438` | |
| `0317/written.key` | [0317: Writing a chart's data and type](../experiments/0317-writing-chart-data.md) | 1,242,311 | `d687cf3c82de2015d990d67260ab7ca51c11f0ba74881c97d2d84570231a305d` | |
| `0318/letter-resaved.pages` | [0318: Writing the paper size and a margin](../experiments/0318-writing-paper-size-and-margin.md) | 91,378 | `1fff3d52a6c59b794b0aaa863bbfa03fc5ee8b47bc0da48e833497e9a90d8c1c` | |
| `0318/letter.pages` | [0318: Writing the paper size and a margin](../experiments/0318-writing-paper-size-and-margin.md) | 395,046 | `4f89cd5c2cf7850a52c20dd32add8c81bc737cffe64f79a796b44d68c8909d8e` | |
| `0318/margin.pages` | [0318: Writing the paper size and a margin](../experiments/0318-writing-paper-size-and-margin.md) | 395,046 | `33e165393247d84af0cb4d048c453c6753c62811ad6824a9ed9e8759cd50c903` | |
| `0318/original.pages` | [0318: Writing the paper size and a margin](../experiments/0318-writing-paper-size-and-margin.md) | 90,438 | `96db185563729e8d065f4825fb7763535b54571fa59d55d6eb351c7000f43349` | |
| `0319/align-1.pages` | [0319: Writing paragraph alignment, measured on the page](../experiments/0319-writing-paragraph-alignment.md) | 395,168 | `ecc78535db6df8da12cb8646f1c819f79fb8c5a46a43f2d909f0f5ebbc10b9bf` | |
| `0319/align-2.pages` | [0319: Writing paragraph alignment, measured on the page](../experiments/0319-writing-paragraph-alignment.md) | 395,168 | `b3a420ca6cfa04ca082ea72df503af4074c1af46a2e732f189001595d31ef3d7` | |
| `0319/original.pages` | [0319: Writing paragraph alignment, measured on the page](../experiments/0319-writing-paragraph-alignment.md) | 90,565 | `bc1544ab1eee11cc1b5484a04196ca8203f879b5b90009c93e1b983f14bd52b8` | |
| `0320/first36.pages` | [0320: Writing indents, measured on the page](../experiments/0320-writing-indents.md) | 395,522 | `a194e18cbd24a837038cd89398144daf4bbb0753a4a53488a4a12ab20f570086` | |
| `0320/left72.pages` | [0320: Writing indents, measured on the page](../experiments/0320-writing-indents.md) | 395,522 | `08af3fa92aee3e4c33576da4c69bf969ae701373ad7790764bab7685f6fe33b3` | |
| `0320/long.pages` | [0320: Writing indents, measured on the page](../experiments/0320-writing-indents.md) | 395,522 | `8dfb480b9bc0f5fb24d280ad80ac82372b58df3d33ffc251e2aa6d744a5a7036` | |
| `0320/right72.pages` | [0320: Writing indents, measured on the page](../experiments/0320-writing-indents.md) | 395,522 | `f4f3bdd75e1c93b7a5a9a23b9e184a88d3e3b25700b3d42a8e2dc5ce0776b85a` | |
| `0321/after24.pages` | [0321: Writing paragraph and line spacing, measured on the page](../experiments/0321-writing-spacing.md) | 395,168 | `1c29776c0ca4098f58c6f4a2ae4352bd7361d5093e9f19cacd844ef0e178d77f` | |
| `0321/before24.pages` | [0321: Writing paragraph and line spacing, measured on the page](../experiments/0321-writing-spacing.md) | 395,168 | `514f62606151b38458e6fed44d7989142edaaef97229bd3ca6001c1b77ef6834` | |
| `0321/double.pages` | [0321: Writing paragraph and line spacing, measured on the page](../experiments/0321-writing-spacing.md) | 395,529 | `314be40228c0c20a6ea7e6e8193b76f765478ada31ba9810caea0ae5018e6b3f` | |
| `0321/exactly30.pages` | [0321: Writing paragraph and line spacing, measured on the page](../experiments/0321-writing-spacing.md) | 395,529 | `4f9335acc313eb87e85a64c087ff3c526116da9327f776ed45535d148281b999` | |
| `0321/long.pages` | [0321: Writing paragraph and line spacing, measured on the page](../experiments/0321-writing-spacing.md) | 395,522 | `8dfb480b9bc0f5fb24d280ad80ac82372b58df3d33ffc251e2aa6d744a5a7036` | |
| `0321/two.pages` | [0321: Writing paragraph and line spacing, measured on the page](../experiments/0321-writing-spacing.md) | 90,565 | `bc1544ab1eee11cc1b5484a04196ca8203f879b5b90009c93e1b983f14bd52b8` | |
| `0322/caps.pages` | [0322: Writing character properties, measured on the page](../experiments/0322-writing-character-properties.md) | 395,046 | `b7490b1562add5c6e077f2b55ae673ec0cae301ad11e5390550e2c50d264a6b8` | |
| `0322/long-shift10.pages` | [0322: Writing character properties, measured on the page](../experiments/0322-writing-character-properties.md) | 395,522 | `7cf22798e00bb17f9a135a42221b71471e16c067f65c1ed623decd7520b14b8c` | |
| `0322/original.pages` | [0322: Writing character properties, measured on the page](../experiments/0322-writing-character-properties.md) | 90,438 | `96db185563729e8d065f4825fb7763535b54571fa59d55d6eb351c7000f43349` | |
| `0322/shift10.pages` | [0322: Writing character properties, measured on the page](../experiments/0322-writing-character-properties.md) | 395,046 | `d746ec38b688be2e84bfd644d8e4cdc449ca16ce804f82de144cee445d3d0fe1` | |
| `0322/super.pages` | [0322: Writing character properties, measured on the page](../experiments/0322-writing-character-properties.md) | 395,046 | `bfe721c88e342e2576ffa3ab2f10b90dda3b75c80fe0836c0215210440c75cad` | |
| `0322/tracking.pages` | [0322: Writing character properties, measured on the page](../experiments/0322-writing-character-properties.md) | 395,046 | `8dd248582a61a1f8026ee66c3b2466c1699ab3821ec17fd90d3cc71253a73bcf` | |
| `0324/one.pages` | [0324: Writing text columns, measured on the page](../experiments/0324-writing-columns.md) | 395,522 | `8dfb480b9bc0f5fb24d280ad80ac82372b58df3d33ffc251e2aa6d744a5a7036` | |
| `0324/two.pages` | [0324: Writing text columns, measured on the page](../experiments/0324-writing-columns.md) | 395,533 | `55b6b0b103b18a38f4a909c8f6e3db161862dc87477acff3e936be88b42287c6` | |
| `0325/left200.pages` | [0325: Writing tab stops, measured on the page](../experiments/0325-writing-tab-stops.md) | 395,051 | `3c6755286508823c005a18abce3d12f5b678dbc92285a79c5949458a1811b36d` | |
| `0325/right200.pages` | [0325: Writing tab stops, measured on the page](../experiments/0325-writing-tab-stops.md) | 395,053 | `f5b96c974f546608e07d0e7c513ab5adafd8b76f42987caf5ae2aaec0e85e1a7` | |
| `0325/tab.pages` | [0325: Writing tab stops, measured on the page](../experiments/0325-writing-tab-stops.md) | 395,044 | `3bb284fd87065871b549c9e27b26b9d42cb9516eddde97824c9758b9d96c1e8f` | |
| `0326/long.pages` | [0326: Writing the top and right margins](../experiments/0326-writing-top-and-right-margins.md) | 395,522 | `8dfb480b9bc0f5fb24d280ad80ac82372b58df3d33ffc251e2aa6d744a5a7036` | |
| `0326/right150.pages` | [0326: Writing the top and right margins](../experiments/0326-writing-top-and-right-margins.md) | 395,522 | `48cc1c46b598d70121f19cc38150fdd21c71118ddcc8d655fa70acf48c56e17a` | |
| `0326/top150.pages` | [0326: Writing the top and right margins](../experiments/0326-writing-top-and-right-margins.md) | 395,522 | `380bc072d55e118332f994a895b6ff8cdc5e1798357f56f103eb0cd764fd0feb` | |
| `0327/header-off.pages` | [0327: Writing header and footer text](../experiments/0327-writing-headers-and-footers.md) | 395,065 | `a4e6d5ef1f8d14bf9db7b27c716b8aa8a3fe070c8f71373e65afbdb4c01b1b18` | |
| `0327/header.pages` | [0327: Writing header and footer text](../experiments/0327-writing-headers-and-footers.md) | 395,065 | `d98d83439b48599eb90d92ddb381bd5858f84c6ce6decf8d63db85d17ff0026a` | |
| `0328/background-resaved.pages` | [0328: Writing a section's page background](../experiments/0328-writing-a-page-background.md) | 90,830 | `c49934a24860cd85fccaa94fd52cc77a60763b987a81c655f6e28aed7444ccf6` | |
| `0328/background.pages` | [0328: Writing a section's page background](../experiments/0328-writing-a-page-background.md) | 395,073 | `b04a8530b99a265f28b75b0283588e6dd83d3b6a5ab0cd02f278a08e7608ecb8` | |
| `0329/space0.pages` | [0329: The colour space field](../experiments/0329-the-colour-space-field.md) | 395,075 | `6709c27f1d55f7863551838823c3d3c66a102de89962de2c9d4e90cda287ccd5` | |
| `0329/space1.pages` | [0329: The colour space field](../experiments/0329-the-colour-space-field.md) | 395,073 | `b04a8530b99a265f28b75b0283588e6dd83d3b6a5ab0cd02f278a08e7608ecb8` | |
| `0329/space2.pages` | [0329: The colour space field](../experiments/0329-the-colour-space-field.md) | 395,075 | `8c18509da926c1b79277032aae31bf220063d960c10d60692495540404b20b3e` | |
| `0329/space3.pages` | [0329: The colour space field](../experiments/0329-the-colour-space-field.md) | 395,075 | `20f3469fd5ad7b51178d8cda211b44eb43c721401b2008906d8691945a022a12` | |
| `0330/original.pages` | [0330: Writing a shape's fill and stroke, measured on the page](../experiments/0330-writing-a-shape-fill-and-stroke.md) | 92,690 | `e3a7c932d98aa3eb40dddc5b766e02ad57476978f315c0c66502bf44d9aecdf6` | |
| `0330/written.pages` | [0330: Writing a shape's fill and stroke, measured on the page](../experiments/0330-writing-a-shape-fill-and-stroke.md) | 397,686 | `929e81405653d94bca0657622b4dcb66181c74ce0a691b30b55fedbb3fd9c421` | |
| `0331/half.pages` | [0331: Writing a shape's opacity and shadow, measured on the page](../experiments/0331-writing-opacity-and-shadow.md) | 397,691 | `b6d373ba656436be070de721d631f77e890d43ede30610195b74a0dbd63090ac` | |
| `0331/shadow.pages` | [0331: Writing a shape's opacity and shadow, measured on the page](../experiments/0331-writing-opacity-and-shadow.md) | 397,735 | `83bc917d3d3a22df8d9accdf14428f0d862222f73977c561b5291a02510d1139` | |
| `0332/dashed-resaved.pages` | [0332: Writing a dash pattern, measured on the page](../experiments/0332-writing-a-dash-pattern.md) | 94,702 | `05d9e5aa5a1de64cef52a96142e7cccd8e878c7f19d51c7fc113b7b7ce426d1d` | |
| `0332/dashed.pages` | [0332: Writing a dash pattern, measured on the page](../experiments/0332-writing-a-dash-pattern.md) | 397,658 | `93589261f85e90d5ae8cedf85155bb09d1d22ab59c510b0e4752e047affcd2f2` | |
| `0333/moved.pages` | [0333: Writing a point of a shape's path, measured on the page](../experiments/0333-writing-a-path-point.md) | 397,250 | `061b7c2cb58632fd07501b6497543fb9fa4ea853ff3dbd2b532bdd88caa7fc47` | |
| `0333/original.pages` | [0333: Writing a point of a shape's path, measured on the page](../experiments/0333-writing-a-path-point.md) | 92,412 | `de99366e91bc2f0d79452dce9356273f1f52eb4efc396644eb076415a3d8a81d` | |
| `0334/dash.pages` | [0334: Writing a list's marker and indent, measured on the page](../experiments/0334-writing-list-markers.md) | 91,627 | `54f31a3f97489b075cba0c55ce65d13f4f8471e7dbf38f07bc4838869c520ddd` | |
| `0334/guillemet.pages` | [0334: Writing a list's marker and indent, measured on the page](../experiments/0334-writing-list-markers.md) | 396,218 | `a7e93ff23f2febc8be6bdb8456f531503ccfa16acb56d7eec89f11f45e2883a6` | |
| `0334/indent72.pages` | [0334: Writing a list's marker and indent, measured on the page](../experiments/0334-writing-list-markers.md) | 396,209 | `48deb47877d6fb80e4d518e286eea29dd162ceb16a568d6b37552c28c02820b7` | |
| `0334/none.pages` | [0334: Writing a list's marker and indent, measured on the page](../experiments/0334-writing-list-markers.md) | 396,209 | `f56d6552007c6029c13e993655e712f566449aacb960eeb120996f8e78f62eaf` | |
| `0335/six.pages` | [0335: Writing a drop cap's height, measured on the page](../experiments/0335-writing-a-drop-cap.md) | 395,964 | `440c0bf1ee7b362ec867c83e2f94a748b78155fa464c63f30d8262d185345d62` | |
| `0335/three.pages` | [0335: Writing a drop cap's height, measured on the page](../experiments/0335-writing-a-drop-cap.md) | 91,348 | `305c79cd38226a3607b527cb8b6f54ad52780011bab04e26d04cfebab597f093` | |
| `0336/new-all.pages` | [0336: Writing a paragraph border's edges, measured on the page](../experiments/0336-writing-paragraph-borders.md) | 397,012 | `a88b646e478e38b333f013683ba407ed42d05bda070a7d1a0ccb66208b7bd2fb` | |
| `0336/new-bottom.pages` | [0336: Writing a paragraph border's edges, measured on the page](../experiments/0336-writing-paragraph-borders.md) | 397,012 | `3be4380fcbc107aebe85c91722d7c7c61270839ebd1b749d9052c9273bc944be` | |
| `0336/old-all.pages` | [0336: Writing a paragraph border's edges, measured on the page](../experiments/0336-writing-paragraph-borders.md) | 397,012 | `c9e9cd3d4b970ba5507b93ce9c09f848e69dd810c914cea2c811c9780fc7d65b` | |
| `0336/old-bottom.pages` | [0336: Writing a paragraph border's edges, measured on the page](../experiments/0336-writing-paragraph-borders.md) | 397,012 | `18651471be587d0232543605cb56026d071fd243ad438b297292de1a25706e34` | |
| `0336/original.pages` | [0336: Writing a paragraph border's edges, measured on the page](../experiments/0336-writing-paragraph-borders.md) | 92,285 | `cdfecb2aeea41f079005617b8682cda23012e3b04b700c164de043db450e8a84` | |
| `0337/original.numbers` | [0337: Writing a date cell](../experiments/0337-writing-a-date.md) | 140,344 | `210c030fea871ee90dabd9a49c30461927f5244a89e3cd56d28fc9daea5913ce` | |
| `0337/resaved.numbers` | [0337: Writing a date cell](../experiments/0337-writing-a-date.md) | 141,515 | `326790cbf66ae208e25bab800d89d6bd1be46da95363ada2e889f67cc6a54f11` | |
| `0337/written.numbers` | [0337: Writing a date cell](../experiments/0337-writing-a-date.md) | 454,309 | `c6734f85a8588a4c9234de248c5558f8917b0587620197fc2d29de0df4db8911` | |
| `0338/original.numbers` | [0338: Writing a checkbox cell](../experiments/0338-writing-a-checkbox.md) | 140,093 | `4a5b5a9b878da0dd896460f709162467287af1e5c76866a429c97f717e2d5f50` | |
| `0338/unchecked.numbers` | [0338: Writing a checkbox cell](../experiments/0338-writing-a-checkbox.md) | 454,015 | `b1912bf9fff16f9dc5610a6a5552c2c71824eb13ea13209e814deb09e061535d` | |
| `0339/original.numbers` | [0339: Writing a currency format](../experiments/0339-writing-a-currency-format.md) | 140,344 | `210c030fea871ee90dabd9a49c30461927f5244a89e3cd56d28fc9daea5913ce` | |
| `0339/places0.numbers` | [0339: Writing a currency format](../experiments/0339-writing-a-currency-format.md) | 454,309 | `4e9a862fa87473b8bca88bf3db97199a4958df2fcbdc2e7b26325b31c1d4d785` | |
| `0339/usd.numbers` | [0339: Writing a currency format](../experiments/0339-writing-a-currency-format.md) | 454,309 | `4769f5fe7eb6c481bfa1eff15bee68f95bc18e71ccea3bbdcd0a0cadaaa14bb7` | |
| `0340/original.numbers` | [0340: Writing a date format's pattern](../experiments/0340-writing-a-date-pattern.md) | 140,344 | `210c030fea871ee90dabd9a49c30461927f5244a89e3cd56d28fc9daea5913ce` | |
| `0340/pattern.numbers` | [0340: Writing a date format's pattern](../experiments/0340-writing-a-date-pattern.md) | 454,318 | `b2cb09bcdace688833bef3b9d65d563a1b9668d26c0342b4fc96ecaaf3a92d47` | |
| `0341/original.numbers` | [0341: Writing a format's decimal places](../experiments/0341-writing-decimal-places.md) | 140,344 | `210c030fea871ee90dabd9a49c30461927f5244a89e3cd56d28fc9daea5913ce` | |
| `0341/pct-f4.numbers` | [0341: Writing a format's decimal places](../experiments/0341-writing-decimal-places.md) | 454,309 | `9077b0843eebdc7c2238fd9c16fde60806139201669b67559ad7445e6f77706d` | |
| `0341/pct-f5.numbers` | [0341: Writing a format's decimal places](../experiments/0341-writing-decimal-places.md) | 454,309 | `1178bb8ce770dd7da22fb2d1d1e29ac12118a9a3165d3c371abe07177906480a` | |
| `0341/pct2.numbers` | [0341: Writing a format's decimal places](../experiments/0341-writing-decimal-places.md) | 454,308 | `c7439de95a2a810d3081482aa3c6c72a13cf5ba93e456d491fe3852a4b8d2be2` | |
| `0342/f4.numbers` | [0342: Writing a negative number, and the format's negative style and thousands separator](../experiments/0342-negative-numbers-and-thousands.md) | 457,165 | `189f60e1478a4f591c05ccb7c3c7bac32362693854ee10fefe2fee775877bcdc` | |
| `0342/f5-2.numbers` | [0342: Writing a negative number, and the format's negative style and thousands separator](../experiments/0342-negative-numbers-and-thousands.md) | 457,165 | `c6d34bc54702eba70a1c2c9d3c5917c54fd743ad4b585fbdb3f0aabd8a032094` | |
| `0342/f5.numbers` | [0342: Writing a negative number, and the format's negative style and thousands separator](../experiments/0342-negative-numbers-and-thousands.md) | 457,165 | `ebbe653e88330beeceefb11c684f0d0535fdd271ea484f52f2b59fa9ccc58cb0` | |
| `0342/negative.numbers` | [0342: Writing a negative number, and the format's negative style and thousands separator](../experiments/0342-negative-numbers-and-thousands.md) | 457,165 | `c207a26718210505dcbc049065a9e7cc2d813fec19a490aa7c1c262213a147e8` | |
| `0343/neg0.numbers` | [0343: The negative-number styles](../experiments/0343-negative-number-styles.md) | 457,165 | `c207a26718210505dcbc049065a9e7cc2d813fec19a490aa7c1c262213a147e8` | |
| `0343/neg1.numbers` | [0343: The negative-number styles](../experiments/0343-negative-number-styles.md) | 457,165 | `189f60e1478a4f591c05ccb7c3c7bac32362693854ee10fefe2fee775877bcdc` | |
| `0343/neg2.numbers` | [0343: The negative-number styles](../experiments/0343-negative-number-styles.md) | 457,165 | `6246f7728a8af80fd1ea62180cb9e22a9cbc2a67a7d59ef6ed9394258eb53c43` | |
| `0343/neg3.numbers` | [0343: The negative-number styles](../experiments/0343-negative-number-styles.md) | 457,165 | `89804a1e5241e53d4696bd9435788e4886cf03ac81888bfcbb2bcc5b3d2130c0` | |
| `0344/alternating.numbers` | [0344: Writing alternating row colours](../experiments/0344-writing-alternating-rows.md) | 457,167 | `984c8b35797ce69daea3dbd6d7e5447eb95a512585e613bad62fc678517b8987` | |
| `0344/plain.numbers` | [0344: Writing alternating row colours](../experiments/0344-writing-alternating-rows.md) | 138,837 | `317c41bb605f4f3e2e492fdee400ab0f24f0989884239cee3a3f2ac7f2dcedd1` | |
| `0345/no-hlines.numbers` | [0345: Writing a table's gridlines and name visibility](../experiments/0345-writing-gridlines-and-title.md) | 457,168 | `1640c05219353050cbbe091dfca2516e8f4e5534da3748b15814dccc26375c48` | |
| `0345/no-title.numbers` | [0345: Writing a table's gridlines and name visibility](../experiments/0345-writing-gridlines-and-title.md) | 457,165 | `40e73e19183bb5eca67a04c3d6c54715eda0ce44c94673c2bda53fafea7e5872` | |
| `0345/plain.numbers` | [0345: Writing a table's gridlines and name visibility](../experiments/0345-writing-gridlines-and-title.md) | 138,837 | `317c41bb605f4f3e2e492fdee400ab0f24f0989884239cee3a3f2ac7f2dcedd1` | |
| `0346/original.key` | [0346: Writing a slide's background colour](../experiments/0346-writing-a-slide-background.md) | 885,748 | `3e5e6327488684553880bebce619f933855b3727106f0e9f003c61b5c312a432` | |
| `0346/written.key` | [0346: Writing a slide's background colour](../experiments/0346-writing-a-slide-background.md) | 1,223,065 | `31b49e4d6abf1c1656a021aea437dff4c83743b305f94e4d9a348783f74bd48c` | |
| `0348/both.pages` | [0348: Writing an image's size, measured on the page](../experiments/0348-writing-an-image-size.md) | 395,956 | `2c83a516678d3a43b30c173e83c96471087b643950e6980effa723362a6269d7` | |
| `0348/field4-only.pages` | [0348: Writing an image's size, measured on the page](../experiments/0348-writing-an-image-size.md) | 395,956 | `23e493c2e897000f8d44e2805a095a3ebb8ed262ee137115e2976402568ea152` | |
| `0348/geometry-only.pages` | [0348: Writing an image's size, measured on the page](../experiments/0348-writing-an-image-size.md) | 395,956 | `ba681d58b17ee6574d3a4e382335e027cc4d7b72aaa0a2ff555aaa29d9cf0250` | |
| `0348/original.pages` | [0348: Writing an image's size, measured on the page](../experiments/0348-writing-an-image-size.md) | 91,240 | `8276979523a753a81dbe06c6e792abe0f549bad808593d5967cf7370e43f6b7a` | |
| `0349/original.pages` | [0349: Writing a text box's text](../experiments/0349-writing-text-in-a-box.md) | 91,269 | `95c51f646f50ce78a409199397d74727297afdeb122c5ffed0be0d92c49f7112` | |
| `0349/written.pages` | [0349: Writing a text box's text](../experiments/0349-writing-text-in-a-box.md) | 396,101 | `ed4e12a7a1526269be8ba0ad8f144ab39f9eabbc75f9cec059ceb0f609c89254` | |
| `0350/column.key` | [0350: Writing a chart's grouping](../experiments/0350-writing-chart-grouping.md) | 1,242,311 | `d1e02ab3e8ecb8271f44cd4b797dbbdeba49ff1172bc5829b20c1ad136edf1ce` | |
| `0350/row.key` | [0350: Writing a chart's grouping](../experiments/0350-writing-chart-grouping.md) | 904,185 | `a988fbe07c49f066e7d72b277110f27eb0fab4d0581d76be07ffad1fcf4e4438` | |
| `0351/bold-resaved.pages` | [0351: Writing a character style run](../experiments/0351-writing-a-character-run.md) | 90,886 | `b6c93b41cc6cd48574d879bc27be33d2bf0f925ebe559ae2a4c5f51e65105fc6` | |
| `0351/bold.pages` | [0351: Writing a character style run](../experiments/0351-writing-a-character-run.md) | 395,067 | `2ede30db53c8cb46c9e66101497a5ead795347df809118b9f07885fc58b6ef48` | |
| `0351/plain.pages` | [0351: Writing a character style run](../experiments/0351-writing-a-character-run.md) | 395,051 | `54d6064c55da12e7ae7c08cdbb0fd0f3392e7333fa2a09c8c7fbdca0612aa786` | |
| `0352/original.pages` | [0352: Writing paragraph style runs](../experiments/0352-writing-paragraph-style-runs.md) | 90,565 | `bc1544ab1eee11cc1b5484a04196ca8203f879b5b90009c93e1b983f14bd52b8` | |
| `0352/title.pages` | [0352: Writing paragraph style runs](../experiments/0352-writing-paragraph-style-runs.md) | 395,174 | `6a1e1701e2c9d778fa3d0913700b30f5a71261e78f49e1ce8c19019dd5fe0097` | |
| `0353/list-resaved.pages` | [0353: Writing a list](../experiments/0353-writing-a-list.md) | 90,725 | `edf106d85ec5653b855253e8ae4c0c7cdb26acb258c3640bf27cdbd3a48265b7` | |
| `0353/list.pages` | [0353: Writing a list](../experiments/0353-writing-a-list.md) | 395,178 | `82749a9553f1268ed4a0505f0d21baedc98577bc542a7de57d5dc0a98cdb3513` | |
| `0353/original.pages` | [0353: Writing a list](../experiments/0353-writing-a-list.md) | 90,565 | `bc1544ab1eee11cc1b5484a04196ca8203f879b5b90009c93e1b983f14bd52b8` | |
| `0354/original.pages` | [0354: Writing a link's address](../experiments/0354-writing-a-link.md) | 90,396 | `7c28df6d409974c61f6c1d96486b812670906a77ebd1f3b83b74c15ea27e9f23` | |
| `0354/written.pages` | [0354: Writing a link's address](../experiments/0354-writing-a-link.md) | 395,031 | `5fb0d3546f263a6257fc12f8692d7ebf2a32e332188bc1ca21954d1959d19526` | |
| `0355/email.pages` | [0355: Writing email and phone links](../experiments/0355-writing-email-and-phone-links.md) | 395,026 | `6bf00d61e7155407423fe73dd81b5b177b41553077d8b926bfffd5f26ecea96c` | |
| `0355/phone.pages` | [0355: Writing email and phone links](../experiments/0355-writing-email-and-phone-links.md) | 395,017 | `528f758b68abd9b8b9523943519719355cd6967257f17971a580ce6e9f2e9f1b` | |
| `0356/original.pages` | [0356: Writing a footnote's text](../experiments/0356-writing-a-footnote.md) | 91,544 | `0ba243a9fa8cda7d9a681b4877c64d2e0efed1579e6f645162652d0536d162bf` | |
| `0356/written.pages` | [0356: Writing a footnote's text](../experiments/0356-writing-a-footnote.md) | 396,320 | `d5605a2489d1ae89dcb2719496bbce4bef75f2806358532c1fb21926262499a5` | |
| `0357/date.pages` | [0357: Writing a date field](../experiments/0357-writing-a-date-field.md) | 397,578 | `62b16c5e8c1d943766dc950c6a3ae41de2ba2717ad57d71db0bf9e43156d6858` | |
| `0357/f5.pages` | [0357: Writing a date field](../experiments/0357-writing-a-date-field.md) | 397,574 | `6e0fdea62a74665ca0f294ee0493bd938b74fdc5300beb20db5e89d5c411d230` | |
| `0357/f6.pages` | [0357: Writing a date field](../experiments/0357-writing-a-date-field.md) | 397,574 | `a66e0ad2b9247b5e887a5b26b74cb114825d3209e21073b8177a71ab7479c06d` | |
| `0357/f7.pages` | [0357: Writing a date field](../experiments/0357-writing-a-date-field.md) | 397,574 | `b0df2880ac871ec8f90e048f8d70b677d635b2231f1879a76e8c2ab94391ecaf` | |
| `0357/original.pages` | [0357: Writing a date field](../experiments/0357-writing-a-date-field.md) | 92,940 | `430659fab08556c8fc151734402e46f2ab93e04ee0017cb6699c715e9d43358c` | |
| `0357/pattern.pages` | [0357: Writing a date field](../experiments/0357-writing-a-date-field.md) | 397,574 | `a5986d7f4dc8cf0902c54d617049eb77640e39f47d02bdeb0f2c57642cf7337f` | |
| `0358/lower-alpha.pages` | [0358: Writing a page number's format](../experiments/0358-writing-a-page-number-format.md) | 395,379 | `3fce5407e07a7b4f0ea4d7b3dda6fdac4db8d5d4711fdd5018527f17d100cda2` | |
| `0358/lower-alphabetic.pages` | [0358: Writing a page number's format](../experiments/0358-writing-a-page-number-format.md) | 395,384 | `514cacc281a6c3945900c8a2b4247277fe436d7dfab5255f806d9281af093081` | |
| `0358/lower-latin.pages` | [0358: Writing a page number's format](../experiments/0358-writing-a-page-number-format.md) | 395,379 | `20bd87f1166f19109fc05531a7df3cb450a4b5cedb1ebe62089cb7167d9ddac4` | |
| `0358/lower-roman.pages` | [0358: Writing a page number's format](../experiments/0358-writing-a-page-number-format.md) | 395,379 | `1df6ce1b453454fbe91bc869f890fff2416c159e3cef96f64c00a9b2c7b65009` | |
| `0358/original.pages` | [0358: Writing a page number's format](../experiments/0358-writing-a-page-number-format.md) | 90,756 | `8f4a98ae31e23af1758c6c29e9a7e461d7089158dade032145f83240ad3e35a2` | |
| `0358/upper-alpha.pages` | [0358: Writing a page number's format](../experiments/0358-writing-a-page-number-format.md) | 395,379 | `28aef7a8c51b0948cb6202674aa42dee89a87535abf668667db35655f959232d` | |
| `0358/upper-alphabetic.pages` | [0358: Writing a page number's format](../experiments/0358-writing-a-page-number-format.md) | 395,384 | `5704366e1558b982a881b7c37850c47c33e02372c2690ca0258d076e7a8c9733` | |
| `0358/upper-latin.pages` | [0358: Writing a page number's format](../experiments/0358-writing-a-page-number-format.md) | 395,379 | `03dc457b51674d1dff2b081eaefec9a197d9b9daa5b684197f8ae58f7a1e0494` | |
| `0358/upper-letter.pages` | [0358: Writing a page number's format](../experiments/0358-writing-a-page-number-format.md) | 395,380 | `8a6671fb37ad7dad553f415ab298707f3c58f3d502d45067bb3da012fabba301` | |
| `0358/upper-roman.pages` | [0358: Writing a page number's format](../experiments/0358-writing-a-page-number-format.md) | 395,379 | `1f18ab5f6da6b60647c730d594de1ceae2fccffb903da245983a0158799bf5c7` | |
| `0359/count.pages` | [0359: Writing a page break and a page count](../experiments/0359-writing-a-page-break-and-page-count.md) | 395,387 | `5752ab86b7b533f0ed9528350849bb2d2ff25e3e61cd0a7c4cd43060113959a0` | |
| `0359/two-pages.pages` | [0359: Writing a page break and a page count](../experiments/0359-writing-a-page-break-and-page-count.md) | 395,387 | `cbb09bb7322f7b38aebf624dc18a7b9646a1775166ac70465d0386f0dd99b7df` | |
| `0360/column-break.pages` | [0360: Writing a line break and a column break](../experiments/0360-writing-line-and-column-breaks.md) | 395,076 | `63f9a09d1d385dc2c2179ba7018665021c1b23d71ea0053244175c825000b199` | |
| `0360/line-break.pages` | [0360: Writing a line break and a column break](../experiments/0360-writing-line-and-column-breaks.md) | 395,065 | `57a317c43771143cd676acd3ffc5c58a0b733b7ce556c345f59bc606ab020afd` | |
| `0361/char-only-resaved.pages` | [0361: Writing a section break](../experiments/0361-writing-a-section-break.md) | 91,360 | `09e5fb9e194f9d7085e71ec624cf5f054b7ef0e24bffeabaf623df63aed77455` | |
| `0361/char-only.pages` | [0361: Writing a section break](../experiments/0361-writing-a-section-break.md) | 395,053 | `861507eb6630ba2c98da8841c5112ee6f3e7fceb607ffbf685c3c66fa01b6bcf` | |
| `0361/with-run-resaved.pages` | [0361: Writing a section break](../experiments/0361-writing-a-section-break.md) | 90,377 | `1b9ebbda2da77ae6a137f88ee93bd70cf0debe15ee55086c1013544a46f1914d` | |
| `0361/with-run.pages` | [0361: Writing a section break](../experiments/0361-writing-a-section-break.md) | 395,063 | `6bc283b79c7ad704ae747d000bd92b9051acc560dfdbf45597efd3b3da4ccdb6` | |
| `0362/both.pages` | [0362: Writing first-page headers](../experiments/0362-writing-first-page-headers.md) | 395,087 | `b463e4e5404c375ed834ff8f4d5d82e0f406b9ae0fa9271f72db4f5b714f4dc3` | |
| `0362/field-18.pages` | [0362: Writing first-page headers](../experiments/0362-writing-first-page-headers.md) | 395,087 | `baed1f9937f18ad07322d2e70d0566e06e2fc04097814ba77d8583c8d71d7e92` | |
| `0362/field-20.pages` | [0362: Writing first-page headers](../experiments/0362-writing-first-page-headers.md) | 395,087 | `43681e7f2925a5e59309110e6f210e5780f12af26d7fb7af0f4e2e7b751aa72d` | |
| `0362/field-21.pages` | [0362: Writing first-page headers](../experiments/0362-writing-first-page-headers.md) | 395,087 | `aa09786cda64480fd5b0f69df7a31a8441d9589381240f35f7a62971eeef3d9d` | |
| `0362/hide-first.pages` | [0362: Writing first-page headers](../experiments/0362-writing-first-page-headers.md) | 395,087 | `6f28995fd4c97b6ef2359ce325e1062ca1d7ad5e21f12e51395e2b373cfcbb03` | |
| `0364/five-by-four-resaved.numbers` | [0364: Writing names and a table's size](../experiments/0364-writing-names-and-table-size.md) | 112,821 | `3b89b264fe14d92f7c6c62af3beaec9728e5b5e366181c22f5e5e13195e1bbe9` | |
| `0364/five-by-four.numbers` | [0364: Writing names and a table's size](../experiments/0364-writing-names-and-table-size.md) | 456,626 | `ec079457be0a54b0007c5445bc45a16284ddb862f4c90faaf9a570b2e4b97606` | |
| `0364/lists-only.numbers` | [0364: Writing names and a table's size](../experiments/0364-writing-names-and-table-size.md) | 456,626 | `d2624761f549f78186b956bcd58e2f62d1fdee0d9cd9bfbbd13d7315f200471e` | |
| `0364/more-rows.numbers` | [0364: Writing names and a table's size](../experiments/0364-writing-names-and-table-size.md) | 457,165 | `e794109e939026e9f0e465b80a5896c33ed2850a6f4cca244d692983508f4040` | |
| `0364/names.numbers` | [0364: Writing names and a table's size](../experiments/0364-writing-names-and-table-size.md) | 457,163 | `6cb7464b5efb539ce8f0496a4c6b6176454d39d60ccda1b8048b9267a8795f81` | |
| `0365/thirty-by-nine-resaved.numbers` | [0365: Growing a table](../experiments/0365-growing-a-table.md) | 152,294 | `92e5587c9f04c64675e40e4fdd35f8b72acc0a9d8babe4fc8a58df634cb0bd21` | |
| `0365/thirty-by-nine.numbers` | [0365: Growing a table](../experiments/0365-growing-a-table.md) | 457,434 | `d62beb0a4f1949f3d62adbde64b6fe77e1c908337791af696127c5dafca79dde` | |
| `0366/base.pages` | [0366: Writing the bottom margin and the header and footer distances](../experiments/0366-writing-bottom-margin-and-header-distances.md) | 395,532 | `393ca00f2488e07ac4bdda0958df72f0ead2c56366c32741448b54fc39092163` | |
| `0366/bottom-200.pages` | [0366: Writing the bottom margin and the header and footer distances](../experiments/0366-writing-bottom-margin-and-header-distances.md) | 395,532 | `fb8eb7947a71951168b3fb4c5e20be067d0fe27bdc7c10c0603f66979817e903` | |
| `0366/footer-72.pages` | [0366: Writing the bottom margin and the header and footer distances](../experiments/0366-writing-bottom-margin-and-header-distances.md) | 395,532 | `2812b1d2c03d8c410f0c20e50fbca0b1844430c0ea885d43c564483d0094aa3e` | |
| `0366/header-72.pages` | [0366: Writing the bottom margin and the header and footer distances](../experiments/0366-writing-bottom-margin-and-header-distances.md) | 395,532 | `ea2027d86f9f8ae4247b1568c068d83b199bb249c753a73fe95164b396017a46` | |
| `0367/both-resaved.pages` | [0367: Writing the orientation](../experiments/0367-writing-orientation.md) | 84,968 | `0fa8d312d8552ee7d35ca8d697ecb8c5679f6b3063d0129c6ada110f1f183c5d` | |
| `0367/both.pages` | [0367: Writing the orientation](../experiments/0367-writing-orientation.md) | 395,046 | `5f7c3bb9c4435589c4dd9c886036b2e2d607ad230f56778f53c663ed55355741` | |
| `0367/flag-only-resaved.pages` | [0367: Writing the orientation](../experiments/0367-writing-orientation.md) | 90,443 | `bd50cb5cffbb5e72cffa5be79e15256c39abe6b13f66c9482c9b25cbcb97f534` | |
| `0367/flag-only.pages` | [0367: Writing the orientation](../experiments/0367-writing-orientation.md) | 395,046 | `f55d233f0694c25414dd91aa351b177f315df2b946c1d26252bc10fc336e927b` | |
| `0367/swap-only-resaved.pages` | [0367: Writing the orientation](../experiments/0367-writing-orientation.md) | 84,968 | `6b1642a4433894925fe47bbe452f213c5f907c4c09ac65c7c1a1dfa76c04d255` | |
| `0367/swap-only.pages` | [0367: Writing the orientation](../experiments/0367-writing-orientation.md) | 395,046 | `d6522a336d48ee6238ddfa201aa66f60186f9734316b7a732784e1c5e0804026` | |
| `0369/nbsp.pages` | [0369: Writing a tab and a non-breaking space](../experiments/0369-writing-a-tab-and-a-non-breaking-space.md) | 395,283 | `9b16819ac56ec5a613a645d40813883760889b7201d4eba86ccaa7d2a39230b5` | |
| `0369/no-tab.pages` | [0369: Writing a tab and a non-breaking space](../experiments/0369-writing-a-tab-and-a-non-breaking-space.md) | 395,052 | `fdd99619502ed8776cb1942a262791e005c7d576b841f5065bc9724fe8055463` | |
| `0369/spaces.pages` | [0369: Writing a tab and a non-breaking space](../experiments/0369-writing-a-tab-and-a-non-breaking-space.md) | 395,282 | `f07e955e11e0e6f33436a83a4ba9075b5eb0e4aaa13620894f55ffedf66fdea9` | |
| `0369/tab.pages` | [0369: Writing a tab and a non-breaking space](../experiments/0369-writing-a-tab-and-a-non-breaking-space.md) | 395,052 | `593a06305dc3191ad1fa1db0effb7b9c19af150153e26afc3e55a1883437bb37` | |
| `0370/b-only.numbers` | [0370: Writing a formula's range](../experiments/0370-writing-a-formula-range.md) | 451,675 | `c414f097a7813b96da413d9b17429498619036714b81a1aa09b967b0b4bd3f61` | |
| `0370/b-to-c-rows.numbers` | [0370: Writing a formula's range](../experiments/0370-writing-a-formula-range.md) | 451,677 | `0a53bdc7eb9f59dfe36aa18076efe659019e4f2f1c7ca47a4221a36c625f131e` | |
| `0370/c-only.numbers` | [0370: Writing a formula's range](../experiments/0370-writing-a-formula-range.md) | 451,675 | `caf8eb04040826f37e5bcbf877da0248314b0efeebed98564bc92f4c29234549` | |
| `0371/abs-c.numbers` | [0371: Writing a cell reference](../experiments/0371-writing-a-cell-reference.md) | 451,511 | `0c4b9fe473e325fa7cf9f92398a2a6499cd04723b78002a1684ba379e99c417f` | |
| `0371/all-absolute.numbers` | [0371: Writing a cell reference](../experiments/0371-writing-a-cell-reference.md) | 451,511 | `c7ca936410b5e7a3430973b62506b09a6ac845715461bd411b89659591e7396f` | |
| `0371/all-relative.numbers` | [0371: Writing a cell reference](../experiments/0371-writing-a-cell-reference.md) | 451,511 | `1acc297129bfcaf1e1e22e6b3dfe7640a459888c660cf1f9b21c1878e9c823bd` | |
| `0371/rel-c.numbers` | [0371: Writing a cell reference](../experiments/0371-writing-a-cell-reference.md) | 451,511 | `a17c275925a0682595fae38121f103c9ef077f6646d9cd3bbd393e9b99c915a2` | |
| `0372/group-moved.pages` | [0372: Writing a group's position and a member's offset](../experiments/0372-writing-a-group.md) | 400,915 | `365a2e6c3cf27f308b27695bed74b7f6ade5e4bd5e56deeed171893eb3fe8a6e` | |
| `0372/member.pages` | [0372: Writing a group's position and a member's offset](../experiments/0372-writing-a-group.md) | 400,915 | `2f7039c794850ecb3b505670404ea56458f1dab6e6e2d2a9b9b4971e025b801d` | |
| `0373/flipped-180.pages` | [0373: Writing a flip](../experiments/0373-writing-a-flip.md) | 397,250 | `0ece61a09aeea4f88b7d95db596e9685e6c7d01486a6cb6431759b391cb877eb` | |
| `0373/flipped.pages` | [0373: Writing a flip](../experiments/0373-writing-a-flip.md) | 397,250 | `0446e26ccbf5e4f1a9fc76e90e54b1ae203c23a6c1225b02d4f78bf59ff9cd33` | |
| `0373/original.pages` | [0373: Writing a flip](../experiments/0373-writing-a-flip.md) | 397,250 | `061b7c2cb58632fd07501b6497543fb9fa4ea853ff3dbd2b532bdd88caa7fc47` | |
| `0373/rotated-180.pages` | [0373: Writing a flip](../experiments/0373-writing-a-flip.md) | 397,250 | `3b7757c4390cc8668ae91fc057fd660eec08bb92d47b281c1badb281e0e37b23` | |
| `0374/both.pages` | [0374: Writing a caption's and a title's text](../experiments/0374-writing-a-caption-and-title.md) | 401,052 | `532a592b74a4119a67aacf1d7ff07c24ffdc901a4be7e7b3de4aca8902df30c3` | |
| `0374/caption.pages` | [0374: Writing a caption's and a title's text](../experiments/0374-writing-a-caption-and-title.md) | 401,037 | `5fff2ce667e3719e0ff2830f60a1ba226e75c49fc16cc0bbd3cf82eb4fd90123` | |
| `0374/original.pages` | [0374: Writing a caption's and a title's text](../experiments/0374-writing-a-caption-and-title.md) | 95,797 | `1e2d32b5862fca8695d33cdef37721474270d9924ff6b5ceb0839c7a0a46e6ba` | |
| `0374/title.pages` | [0374: Writing a caption's and a title's text](../experiments/0374-writing-a-caption-and-title.md) | 401,035 | `557bb2278f3e43cf3f5a846320600b8cd542488484ef108e7d76ec12cf360eb1` | |
| `0375/author.pages` | [0375: Writing a comment's text, time and author](../experiments/0375-writing-a-comment.md) | 395,207 | `554cb87545c4b93f8fdf5df15876bd06740e975bba3ba71f1313758ec3ac7882` | |
| `0375/text.pages` | [0375: Writing a comment's text, time and author](../experiments/0375-writing-a-comment.md) | 395,226 | `31703a6aab98da59ad88a798c8c492cbf4fb521bdbef814ec148aafa843d8b67` | names its author |
| `0375/time.pages` | [0375: Writing a comment's text, time and author](../experiments/0375-writing-a-comment.md) | 395,215 | `5034810ebdfd664fc08ae16c4c9825957bfbdd99066b8be7f34ab70040f3aef8` | names its author |
| `0376/comment-emptied.pages` | [0376: A highlight is a comment without text](../experiments/0376-highlight-and-comment.md) | 395,211 | `dd2734572dca5a3c765efc19d953b7d3a8b01fb66085946ad73fe987ddba1ff1` | names its author |
| `0376/comment.pages` | [0376: A highlight is a comment without text](../experiments/0376-highlight-and-comment.md) | 90,582 | `5d4fba777858429ebdc8d1346f121567eae763fea92463b5c0ede3d09db3a6e2` | names its author |
| `0376/highlight-with-text.pages` | [0376: A highlight is a comment without text](../experiments/0376-highlight-and-comment.md) | 395,228 | `2ca156f7376f38ce723ccffc037b0fe8dc92046a1438eba352fb5b17bef9ed6e` | names its author |
| `0376/highlight.pages` | [0376: A highlight is a comment without text](../experiments/0376-highlight-and-comment.md) | 90,590 | `ddacfc01c1f916ceee3ab1506b0f6fdb22cf49ca368a875260eee25db045d5fb` | names its author |
| `0377/deleted-as-insertion.pages` | [0377: Writing a tracked change's kind and its author's colour](../experiments/0377-writing-a-tracked-change.md) | 395,730 | `b677f5b556ab18e1fe9a0a8a9a65cab6d3b23f61022b0996c860ca6c598252d1` | names its author |
| `0377/deleted-blue.pages` | [0377: Writing a tracked change's kind and its author's colour](../experiments/0377-writing-a-tracked-change.md) | 395,730 | `79a66146fa5e68bd62fdd7a2f71b9398a2a1f277f2fceca26c8e6a794d4643e8` | names its author |
| `0377/deleted-green.pages` | [0377: Writing a tracked change's kind and its author's colour](../experiments/0377-writing-a-tracked-change.md) | 395,730 | `2ede5c7ebcfaa7d0d0eb27d753a1187fcf7ed084f358b9272f097cab4ac78911` | names its author |
| `0377/deleted-red.pages` | [0377: Writing a tracked change's kind and its author's colour](../experiments/0377-writing-a-tracked-change.md) | 395,730 | `f0f2e622354260a364c877a61fc7119dcd87848bb6015d2780f6df8115837204` | names its author |
| `0377/deleted.pages` | [0377: Writing a tracked change's kind and its author's colour](../experiments/0377-writing-a-tracked-change.md) | 90,932 | `eecbe112ce8fb4e10e1880f5dff21bde5d8261f12c29e14c3da67ee6f0cd9380` | names its author |
| `0377/inserted-as-deletion.pages` | [0377: Writing a tracked change's kind and its author's colour](../experiments/0377-writing-a-tracked-change.md) | 395,753 | `b6163179a43e485a88b3f186aec8edb2a57adec58db1f13ad5c0193c829d3685` | names its author |
| `0377/inserted.pages` | [0377: Writing a tracked change's kind and its author's colour](../experiments/0377-writing-a-tracked-change.md) | 90,954 | `8c091a38124ae34ba5e702d6fe1efd2fe7ea0f6c4ccb921f0ef75569751976ba` | names its author |
| `0378/original.key` | [0378: Writing the slide order](../experiments/0378-writing-slide-order.md) | 886,912 | `1e56d02d37f1b4ddc4cb0135f4695009337753f77782592d38f5a209e421f2a2` | |
| `0378/reversed.key` | [0378: Writing the slide order](../experiments/0378-writing-slide-order.md) | 1,226,786 | `ae02685aedc4493cb137e42fa435d455437d8898efe8223a9d0d8402e71c6f02` | |
| `0378/rotated.key` | [0378: Writing the slide order](../experiments/0378-writing-slide-order.md) | 1,226,786 | `3702c4103cd5440739ba56759cb6bee512b105e38b996ae3913f56aa152eb75c` | |
| `0378/two.key` | [0378: Writing the slide order](../experiments/0378-writing-slide-order.md) | 1,226,779 | `d98a68219278827ee9cbefacf06677d6612ff768a8459fcdf6f1c4de9df10316` | |
| `0379/blank.key` | [0379: Writing a slide's layout](../experiments/0379-writing-a-slide-layout.md) | 1,226,786 | `a4a75a821776ac6d96036bddd22b792929474ea4cef4614d1263d89ff0575917` | |
| `0379/original.key` | [0379: Writing a slide's layout](../experiments/0379-writing-a-slide-layout.md) | 886,912 | `1e56d02d37f1b4ddc4cb0135f4695009337753f77782592d38f5a209e421f2a2` | |
| `0379/picture.key` | [0379: Writing a slide's layout](../experiments/0379-writing-a-slide-layout.md) | 1,226,786 | `578535cb4ad4c4ce7dc4ac5e28eb345fcd27203e33eb12fc7607f5b14f8d7e94` | |
| `0379/rewritten.key` | [0379: Writing a slide's layout](../experiments/0379-writing-a-slide-layout.md) | 1,226,786 | `7a70949628c5e7e032b1fa8eef1d3a8621de0ef9fb05cda40d244c6152e2a611` | |
| `0379/same-as-c.key` | [0379: Writing a slide's layout](../experiments/0379-writing-a-slide-layout.md) | 1,226,786 | `9c849e492d6467ab98c8a6abe0ead17ebc341d89ea631680869408d8951fa6b5` | |
| `0380/both.key` | [0380: Writing auto restart and the idle time](../experiments/0380-writing-auto-restart-and-idle-time.md) | 1,226,786 | `ea25c36c8c1ea85cc8717b35c3f8bab3637bf63a827d3fe689f74c84f203227f` | |
| `0380/idle-150.key` | [0380: Writing auto restart and the idle time](../experiments/0380-writing-auto-restart-and-idle-time.md) | 1,226,786 | `d1037e65458aa3a566ed2129603e136219dab2ef3a85cc8dd238095e8355e90a` | |
| `0380/idle-179.key` | [0380: Writing auto restart and the idle time](../experiments/0380-writing-auto-restart-and-idle-time.md) | 1,226,786 | `cd625f9d1005b4cd2534181594729a1d84c398052a6fe664e0afd53a57a51433` | |
| `0380/idle-300.key` | [0380: Writing auto restart and the idle time](../experiments/0380-writing-auto-restart-and-idle-time.md) | 1,226,786 | `9ccd715ec1b4261b2016d3ab4a981db7ab9ef5ab2fcbb33d845b01334b61e7a4` | |
| `0380/idle-60.key` | [0380: Writing auto restart and the idle time](../experiments/0380-writing-auto-restart-and-idle-time.md) | 1,226,786 | `e57d85107ecf2200b4b8e600e416c76fc854f167c114143648c4802621caa8bd` | |
| `0380/original.key` | [0380: Writing auto restart and the idle time](../experiments/0380-writing-auto-restart-and-idle-time.md) | 886,912 | `1e56d02d37f1b4ddc4cb0135f4695009337753f77782592d38f5a209e421f2a2` | |
| `0380/restart.key` | [0380: Writing auto restart and the idle time](../experiments/0380-writing-auto-restart-and-idle-time.md) | 1,226,786 | `74cbafd5038f1cd22c0a703b4833cc96f319eccc35c7e45282184a19a5c30983` | |
| `0381/a-and-b-numbered.key` | [0381: Writing a slide number](../experiments/0381-writing-a-slide-number.md) | 1,226,786 | `fbf20535224cf6f1c3e6057269616965c9fc413c3986a3f894788950aae1787a` | |
| `0381/a-numbered-placeholder.key` | [0381: Writing a slide number](../experiments/0381-writing-a-slide-number.md) | 1,226,801 | `b50f39b3cd4abb69c56724db9e531222f64899f909844780e43e82dc9631fd5b` | |
| `0381/a-numbered.key` | [0381: Writing a slide number](../experiments/0381-writing-a-slide-number.md) | 1,226,786 | `57d4cfa56d5100fcc8acea5f544f9f1ef3ec0d80af1759d2cce8678f610e737a` | |
| `0381/a-placeholder.key` | [0381: Writing a slide number](../experiments/0381-writing-a-slide-number.md) | 1,226,801 | `646fd8c85c1c6b73342623c2f4cea54851884e60edc2151df740a35486c295e1` | |
| `0381/all-numbered.key` | [0381: Writing a slide number](../experiments/0381-writing-a-slide-number.md) | 1,226,786 | `98907d0fce7ce0c08121e6b720e786947f066950703c4d81d33ab3323823960e` | |
| `0381/original.key` | [0381: Writing a slide number](../experiments/0381-writing-a-slide-number.md) | 886,912 | `1e56d02d37f1b4ddc4cb0135f4695009337753f77782592d38f5a209e421f2a2` | |
| `0382/column-b.numbers` | [0382: Writing a merged range](../experiments/0382-writing-merged-cells.md) | 451,554 | `feafed3e2b3cc76a2aa472d96f7763fa1d80e1b2b428b79110f7fc20f1cb90ae` | |
| `0382/columns-c-d.numbers` | [0382: Writing a merged range](../experiments/0382-writing-merged-cells.md) | 451,556 | `7588f7513a39c7b16563c4860e9955c66bdf73f95670c00321c72cc375d34c84` | |
| `0382/original.numbers` | [0382: Writing a merged range](../experiments/0382-writing-merged-cells.md) | 137,614 | `3cbb3e1a2c668655b7355a22ef1e1d67ef7ac40d4c67d4afe0e90323601f4a85` | |
| `0382/rows-2-5.numbers` | [0382: Writing a merged range](../experiments/0382-writing-merged-cells.md) | 451,554 | `0b82c9ac8c0a1db859f7343eee2db0e12bbcbedbd94bd488d82a4a62db36f1d5` | |
| `0383/all-unhidden.numbers` | [0383: Writing a filter's value and its hidden rows](../experiments/0383-writing-a-filter.md) | 420,922 | `c882f255b20fe2fae80326e8136a3b1d4b31fb06c7c3b08fdf034faee31559a5` | |
| `0383/only-522-0.numbers` | [0383: Writing a filter's value and its hidden rows](../experiments/0383-writing-a-filter.md) | 420,922 | `0ea3ac8973569ee68e2dd1ed1038750685c2251b6b74c5260c24e3c47640e3e5` | |
| `0383/only-522-3.numbers` | [0383: Writing a filter's value and its hidden rows](../experiments/0383-writing-a-filter.md) | 420,922 | `e8bac385f49549b719f6d3440ef51fb92fd4c8dffe091307d57111ac1e8fa7b9` | |
| `0383/original-off.numbers` | [0383: Writing a filter's value and its hidden rows](../experiments/0383-writing-a-filter.md) | 139,382 | `333f00ad9a41a172d6d93c3f9806a02a45010c9b71cf4b293a0c0a2cd2bab5ed` | |
| `0383/original-toggled.numbers` | [0383: Writing a filter's value and its hidden rows](../experiments/0383-writing-a-filter.md) | 101,831 | `99afe4ade8666283baea20655767080feff3e99fdc3d03c9d106cb0c0ae7ce44` | |
| `0383/original.numbers` | [0383: Writing a filter's value and its hidden rows](../experiments/0383-writing-a-filter.md) | 101,831 | `af1efcd55da08324c4e63bde2ea166001c7d9440c47509ab728fcb220f9b764e` | |
| `0383/value-0-off.numbers` | [0383: Writing a filter's value and its hidden rows](../experiments/0383-writing-a-filter.md) | 144,632 | `b087bc37360c38607c019e1922febcacf9450f65718ead999242422b2fcb3d9d` | |
| `0383/value-0-toggled.numbers` | [0383: Writing a filter's value and its hidden rows](../experiments/0383-writing-a-filter.md) | 107,081 | `d6f5f165926ec4f6b4533c7ee8ddd0f769aef2ef9f3b1a84cb9e90aa805414f3` | |
| `0383/value-0.numbers` | [0383: Writing a filter's value and its hidden rows](../experiments/0383-writing-a-filter.md) | 420,922 | `6d70c7808f6eb96165cffc42eea6fb0310d4813ae97c71c0e625a3b44b780fdd` | |
| `0383/value-3-off.numbers` | [0383: Writing a filter's value and its hidden rows](../experiments/0383-writing-a-filter.md) | 144,633 | `7c83008c695fba542f2f1a03274f0f2e0e2ba10490a395524f1873dbd2bab5ef` | |
| `0383/value-3-toggled.numbers` | [0383: Writing a filter's value and its hidden rows](../experiments/0383-writing-a-filter.md) | 107,082 | `aeee94813f2cb0d437b573e4de021c18c725f0e9c382e00ac7ad42fc1816bf49` | |
| `0383/value-3.numbers` | [0383: Writing a filter's value and its hidden rows](../experiments/0383-writing-a-filter.md) | 420,922 | `fb8ffb566966450c0e0be24bf7d005d11f1c6ddab67f1be641308ae1e3ef0b2e` | |
| `0384/angle-0.pages` | [0384: Writing a gradient's stops and angle](../experiments/0384-writing-a-gradient.md) | 398,470 | `b865bec3388e28a98a38a90aa13a7c3d4bfac59a757a092a8db873b9011a3adf` | |
| `0384/original.pages` | [0384: Writing a gradient's stops and angle](../experiments/0384-writing-a-gradient.md) | 93,600 | `6122e8d9e9e0fb67a19d72fd2169117fda575f46047d1516e2c88c4d51d11566` | |
| `0384/radial.pages` | [0384: Writing a gradient's stops and angle](../experiments/0384-writing-a-gradient.md) | 398,470 | `a793bc73927a6b76a6487880354cf932e6ff978bf00643c03216eb5507975ebb` | |
| `0384/red-green.pages` | [0384: Writing a gradient's stops and angle](../experiments/0384-writing-a-gradient.md) | 398,470 | `c2cc28314d6df559bff4c4aa7c2bbe3ea173c3acb54280c8e11fbf0cf0c91e62` | |
| `0384/stops-moved.pages` | [0384: Writing a gradient's stops and angle](../experiments/0384-writing-a-gradient.md) | 398,470 | `d8e69bc8b58dc0952f531129e0e7bade9bc6f0cdacc9e990ec45d1de06bb976e` | |
| `0385/pages-radial.pages` | [0385: Writing a radial gradient's angle](../experiments/0385-writing-a-radial-gradient.md) | 93,792 | `cb289716fed95f7790409b1006168a205b28569f719f59b1f8b68d355c604841` | |
| `0385/radial-315.pages` | [0385: Writing a radial gradient's angle](../experiments/0385-writing-a-radial-gradient.md) | 398,470 | `619f4f8dd0c6d22b63d07765d91e54833425f121119ed44a3d9e4fc59cfd1c9d` | |
| `0385/radial-90.pages` | [0385: Writing a radial gradient's angle](../experiments/0385-writing-a-radial-gradient.md) | 398,470 | `fce604c474bbd81c6b461c97eccbd3e5272eadf4dcf0436ed8c1acd154e9024c` | |
| `0385/radial-advanced.pages` | [0385: Writing a radial gradient's angle](../experiments/0385-writing-a-radial-gradient.md) | 398,470 | `6d08f2841433967d9d2478020fb89a9cf6aee91bddb26ac286bdc04129d5c40d` | |
| `0385/written-radial.pages` | [0385: Writing a radial gradient's angle](../experiments/0385-writing-a-radial-gradient.md) | 398,470 | `a793bc73927a6b76a6487880354cf932e6ff978bf00643c03216eb5507975ebb` | |
| `0386/not-facing.pages` | [0386: Writing left and right pages](../experiments/0386-writing-left-and-right-pages.md) | 396,081 | `cc785e9a536c876f15f8f69557f6f49452dab4162b9d663d6ef8ce165de11450` | |
| `0386/original.pages` | [0386: Writing left and right pages](../experiments/0386-writing-left-and-right-pages.md) | 91,358 | `84006b7f5a65341814d7059bcb187e097fbf9f6fae51a40e4ea01ace1df76e16` | |
| `0386/same.pages` | [0386: Writing left and right pages](../experiments/0386-writing-left-and-right-pages.md) | 396,081 | `2be3b444cdf40920b3f44fd69bc1b8954bb158bcffba9a0bb317efc8cd2a7d69` | |
| `0387/both-own.pages` | [0387: Writing *same as previous section*](../experiments/0387-writing-same-as-previous-section.md) | 397,815 | `252cb840fad486582c6e7abfec4054b77dabbc0f90f8bdb4a3c563b4b523acbd` | |
| `0387/both.pages` | [0387: Writing *same as previous section*](../experiments/0387-writing-same-as-previous-section.md) | 397,815 | `e20d5fee34ff4a94ad44de9b94f4fb2bb036a1b1d346d90860a0bb586ecbccf0` | |
| `0387/first-only-own.pages` | [0387: Writing *same as previous section*](../experiments/0387-writing-same-as-previous-section.md) | 397,800 | `e9d7747a0bf1eb8651bae592f845c7814d8c5fd22bd54d6d377d18d4bb87c7f3` | |
| `0387/first-only.pages` | [0387: Writing *same as previous section*](../experiments/0387-writing-same-as-previous-section.md) | 397,800 | `c5df57390832da8d0ef0af4e9f07315ac9d977b7b51ede9d04e0f750b40f80b7` | |
| `0388/level-0.pages` | [0388: Writing a list level](../experiments/0388-writing-a-list-level.md) | 396,091 | `d35a513775a5091d89c75fb475f6e89afe38589c28378b9083d90df610c38526` | |
| `0388/level-2.pages` | [0388: Writing a list level](../experiments/0388-writing-a-list-level.md) | 396,091 | `27fa138ec0b23c6e0f1c176bcd6667efa718da662492380f5f6b0b76d2dcf37f` | |
| `0388/level-4.pages` | [0388: Writing a list level](../experiments/0388-writing-a-list-level.md) | 396,091 | `93a42838fc2adeee856ea79d85a91464adb0f52fc11015d7ca98f1b7c27edfee` | |
| `0388/original.pages` | [0388: Writing a list level](../experiments/0388-writing-a-list-level.md) | 91,508 | `d9a5f544cc549c2222849ac8a08b5c061692e2a539ed5ec94a09bb893433cf0b` | |
| `0389/both-renamed.pages` | [0389: Writing a bookmark and a link to it](../experiments/0389-writing-a-bookmark-link.md) | 395,492 | `0950df54354e95f98dc29e7afdfbd9dc7a1503d109099c1c17694418dc8bdf95` | |
| `0389/link-elsewhere.pages` | [0389: Writing a bookmark and a link to it](../experiments/0389-writing-a-bookmark-link.md) | 395,492 | `91101f28642389fdf0f77e87f2d828b27636585f10bc2b759735dc682e2c1acf` | |
| `0389/moved.pages` | [0389: Writing a bookmark and a link to it](../experiments/0389-writing-a-bookmark-link.md) | 395,492 | `811ae3bba79f42ee73b3b33f668d2f900316bedd0653cfe5b84b07680682ed35` | |
| `0389/original.pages` | [0389: Writing a bookmark and a link to it](../experiments/0389-writing-a-bookmark-link.md) | 90,821 | `241881ca339ca09787aceee9fe0a38ec0a4623bf88561521948910769f31fcdf` | |
| `0390/left.pages` | [0390: Writing an image mask's position and size](../experiments/0390-writing-an-image-mask.md) | 399,988 | `99444c3e6cb1bfeb6f80c8691daa8ecd95fab0c86ecc982068c50ec0525bb1db` | |
| `0390/natural-200.pages` | [0390: Writing an image mask's position and size](../experiments/0390-writing-an-image-mask.md) | 399,988 | `829e87af211956f80252af4bf985492df6ee7a4063e795ea8ed96f3acec06f4c` | |
| `0390/natural-50.pages` | [0390: Writing an image mask's position and size](../experiments/0390-writing-an-image-mask.md) | 399,988 | `f1dd591a718e36f729a556c19ecedaef4f2f0e6cbd66cab6cca0c92108d4d3e3` | |
| `0390/original.pages` | [0390: Writing an image mask's position and size](../experiments/0390-writing-an-image-mask.md) | 95,114 | `fc157925e2fc4640ce7ba4b30a7c7ddf721dcc1d8394885750f818faa00883eb` | |
| `0390/wide.pages` | [0390: Writing an image mask's position and size](../experiments/0390-writing-an-image-mask.md) | 399,988 | `3813f3778c8809544882d2dedb3f2fe74a2e4a6619b701d909c74d074565e058` | |
| `0391/b2-cached-match.numbers` | [0391: Writing the value of a highlighting rule and a filter](../experiments/0391-writing-a-rule-value.md) | 459,075 | `124faf912be42d1769d3b13f50e57732a0d522029f9c8681e18ce735c4482c9b` | |
| `0391/b5-cached-none.numbers` | [0391: Writing the value of a highlighting rule and a filter](../experiments/0391-writing-a-rule-value.md) | 459,075 | `488ed3cc7565ac347bbb47e47829468efbf5c9d82830b0fdba9e3e99efbd1e78` | |
| `0391/only-522-zero.numbers` | [0391: Writing the value of a highlighting rule and a filter](../experiments/0391-writing-a-rule-value.md) | 459,075 | `0511ab30b0b93dc7a537cb61910c24d9bd58c7556d4c3f5ab4b06dcb0d2ab5ca` | |
| `0391/only-522.numbers` | [0391: Writing the value of a highlighting rule and a filter](../experiments/0391-writing-a-rule-value.md) | 459,075 | `a56d5a58fc881e22bcf59dde5d4890f17fbc4a0a4555d01390ec4b47ddd4086a` | |
| `0391/original-edited.numbers` | [0391: Writing the value of a highlighting rule and a filter](../experiments/0391-writing-a-rule-value.md) | 140,483 | `67bf292c7f81819641fc18c15e4870d4d5ce8254a473d0fb514ecd50f304a376` | |
| `0391/original.numbers` | [0391: Writing the value of a highlighting rule and a filter](../experiments/0391-writing-a-rule-value.md) | 140,220 | `92adee3afad6131393013c3e77656ad82a57caddfe8913b82aa3f1ea4e78891c` | |
| `0391/rule-all-0-edited.numbers` | [0391: Writing the value of a highlighting rule and a filter](../experiments/0391-writing-a-rule-value.md) | 140,544 | `ed8daaf493b5a6bcdf14b3afed64bf640c32745af3c1aa00fb77cbd75fd7532e` | |
| `0391/rule-all-0.numbers` | [0391: Writing the value of a highlighting rule and a filter](../experiments/0391-writing-a-rule-value.md) | 459,075 | `c09f1f760e679ae224154690b9b2ad85e4b31be95499a8a3aa8a8706f45b717d` | |
| `0391/rule-all-3-and-522.numbers` | [0391: Writing the value of a highlighting rule and a filter](../experiments/0391-writing-a-rule-value.md) | 459,075 | `6d5a615c43fdc355aa091fd19071cb9279747905d69c30857098adaebb1df3ac` | |
| `0391/rule-all-3-edited.numbers` | [0391: Writing the value of a highlighting rule and a filter](../experiments/0391-writing-a-rule-value.md) | 140,547 | `e45f0de5050277befa292ac1addba65ad83544ab2937660320514b39eeff90eb` | |
| `0391/rule-all-3.numbers` | [0391: Writing the value of a highlighting rule and a filter](../experiments/0391-writing-a-rule-value.md) | 459,075 | `60c8d5c9094c543bc823905751ecebb0fcb389539073bc3e6f9eb80155dbd5bc` | |
| `0391/rule-formula-3.numbers` | [0391: Writing the value of a highlighting rule and a filter](../experiments/0391-writing-a-rule-value.md) | 459,075 | `62d48350c06924544e3649a63e2163302228e6a24c5f2b922711963e30c96803` | |
| `0391/rule-settings-3.numbers` | [0391: Writing the value of a highlighting rule and a filter](../experiments/0391-writing-a-rule-value.md) | 459,075 | `7e06a76d5d39e42fe5b56ff53d4933736ef8ace5cf3081855e69bf40a720b3a7` | |
| `0392/body-bold-emph-off.pages` | [0392: Writing an inherited and a cleared character property](../experiments/0392-writing-inherited-properties.md) | 395,067 | `5b445ef873dabb062827f07e29b659a08913bc35aad15bb921290a481b9cd06a` | |
| `0392/body-bold.pages` | [0392: Writing an inherited and a cleared character property](../experiments/0392-writing-inherited-properties.md) | 395,067 | `c5173f61464e1294788422e6d91c2298708c2a98fc24e9bbe5296f654ca62888` | |
| `0392/body-italic-emph-off.pages` | [0392: Writing an inherited and a cleared character property](../experiments/0392-writing-inherited-properties.md) | 395,069 | `0a9411d0bc93b7a0d2200d40ff599852285b917a772f01c4e13ce7e2cb7fe3a5` | |
| `0392/body-italic.pages` | [0392: Writing an inherited and a cleared character property](../experiments/0392-writing-inherited-properties.md) | 395,067 | `b4d960c1d7ed309398080435fe20e5b5e44e7b1ae712fc09ea9b15262b4e5ecf` | |
| `0392/original.pages` | [0392: Writing an inherited and a cleared character property](../experiments/0392-writing-inherited-properties.md) | 395,067 | `2ede30db53c8cb46c9e66101497a5ead795347df809118b9f07885fc58b6ef48` | |
| `0393/original.pages` | [0393: Writing an unnamed style's parent](../experiments/0393-writing-a-style-parent.md) | 91,218 | `5fa04c6cc124ad99db5c0475740b06ceb877fd7ac999601e0ed1c1c4a45e5e6d` | |
| `0393/parent-heading.pages` | [0393: Writing an unnamed style's parent](../experiments/0393-writing-a-style-parent.md) | 395,868 | `0845507410d7fbec52bfc255d19e1098ed238e8eb26e9f0a61f7eed83184d36a` | |
| `0393/parent-title.pages` | [0393: Writing an unnamed style's parent](../experiments/0393-writing-a-style-parent.md) | 395,868 | `f094e98cd0c988b3a2df68402ecfeb3c7141ce443f51cccba4fec5de353a2599` | |
| `0394/annotation-plain-listed.pages` | [0394: Renaming a part](../experiments/0394-renaming-a-part.md) | 94,567 | `d169abaf555bed78a87ffa50dd7515ac55afde5cdb6b1615cdb07001bbd3d187` | |
| `0394/annotation-plain.pages` | [0394: Renaming a part](../experiments/0394-renaming-a-part.md) | 90,302 | `b31d372d4efd8bbff94610782dda204aa37ea2fb58608266f379a3a7e4b25eff` | |
| `0394/document-numbered.pages` | [0394: Renaming a part](../experiments/0394-renaming-a-part.md) | 90,334 | `72b87ad327d66d00ec036156a4464e60d5ef32b503c0c8900318d02626d2114b` | |
| `0394/document-other.pages` | [0394: Renaming a part](../experiments/0394-renaming-a-part.md) | 90,312 | `2a3e01bfcf79e8ee69381169ea161df9c02c5491587b00dedf63dffce5be848c` | |
| `0394/document-zebra-listed.pages` | [0394: Renaming a part](../experiments/0394-renaming-a-part.md) | 94,617 | `1d986920247d24ad92c6b7c8590c66baa6b6bc0beb2663f5abff12f6f6ce1209` | |
| `0394/metadata-other.pages` | [0394: Renaming a part](../experiments/0394-renaming-a-part.md) | 90,312 | `259952389b54dc0bfafa31ef7cb8ff9f87b960bb85c3fb3ce35c8dbafd112607` | |
| `0394/metadata-renamed-only.pages` | [0394: Renaming a part](../experiments/0394-renaming-a-part.md) | 90,312 | `259952389b54dc0bfafa31ef7cb8ff9f87b960bb85c3fb3ce35c8dbafd112607` | |
| `0394/original.pages` | [0394: Renaming a part](../experiments/0394-renaming-a-part.md) | 90,438 | `96db185563729e8d065f4825fb7763535b54571fa59d55d6eb351c7000f43349` | |
| `0394/stylesheet-numbered.pages` | [0394: Renaming a part](../experiments/0394-renaming-a-part.md) | 90,324 | `c966e83a4489968f3ff0849eb50d3c365c247b3cd5c3d0d48701cbad073f8fa5` | |
| `0394/stylesheet-own-id.pages` | [0394: Renaming a part](../experiments/0394-renaming-a-part.md) | 90,334 | `d942379a653e7067fec4bfe21605b59b9af91c950c450b46c53207e4ad2fed35` | |
| `0394/viewstate-99-listed.pages` | [0394: Renaming a part](../experiments/0394-renaming-a-part.md) | 94,636 | `145b865909c98d736ec3dd3a62684dac73587f1075a0ee78f353628badf3a82a` | |
| `0394/viewstate-other.pages` | [0394: Renaming a part](../experiments/0394-renaming-a-part.md) | 90,324 | `86f37e26ed559a4584f10b15c71760a35eb1db60930078a97681ce8ec7a1643a` | |
| `0394/viewstate-own-id.pages` | [0394: Renaming a part](../experiments/0394-renaming-a-part.md) | 90,334 | `5757bba7e9fecb9b125f997dbfe018e17d630ab34f460971aac5bb4c2b3bc475` | |
| `0395/original-name.pages` | [0395: Renaming and replacing a data file](../experiments/0395-writing-a-data-file.md) | 95,431 | `18df798105fba565a7cba9a0eff21d192e6211fc3a19608531a84ce83ccfb906` | |
| `0395/original.pages` | [0395: Renaming and replacing a data file](../experiments/0395-writing-a-data-file.md) | 91,240 | `8276979523a753a81dbe06c6e792abe0f549bad808593d5967cf7370e43f6b7a` | |
| `0395/replaced.pages` | [0395: Renaming and replacing a data file](../experiments/0395-writing-a-data-file.md) | 95,429 | `d73d12cab12885eba8317b3472aa691e4802aa26eb5a3bcc75c8d706ad3942df` | |
| `0396/root-ver-900.pages` | [0396: Writing a record header's type, version and references](../experiments/0396-writing-record-headers.md) | 395,046 | `3d14c345f8735967f4a4bc834a8d684d98d3d324329cf7ea31669d4e776fab8b` | |
| `0396/text-refs-none.pages` | [0396: Writing a record header's type, version and references](../experiments/0396-writing-record-headers.md) | 395,032 | `4bb79cbd0810e3de3775769929432d53f3be0314d7e613c483bbeaba35d9a0c2` | |
| `0396/text-type-2022.pages` | [0396: Writing a record header's type, version and references](../experiments/0396-writing-record-headers.md) | 395,046 | `72e1da77576c2591be3f649bc997f584a12a9bc491ee35378c3cdb7ab384fba2` | |
| `0396/text-type-9999.pages` | [0396: Writing a record header's type, version and references](../experiments/0396-writing-record-headers.md) | 395,046 | `7d33574bea43cd9cb115555a2111274778a682526dfacbed89c3841d671c3aad` | |
| `0396/text-ver-000.pages` | [0396: Writing a record header's type, version and references](../experiments/0396-writing-record-headers.md) | 395,046 | `673ab3c0f43f682ad5da63117ea2815d33a333395906eb2364fa09ec5a7b431a` | |
| `0396/text-ver-106.pages` | [0396: Writing a record header's type, version and references](../experiments/0396-writing-record-headers.md) | 395,046 | `df49c3b595505fb2e92087563d4060066c49f951b2bb15c20cafa51d0d2d456a` | |
| `0396/text-ver-900.pages` | [0396: Writing a record header's type, version and references](../experiments/0396-writing-record-headers.md) | 395,046 | `4fd9879258d627e6905fc116c131265ac649e79a793154a50c1b6cde0f4c1912` | |
| `0396/text-ver-none.pages` | [0396: Writing a record header's type, version and references](../experiments/0396-writing-record-headers.md) | 395,041 | `7611e5afc3de01c9e2eaa2477461160aad3af1fa77dd1bca7ba79675eef27e79` | |
| `0397/image-no-data-refs-saved.pages` | [0397: Header field 2.6, the data a payload uses](../experiments/0397-the-data-references-field.md) | 91,246 | `548644181644a5812317d69f1ad899996f8aa0f92cfae316010730807690ce95` | |
| `0397/image-no-data-refs.pages` | [0397: Header field 2.6, the data a payload uses](../experiments/0397-the-data-references-field.md) | 395,953 | `33ce081425d9ae6e5a7179e161023f038e06062b489159675d34355267cf7c04` | |
| `0397/image-other-data-ref-saved.pages` | [0397: Header field 2.6, the data a payload uses](../experiments/0397-the-data-references-field.md) | 91,243 | `23071922e58616f680c16faca713c5575cfa1a01905ccc6fce40060703cd341b` | |
| `0397/image-other-data-ref.pages` | [0397: Header field 2.6, the data a payload uses](../experiments/0397-the-data-references-field.md) | 395,956 | `c2b92e58f4bd56a2b90d3e001a436ec733d01cba0e544241c880921edb079878` | |
| `0397/original-saved.pages` | [0397: Header field 2.6, the data a payload uses](../experiments/0397-the-data-references-field.md) | 91,246 | `78bf37d237b57d1185f39de586fdfa5240043aaee4facaed4a13ce175c3d3b58` | |
| `0397/original.pages` | [0397: Header field 2.6, the data a payload uses](../experiments/0397-the-data-references-field.md) | 91,240 | `8276979523a753a81dbe06c6e792abe0f549bad808593d5967cf7370e43f6b7a` | |
| `0398/donut-extra-bar.pages` | [0398: Header versions and extra payloads](../experiments/0398-extra-payloads.md) | 422,665 | `a7dd5fa43b1c483a62c7f5862b243c48f25e7fef4f8555e38f7d013e5a10102b` | |
| `0398/donut-main-pie.pages` | [0398: Header versions and extra payloads](../experiments/0398-extra-payloads.md) | 422,665 | `fbc92c04c1a423bf5af0c482045f3d88ff67ff1d2085666be662ac6ef1377b82` | |
| `0398/donut-no-extra.pages` | [0398: Header versions and extra payloads](../experiments/0398-extra-payloads.md) | 422,622 | `86ab933ebb610017c1424b73e43561228b51109543975d48142f72d3e688c4f0` | |
| `0398/donut.pages` | [0398: Header versions and extra payloads](../experiments/0398-extra-payloads.md) | 117,360 | `e0b264282745859fed0bb98ff85af3c7a00991974b765c0e7908653c384b5e01` | |
| `0398/pie-no-extra.pages` | [0398: Header versions and extra payloads](../experiments/0398-extra-payloads.md) | 422,622 | `b2984fce09aad534734f47d5d66684a61dbcac78f4b5ca9b550175c988244fec` | |
| `0399/axis-line.key` | [0399: Writing a chart's border and axis options](../experiments/0399-writing-chart-border-and-axes.md) | 1,242,316 | `df89993f83b857ac440fdc2fdec4ed8232597f1ea555be6d897ae7f66408b388` | |
| `0399/axis-name.key` | [0399: Writing a chart's border and axis options](../experiments/0399-writing-chart-border-and-axes.md) | 1,242,318 | `f483671ae481e110fe0a89b61b171166dd7cc705252537eee3af85785914e8c0` | |
| `0399/baseline.key` | [0399: Writing a chart's border and axis options](../experiments/0399-writing-chart-border-and-axes.md) | 904,201 | `a595c00777b5da2f922d7efd0241ca7e46e3994814a45107dc0553b0576c080e` | |
| `0399/border.key` | [0399: Writing a chart's border and axis options](../experiments/0399-writing-chart-border-and-axes.md) | 1,242,316 | `9bcf356257255beede3b89523bd7a8fc0ae8547107220f230d8f2cf99d7726fe` | |
| `0399/keynote-axis-line.key` | [0399: Writing a chart's border and axis options](../experiments/0399-writing-chart-border-and-axes.md) | 914,552 | `38573dc480398ee19ed5747b4afaa171eae6f493ac36ea9fbb93f12a65e65bad` | |
| `0399/keynote-axis-title.key` | [0399: Writing a chart's border and axis options](../experiments/0399-writing-chart-border-and-axes.md) | 915,757 | `33b53cafe7e4e82a4bfa78f033fcb3ff5d6e277e0aa96381160b27499299bffa` | |
| `0399/keynote-border-off.key` | [0399: Writing a chart's border and axis options](../experiments/0399-writing-chart-border-and-axes.md) | 1,253,943 | `641a0828f1fc97b858792c4025348d12381003e333d27eab6f7a0ea9511d5d9f` | |
| `0399/keynote-border.key` | [0399: Writing a chart's border and axis options](../experiments/0399-writing-chart-border-and-axes.md) | 915,879 | `add0935a376777fb0f877dd15f612da59fd78621ceee010391bc7bce0e58520d` | |
| `0399/keynote-no-minimum.key` | [0399: Writing a chart's border and axis options](../experiments/0399-writing-chart-border-and-axes.md) | 913,663 | `a0effc2b98d684a70239f8deadab5e2d22d60300ae215ca5e68f38242d9c41c5` | |
| `0399/no-minimum.key` | [0399: Writing a chart's border and axis options](../experiments/0399-writing-chart-border-and-axes.md) | 1,242,316 | `08b8d930c0d5ac08766534c2dbe979851fc14535ceabeddd5429613ba27744fa` | |
| `0400/baseline.key` | [0400: Writing a category axis name](../experiments/0400-writing-a-category-axis-name.md) | 904,185 | `a988fbe07c49f066e7d72b277110f27eb0fab4d0581d76be07ffad1fcf4e4438` | |
| `0400/category-14.key` | [0400: Writing a category axis name](../experiments/0400-writing-a-category-axis-name.md) | 1,242,313 | `f362a1c1f576dbcc19d7de8664dab8df8754939b4a0262647350b4c13be68491` | |
| `0400/category-name.key` | [0400: Writing a category axis name](../experiments/0400-writing-a-category-axis-name.md) | 1,242,313 | `45823195dbf9d2a675910c83d2922fe348061acd5b0c0656b9c00b0f3ea08243` | |
| `0400/keynote-x-axis-name.key` | [0400: Writing a category axis name](../experiments/0400-writing-a-category-axis-name.md) | 916,680 | `56eda796b2caec1d481116c9d9d5eac31d3cc8914dedd9317c4371534cb72950` | |
| `0401/columns-unfrozen.numbers` | [0401: Writing frozen header columns](../experiments/0401-writing-frozen-header-columns.md) | 457,165 | `9acc0e4014477a12c18c3064b5a1a26c6ccd1f05b5f9718a5707697e4420c07b` | |
| `0401/original.numbers` | [0401: Writing frozen header columns](../experiments/0401-writing-frozen-header-columns.md) | 138,837 | `317c41bb605f4f3e2e492fdee400ab0f24f0989884239cee3a3f2ac7f2dcedd1` | |
| `0401/two-columns-unfrozen.numbers` | [0401: Writing frozen header columns](../experiments/0401-writing-frozen-header-columns.md) | 457,165 | `b5575a83ee474e514dc3bfca6d2603885dded505225f5d770984cf1e4e5753be` | |
| `0402/no-repeat-grown.pages` | [0402: Writing repeated header rows](../experiments/0402-writing-repeated-header-rows.md) | 155,896 | `5ce18d56addd12dfa185d055dce8e22af8707a45ebad72d27a58930795a5639f` | |
| `0402/no-repeat.pages` | [0402: Writing repeated header rows](../experiments/0402-writing-repeated-header-rows.md) | 109,485 | `1df2e30d0942464fa4d9339816f681772035b82532e1994162713ae29f676c92` | |
| `0402/plain-table-grown.pages` | [0402: Writing repeated header rows](../experiments/0402-writing-repeated-header-rows.md) | 155,721 | `e4d80c866ef63d1602671bab28cd6be31fd85d17a1c29cdd418696f9e921a468` | |
| `0402/plain-table.pages` | [0402: Writing repeated header rows](../experiments/0402-writing-repeated-header-rows.md) | 109,446 | `3bd8d763eba804becd046d479b5218e6c6b177deb7004fe0bba0f965de1febf3` | |
| `0402/repeat-off-written-grown.pages` | [0402: Writing repeated header rows](../experiments/0402-writing-repeated-header-rows.md) | 155,824 | `521d621774b0f3c142b9271baf3752f92d1c4b0bd1f93d58302eab1714e1097a` | |
| `0402/repeat-off-written.pages` | [0402: Writing repeated header rows](../experiments/0402-writing-repeated-header-rows.md) | 418,911 | `7c8f46219849e42050dd2c191a1e149c3542ac3623df5a9c06071c4cecb886f8` | |
| `0402/repeat-written-grown.pages` | [0402: Writing repeated header rows](../experiments/0402-writing-repeated-header-rows.md) | 155,844 | `205c78f6407cb8a5bedeca0a2f4fa8ce4aba688dd8d1d098f188d22431de3ea0` | |
| `0402/repeat-written.pages` | [0402: Writing repeated header rows](../experiments/0402-writing-repeated-header-rows.md) | 418,949 | `7e91a08f464f14ba467ab6cea990cf7025bfc3523bbc83f4c5a8023de6356178` | |
| `0403/original.pages` | [0403: Writing a line's rotation and width](../experiments/0403-writing-a-line.md) | 93,444 | `94f8045c2a8ab0d26bfab023dca69db2cf1967c699c071ff6bcd5fe482ed4ee7` | |
| `0403/rot-0.pages` | [0403: Writing a line's rotation and width](../experiments/0403-writing-a-line.md) | 398,180 | `948e1c63e9123e45a75c62e66986c0d40b166e48b3a8ef5b34b4a790e2f21af8` | |
| `0403/rot-180.pages` | [0403: Writing a line's rotation and width](../experiments/0403-writing-a-line.md) | 398,180 | `4641bcc2c69eb68ca6690a53641ad6c8b23332325c3a265115a2bd7b50a68fbf` | |
| `0403/rot-90.pages` | [0403: Writing a line's rotation and width](../experiments/0403-writing-a-line.md) | 398,180 | `d33cee1a33af0281ba2a0056fe6d6c148f1c866648ec77ea51ec6431b0f95c43` | |
| `0403/width-100.pages` | [0403: Writing a line's rotation and width](../experiments/0403-writing-a-line.md) | 398,180 | `edbe02c4716a3c37966b5161f3c47af2f0a662a2a787b4edcaf123279d9db07d` | |
| `0404/natural-100-width-100.pages` | [0404: Writing a line's length](../experiments/0404-writing-a-line-length.md) | 398,180 | `330b25c3eda590b580999be12d75ab0177cc10deba523da8bb7734c89d5e990a` | |
| `0404/natural-100.pages` | [0404: Writing a line's length](../experiments/0404-writing-a-line-length.md) | 398,180 | `a2e6b7ffbfb1d24d9d1b79696e87c95f2bbfe2ad60ef883838c15014380459f9` | |
| `0404/original.pages` | [0404: Writing a line's length](../experiments/0404-writing-a-line-length.md) | 93,444 | `94f8045c2a8ab0d26bfab023dca69db2cf1967c699c071ff6bcd5fe482ed4ee7` | |
| `0404/point-100.pages` | [0404: Writing a line's length](../experiments/0404-writing-a-line-length.md) | 398,180 | `bcd9d35e3149c4c0997a99df438c2b9baf94cdb7779691b1ce25012fe8f32686` | |
| `0405/both-200.pages` | [0405: Writing a shape's size](../experiments/0405-writing-a-shape-size.md) | 398,765 | `6d08e9bc0d1f60b81b02463864020083693dd98d76d41ba15bde71c598adbda7` | |
| `0405/box-200.pages` | [0405: Writing a shape's size](../experiments/0405-writing-a-shape-size.md) | 398,765 | `02283359c5a04d801c7fb91575e67d1d410177938c402a4fe892f77730d4fb05` | |
| `0405/natural-200.pages` | [0405: Writing a shape's size](../experiments/0405-writing-a-shape-size.md) | 398,765 | `0b1d2e7271eabeef7cf67b6f108f9501083876b54ff8b4b92d42f83b7d4f209b` | |
| `0405/original.pages` | [0405: Writing a shape's size](../experiments/0405-writing-a-shape-size.md) | 93,910 | `afa0f2763c220f2fad55bba7bc90f7498b966ea095f621c5291f65adcec41d53` | |
| `0406/field3.pages` | [0406: Writing placeholder text](../experiments/0406-writing-placeholder-text.md) | 395,402 | `0d97ecc1c354225958f4ec041adbd60efee27a58c23ba8450f3cb85533e581c7` | |
| `0406/first-word.pages` | [0406: Writing placeholder text](../experiments/0406-writing-placeholder-text.md) | 395,395 | `c027f2fb70bd20040647e66ae25e402af0b4f945b5f612357bfccfc5454872b0` | |
| `0406/none.pages` | [0406: Writing placeholder text](../experiments/0406-writing-placeholder-text.md) | 395,385 | `1cdf0b2a476d804ff363374eafded00cfaf726e45f40d26fbca1fa346144bd03` | |
| `0406/original.pages` | [0406: Writing placeholder text](../experiments/0406-writing-placeholder-text.md) | 90,778 | `67f0aba65e0983244760c7e3f0cf049e2c8c756148300052fb5be85bef130f7a` | |
| `0406/template-kind.pages` | [0406: Writing placeholder text](../experiments/0406-writing-placeholder-text.md) | 395,395 | `17dc37c37bb697590331c92d9a0befcbe76dd921788f8b36392b4e1efe9734ea` | |
| `0406/whole.pages` | [0406: Writing placeholder text](../experiments/0406-writing-placeholder-text.md) | 395,391 | `c8cba89fcca855e04e2f4f0a75b9291127ce0c2abcf86bd46aaf805333ee69c2` | |
| `0407/entry-model-field2.pages` | [0407: Writing a table of contents](../experiments/0407-writing-a-table-of-contents.md) | 397,261 | `bf10e0ec244a636747067e0ff5242b9bcd2a9f5f9d951a2b7fb51b7565e66cc4` | |
| `0407/entry-model-roman.pages` | [0407: Writing a table of contents](../experiments/0407-writing-a-table-of-contents.md) | 397,265 | `4f4b33f8a90d614ca508099cc82f8d410edb585118445254f8015b334ef6cddb` | |
| `0407/entry-model-text.pages` | [0407: Writing a table of contents](../experiments/0407-writing-a-table-of-contents.md) | 397,271 | `bdfec5773f6fbc6f760559c1024839307a8443578187d4022761e5deef193b85` | |
| `0407/entry-text.pages` | [0407: Writing a table of contents](../experiments/0407-writing-a-table-of-contents.md) | 397,261 | `7d27dcfc80ccaeaaeb64e707d20a227b81e14071fe2abb9e0312dec6cce7ce2b` | |
| `0407/heading-renamed.pages` | [0407: Writing a table of contents](../experiments/0407-writing-a-table-of-contents.md) | 397,261 | `1f8c825f5081965318af7c96d9162d49e3da0acdc55bdba7219ed50d414a2bb9` | |
| `0407/original.pages` | [0407: Writing a table of contents](../experiments/0407-writing-a-table-of-contents.md) | 92,330 | `b22d0740745cce16a5ccae294d5037860f31c475e8234010f3be124fe79c6d49` | |
| `0407/page-number.pages` | [0407: Writing a table of contents](../experiments/0407-writing-a-table-of-contents.md) | 397,261 | `0bc3bc727472c2f75eb76e36fb794bcbe51127c3ef82247fe4b6c56cbb36f283` | |
| `0409/cache-9.numbers` | [0409: Writing a Numbers chart's link to its cells](../experiments/0409-writing-a-numbers-chart-link.md) | 453,694 | `cc0689fddabfd13756e2612130f288b5f1dc1af7af1f65c5ccdac7f89f7535d9` | |
| `0409/cell-b2-9.numbers` | [0409: Writing a Numbers chart's link to its cells](../experiments/0409-writing-a-numbers-chart-link.md) | 453,694 | `83268de029c150a611975d91a9ed68ab32e67201fdefa5b0860a5de55baffdef` | |
| `0409/link-to-c2.numbers` | [0409: Writing a Numbers chart's link to its cells](../experiments/0409-writing-a-numbers-chart-link.md) | 453,694 | `eaf4c3304d7e2fb3ae91b07d0e98a774f25b1c92a2113092fd1b93c473264710` | |
| `0409/link-to-column-c.numbers` | [0409: Writing a Numbers chart's link to its cells](../experiments/0409-writing-a-numbers-chart-link.md) | 453,694 | `e21e8776af0958507fd47d0da7bc94b0a70f5613f36b78ddad19ba42ea143ac4` | |
| `0409/numbers-b2-2.numbers` | [0409: Writing a Numbers chart's link to its cells](../experiments/0409-writing-a-numbers-chart-link.md) | 137,834 | `a99022af6c84519f8d1cb2736a562f7980c82225bfe11f32cfc43cc2b5bdb701` | |
| `0409/numbers-b2-9.numbers` | [0409: Writing a Numbers chart's link to its cells](../experiments/0409-writing-a-numbers-chart-link.md) | 136,578 | `cc036e37e7515a2c6e8c11ada39edfa176583a6a0d5140a1af3f2f190ac7c0e3` | |
| `0409/numbers-x-is-y.numbers` | [0409: Writing a Numbers chart's link to its cells](../experiments/0409-writing-a-numbers-chart-link.md) | 138,191 | `a826efdececf96b8fed1bbe6dfb4e998a90f0789b19e8a8a0b1ff0a988e1df91` | |
| `0409/original.numbers` | [0409: Writing a Numbers chart's link to its cells](../experiments/0409-writing-a-numbers-chart-link.md) | 137,249 | `eb73722d82dfcd750b5c731cbd3113b240d96c618aefcb1fb5a6f2caf7568c78` | |
| `0410/numbers-average.numbers` | [0410: Writing a pivot table's summary function](../experiments/0410-writing-a-pivot-summary.md) | 153,044 | `111775ae8704e4a5c0bd2687e97cd8fd749ae2eb985acc7d74a3a8444121b017` | |
| `0410/sum-edited.numbers` | [0410: Writing a pivot table's summary function](../experiments/0410-writing-a-pivot-summary.md) | 153,278 | `33f8705574cc0ac82a421fae281552943608ef261edd8d4d3e1c88b12aca357c` | |
| `0410/sum.numbers` | [0410: Writing a pivot table's summary function](../experiments/0410-writing-a-pivot-summary.md) | 153,069 | `0645ae445578c670e9e654316fdec72ac55b4a92e87db17eb5782311f25ab785` | |
| `0410/written-average-edited.numbers` | [0410: Writing a pivot table's summary function](../experiments/0410-writing-a-pivot-summary.md) | 156,825 | `4d860efcf38f68425342edcd68bf92da8c6cdf7c91487fe98341e64ef87b22d3` | |
| `0410/written-average.numbers` | [0410: Writing a pivot table's summary function](../experiments/0410-writing-a-pivot-summary.md) | 486,874 | `7bffbabb2284250270efac8df29d9cca2e012763ca74194fbd53050c8a80f91a` | |
| `0411/original.numbers` | [0411: Writing a category's value and rows](../experiments/0411-writing-categories.md) | 146,960 | `d3effbe19f95289167edf7e259f581844b2dbf6e5ca8331fd09815db75d28616` | |
| `0411/rows-swapped.numbers` | [0411: Writing a category's value and rows](../experiments/0411-writing-categories.md) | 469,137 | `ded1864395a4337a477eda21227d6e1ea5ae1f315f0874e6d48c2a0d31c0d459` | |
| `0411/value-z-6-only.numbers` | [0411: Writing a category's value and rows](../experiments/0411-writing-categories.md) | 469,137 | `c8a176bfd1682400b96fa3c1a3426380e7416659b75abed78ab3f8600cf1130b` | |
| `0411/value-z.numbers` | [0411: Writing a category's value and rows](../experiments/0411-writing-categories.md) | 469,137 | `2bacd78d475330753d6797dc6a702673f0eb54378cdea4cd26b1d73027eada93` | |
| `0412/exposure-minus-no-copy.pages` | [0412: Writing image adjustments](../experiments/0412-writing-image-adjustments.md) | 399,430 | `7c9a2560989537f4280e4087e6344f035f91674010f24644b17aaebac5babd3c` | |
| `0412/exposure-minus.pages` | [0412: Writing image adjustments](../experiments/0412-writing-image-adjustments.md) | 399,434 | `fe8ec7b8d425dc61e7dfefe117a129afc8944b6d4281af4ffdce1b3f979ae327` | |
| `0412/no-filtered-copy.pages` | [0412: Writing image adjustments](../experiments/0412-writing-image-adjustments.md) | 399,430 | `9be17474a3c86b05b4eff1fea25c226c65fd7c6ff67b6a66c87876b78de527b2` | |
| `0412/original.pages` | [0412: Writing image adjustments](../experiments/0412-writing-image-adjustments.md) | 94,686 | `42f06e68e685c72b827079aefb783aff87de2b97e6ea1b8b6a5fce3e5eef253c` | |
| `0412/unadjusted.pages` | [0412: Writing image adjustments](../experiments/0412-writing-image-adjustments.md) | 91,240 | `8276979523a753a81dbe06c6e792abe0f549bad808593d5967cf7370e43f6b7a` | |
| `0413/original.pages` | [0413: Writing a shape's style preset](../experiments/0413-writing-a-shape-style-preset.md) | 92,381 | `2cfedb21087e089187adb53f48797bd950d7d1b0d0461f57c70520d55150a335` | |
| `0413/pages-blue.pages` | [0413: Writing a shape's style preset](../experiments/0413-writing-a-shape-style-preset.md) | 95,552 | `6d6311ec79353e445e997c2508a35c0f33adc2685b354bae32bb6f63548846ba` | |
| `0413/style-1731554.pages` | [0413: Writing a shape's style preset](../experiments/0413-writing-a-shape-style-preset.md) | 397,164 | `6136fb298807dfb5b2f0442865e40f0003f8afd395e685dba995aeb6702d08bc` | |
| `0413/style-1731556.pages` | [0413: Writing a shape's style preset](../experiments/0413-writing-a-shape-style-preset.md) | 397,164 | `3ad6087358a2ad61b8ad4787fb7b00fb8ef8fe179145bac21b4608cd3380b0f4` | |
| `0414/arrow-level0.key` | [0414: Writing a Keynote bullet](../experiments/0414-writing-a-keynote-bullet.md) | 1,223,072 | `b024a461217a7fdbf307cbd3b5730675ff30d23a4bd08ed82c835bebfd50cf33` | |
| `0414/original.key` | [0414: Writing a Keynote bullet](../experiments/0414-writing-a-keynote-bullet.md) | 885,783 | `24f9ef5d878fd684eced45f812bca2de0811149edc978dba6b020ea3b9965088` | |
| `0414/star-all.key` | [0414: Writing a Keynote bullet](../experiments/0414-writing-a-keynote-bullet.md) | 1,223,054 | `6dd5e429003724670977e8eb0671108c84ebff08a9cb4655a1c6868d11f40f1e` | |
| `0415/original.key` | [0415: Writing a layout's name](../experiments/0415-writing-a-layout-name.md) | 886,912 | `1e56d02d37f1b4ddc4cb0135f4695009337753f77782592d38f5a209e421f2a2` | |
| `0415/renamed-blank.key` | [0415: Writing a layout's name](../experiments/0415-writing-a-layout-name.md) | 1,226,793 | `1c28bc67bef04df9feb8f9cf740cf21e36eb801bc967d50f4b16a1133e7c5291` | |
| `0415/renamed.key` | [0415: Writing a layout's name](../experiments/0415-writing-a-layout-name.md) | 1,226,794 | `82960eadb922b73f07b6326118cfdfb059ae9294a92a0dcabe413d862f9eb88b` | |
| `0416/original.numbers` | [0416: Writing the order of sheets](../experiments/0416-writing-sheet-order.md) | 145,624 | `6097ec4360217b5858be9265c95c434b4cd06c8b0e93a2d387b45a8b762728c9` | |
| `0416/reversed.numbers` | [0416: Writing the order of sheets](../experiments/0416-writing-sheet-order.md) | 464,875 | `7bbf498e9aa8e09ca665bce03882081902bc6c4ae9d832ee746936b28ed2c815` | |
| `0416/second-only.numbers` | [0416: Writing the order of sheets](../experiments/0416-writing-sheet-order.md) | 464,869 | `1413966295810d20a16cf9330abf59419b5f83f9e0532e322857bd0dc74bc22a` | |
| `0417/first-only.numbers` | [0417: Writing the objects on a sheet](../experiments/0417-writing-sheet-objects.md) | 461,848 | `70b51954672621752e653ff637a6122e09247764959dcbe41e3440f5a363da9f` | |
| `0417/original.numbers` | [0417: Writing the objects on a sheet](../experiments/0417-writing-sheet-objects.md) | 144,736 | `8caa08fca4b142998db4ca34c9791a7c09c0818aba72592bb5cc63bc3fb1af12` | |
| `0417/reversed.numbers` | [0417: Writing the objects on a sheet](../experiments/0417-writing-sheet-objects.md) | 461,854 | `2d0a7f4a742ce4f41f8232578f8ab9d7c604efdc03607777ed69c6093b82251f` | |
| `0418/no-name-y-100.numbers` | [0418: Writing a Numbers table's position](../experiments/0418-writing-a-table-position.md) | 457,165 | `0451417fbf3de019aee071e7366c163e2a058965d855b87015b86fd4b20c9deb` | |
| `0418/no-name.numbers` | [0418: Writing a Numbers table's position](../experiments/0418-writing-a-table-position.md) | 457,165 | `40e73e19183bb5eca67a04c3d6c54715eda0ce44c94673c2bda53fafea7e5872` | |
| `0418/original.numbers` | [0418: Writing a Numbers table's position](../experiments/0418-writing-a-table-position.md) | 138,837 | `317c41bb605f4f3e2e492fdee400ab0f24f0989884239cee3a3f2ac7f2dcedd1` | |
| `0418/x-50-y-0.numbers` | [0418: Writing a Numbers table's position](../experiments/0418-writing-a-table-position.md) | 457,165 | `490bbc11ec1647079f43bfcfd4daf7d36cf7ef511adf573d55185c6968b5bf5f` | |
| `0418/y-100.numbers` | [0418: Writing a Numbers table's position](../experiments/0418-writing-a-table-position.md) | 457,165 | `68ac5756efb3b8e60c15d3319445996d2bb7ac64e542c8f037cfe25202d6e1ff` | |
| `0418/y-minus-28.numbers` | [0418: Writing a Numbers table's position](../experiments/0418-writing-a-table-position.md) | 457,165 | `99ce88b699e41df001e1f913c1998ca6dc403799992f0233365eb02ef8445ce0` | |
| `0419/no-body.pages` | [0419: Writing the document body setting](../experiments/0419-writing-the-document-body-setting.md) | 395,046 | `579ee07113dcb299a742a5a289d341e74b9ba1c1cb181e167c88155a5d51c955` | |
| `0419/original.pages` | [0419: Writing the document body setting](../experiments/0419-writing-the-document-body-setting.md) | 90,438 | `96db185563729e8d065f4825fb7763535b54571fa59d55d6eb351c7000f43349` | |
| `0419/pages-no-body-on.pages` | [0419: Writing the document body setting](../experiments/0419-writing-the-document-body-setting.md) | 394,624 | `99e2429f1ef28b5026dff627f4dc5fe876042d50ca637c3fbb3d2a8ec569bbe2` | |
| `0419/pages-no-body.pages` | [0419: Writing the document body setting](../experiments/0419-writing-the-document-body-setting.md) | 89,806 | `b6f963b0cad955e3628292148efcf135a16a82adce0678c6298bcd8e37b54d36` | |
| `0420/hyphenate.pages` | [0420: Writing hyphenation](../experiments/0420-writing-hyphenation.md) | 395,421 | `cac74ab3f5588f1c19900ab76104d3729b3696352b4a92366040f4b7503a6bbb` | |
| `0420/no-hyphenate.pages` | [0420: Writing hyphenation](../experiments/0420-writing-hyphenation.md) | 395,421 | `fd9097853a28447e8c28698b8aeca631fd5e8e5741bba0e0e6ee20c5b27d9419` | |
| `0420/text.pages` | [0420: Writing hyphenation](../experiments/0420-writing-hyphenation.md) | 395,421 | `fd9097853a28447e8c28698b8aeca631fd5e8e5741bba0e0e6ee20c5b27d9419` | |
| `0421/ligatures-off.pages` | [0421: Writing document ligatures](../experiments/0421-writing-document-ligatures.md) | 395,080 | `b9809bccd8a227d1380c1aa06b5313a6a527a53dd02c325da82feeefe5ff54e6` | |
| `0421/ligatures-on.pages` | [0421: Writing document ligatures](../experiments/0421-writing-document-ligatures.md) | 395,080 | `bacc3f1bc38d33af6a99b5bb6152a03eca34af0671e119e9bbb2f0c2ff548018` | |
| `0421/text.pages` | [0421: Writing document ligatures](../experiments/0421-writing-document-ligatures.md) | 395,080 | `bacc3f1bc38d33af6a99b5bb6152a03eca34af0671e119e9bbb2f0c2ff548018` | |
| `0422/both-off.pages` | [0422: Writing the header and footer switches](../experiments/0422-writing-header-and-footer-switches.md) | 395,072 | `1657d3fc547c21f71a782f80f056c6056d539373aef5aa2fea884e02876d8962` | |
| `0422/footer-hidden.pages` | [0422: Writing the header and footer switches](../experiments/0422-writing-header-and-footer-switches.md) | 395,059 | `8d43b5c550e8ade0def645931fd45f7a8d472c4ab56cfc4bcf1299dfb5f453a7` | |
| `0422/footer.pages` | [0422: Writing the header and footer switches](../experiments/0422-writing-header-and-footer-switches.md) | 395,059 | `d920a66b09d03e8202a0d7cc25fe5b52842d97936fa3cd629c67cdba3460d560` | |
| `0422/footers-off.pages` | [0422: Writing the header and footer switches](../experiments/0422-writing-header-and-footer-switches.md) | 395,072 | `640e44ac719aa254631005e299278ef80640f349077bc4e3c99512b6ea1c8c8a` | |
| `0422/headers-off.pages` | [0422: Writing the header and footer switches](../experiments/0422-writing-header-and-footer-switches.md) | 395,072 | `be5b08c3ad585a002de5d89a61a4864db2a6e1ac6bbfcfd10f59370f790d8a50` | |
| `0422/texts.pages` | [0422: Writing the header and footer switches](../experiments/0422-writing-header-and-footer-switches.md) | 395,072 | `489589b6350c709eb794f70eb95f5257a577833920e565ce3793aa6154a9b73c` | |
| `0423/char-moved-only.pages` | [0423: Writing an object's place in the text](../experiments/0423-writing-an-object-in-the-text.md) | 418,850 | `7e21c6befcbbbecc6050187124dc83d26924c7445b5ec1fff5ca8b5e48b4819e` | |
| `0423/entry-moved-only.pages` | [0423: Writing an object's place in the text](../experiments/0423-writing-an-object-in-the-text.md) | 418,850 | `770232d1e2344e9a780b26599f3ef7dd17ca87ff776ed410ab64a69f1bc12542` | |
| `0423/original.pages` | [0423: Writing an object's place in the text](../experiments/0423-writing-an-object-in-the-text.md) | 109,537 | `35c583b3f068e769ad9ab06a3f720322fa37add9fd65ee31e975d0b983f9a4a0` | |
| `0423/table-first.pages` | [0423: Writing an object's place in the text](../experiments/0423-writing-an-object-in-the-text.md) | 418,850 | `c8c0de00c9ef6c02b25e9ffac885c77c2893f76a68fe8e9a8b11a35e1194d288` | |
| `0424/body-dropped.pages` | [0424: Writing the list of objects on the page](../experiments/0424-writing-the-page-objects-list.md) | 397,158 | `502a30f2d6f3d31027ff25c26a69a05b2d42bba31dff9ae6775f7ca689703f77` | |
| `0424/original.pages` | [0424: Writing the list of objects on the page](../experiments/0424-writing-the-page-objects-list.md) | 92,381 | `2cfedb21087e089187adb53f48797bd950d7d1b0d0461f57c70520d55150a335` | |
| `0424/shape-dropped.pages` | [0424: Writing the list of objects on the page](../experiments/0424-writing-the-page-objects-list.md) | 397,158 | `301c8a94ff00cfb99e01b3cad600e29de98485837366374d61eaa6579102dd85` | |
| `0424/shape-first.pages` | [0424: Writing the list of objects on the page](../experiments/0424-writing-the-page-objects-list.md) | 397,164 | `29014c4ea493546d1092916208fbc6bc58145b6bae6a9aea10c1a36931f9fb1b` | |
| `0425/over-text.pages` | [0425: Writing the stacking order of the page](../experiments/0425-writing-stacking-order.md) | 397,164 | `dad17e1aadca8e481e5c8b2d38b2ac9ace13ce6b6c5bdeb7f8acf910ddb608b5` | |
| `0425/shape-first.pages` | [0425: Writing the stacking order of the page](../experiments/0425-writing-stacking-order.md) | 397,164 | `42a3399c3d90af2412702e05452619da4d84cc9f976ea2c545c811afa8b0c071` | |
| `0426/a2-b3.numbers` | [0426: Writing a merge over a value that isn't in its first cell](../experiments/0426-writing-a-merge-over-a-value.md) | 451,556 | `acfcba25d59ca50f07cead8eef727b95f4dbbb4320cbe405436e6d5b99f13914` | |
| `0426/b1-b2.numbers` | [0426: Writing a merge over a value that isn't in its first cell](../experiments/0426-writing-a-merge-over-a-value.md) | 451,554 | `59784edf93b7f41e20f8d4d9c646c801117870e9eead1e205643c93a559b4e15` | |
| `0426/b2-b3.numbers` | [0426: Writing a merge over a value that isn't in its first cell](../experiments/0426-writing-a-merge-over-a-value.md) | 451,554 | `feafed3e2b3cc76a2aa472d96f7763fa1d80e1b2b428b79110f7fc20f1cb90ae` | |
| `0427/text.pages` | [0427: Writing paragraph runs without a style](../experiments/0427-writing-paragraph-runs-without-a-style.md) | 395,054 | `271bb0ceeae7f6bb57312bc25afa570038c3d9929d079cff15078404c825daad` | |
| `0427/title-body-none.pages` | [0427: Writing paragraph runs without a style](../experiments/0427-writing-paragraph-runs-without-a-style.md) | 395,068 | `e58d7914b876ce30b68490a12fa0f6d61636d8d5b837ed1330ade84306f9ff0f` | |
| `0427/title-none-body.pages` | [0427: Writing paragraph runs without a style](../experiments/0427-writing-paragraph-runs-without-a-style.md) | 395,068 | `276c9c535ae15f5b69cbd2f6ef81ba2c4c04d1e294f87fb264e2b384b36c61d1` | |
| `0427/title-only.pages` | [0427: Writing paragraph runs without a style](../experiments/0427-writing-paragraph-runs-without-a-style.md) | 395,054 | `683e85cc2ea098631944a25b714d863ddceb966a7b5d69905b195c0b5dd6dd48` | |
| `0428/font-bold-name-and-flag.pages` | [0428: Writing a font name with a weight](../experiments/0428-writing-a-font-name-with-a-weight.md) | 395,051 | `59ff7cd48de6368603063c7d5d9d5cd0e600af7f9bfbcfccb7e1674af0c7a629` | |
| `0428/font-bold-name.pages` | [0428: Writing a font name with a weight](../experiments/0428-writing-a-font-name-with-a-weight.md) | 395,051 | `4c0f33e3b51a0fa37d4c3da7db6a02cd474324019eb2232e732d70d05603721d` | |
| `0428/font-italic-name.pages` | [0428: Writing a font name with a weight](../experiments/0428-writing-a-font-name-with-a-weight.md) | 395,053 | `53da038ecf62ecdc27afb4ec7f8ed2309892acf7872479363eca5ce63c162ca1` | |
| `0428/font-light-name-and-flag.pages` | [0428: Writing a font name with a weight](../experiments/0428-writing-a-font-name-with-a-weight.md) | 395,052 | `28eebd64f5d0d30a30c0d66c1c54a733a8364b72672ae535107142b7d6c55459` | |
| `0428/original.pages` | [0428: Writing a font name with a weight](../experiments/0428-writing-a-font-name-with-a-weight.md) | 90,438 | `96db185563729e8d065f4825fb7763535b54571fa59d55d6eb351c7000f43349` | |
| `0429/cr.key` | [0429: Writing breaks in a Keynote title](../experiments/0429-writing-breaks-in-a-keynote-title.md) | 1,223,082 | `42163376c60743056125dd50a6953f685e34db83bab43cb2dc19d466f1ec5063` | |
| `0429/lf.key` | [0429: Writing breaks in a Keynote title](../experiments/0429-writing-breaks-in-a-keynote-title.md) | 1,223,082 | `b9db7971a8c1413207b94e06a2789c3091ea18a331b2d17738b9e4ea316e82d5` | |
| `0429/line-sep.key` | [0429: Writing breaks in a Keynote title](../experiments/0429-writing-breaks-in-a-keynote-title.md) | 1,223,073 | `56e4604c885a398f9c2c76dd4b63470af3dab84b7b5b28332b43999fd245ce06` | |
| `0429/original.key` | [0429: Writing breaks in a Keynote title](../experiments/0429-writing-breaks-in-a-keynote-title.md) | 885,748 | `3e5e6327488684553880bebce619f933855b3727106f0e9f003c61b5c312a432` | |
| `0430/caption-text.key` | [0430: Writing a chart's caption](../experiments/0430-writing-a-chart-caption.md) | 1,252,655 | `5df6c9d85ddc4840da83a8d9eb6cf9323495d7ec6aad221fbd8ce98f353b9de3` | |
| `0430/original.key` | [0430: Writing a chart's caption](../experiments/0430-writing-a-chart-caption.md) | 914,239 | `fd7a5d05c7fe008fa183fa40504f4668b6bbf431888a99115d1756b199aa0f0e` | |
| `0431/original.pages` | [0431: Writing a non-ASCII name into the ZIP](../experiments/0431-writing-a-non-ascii-part-name.md) | 91,240 | `8276979523a753a81dbe06c6e792abe0f549bad808593d5967cf7370e43f6b7a` | |
| `0432/deflate-all.pages` | [0432: Writing compressed ZIP entries](../experiments/0432-writing-compressed-zip-entries.md) | 48,586 | `42afae1c0f0963ba87398da4094a57a934fa0f7c395199493c28bba9de1a6e28` | |
| `0432/deflate-data.pages` | [0432: Writing compressed ZIP entries](../experiments/0432-writing-compressed-zip-entries.md) | 91,116 | `f770a4a02cccac058dfb466e4f98834f830bd3cd035185ddddbed97df2ef1a31` | |
| `0432/deflate-iwa.pages` | [0432: Writing compressed ZIP entries](../experiments/0432-writing-compressed-zip-entries.md) | 62,171 | `c1a3e85d0228d2c1e534bf652dde8e7fe0c572f8fc7621f647d27cf94108fec6` | |
| `0432/original.pages` | [0432: Writing compressed ZIP entries](../experiments/0432-writing-compressed-zip-entries.md) | 91,240 | `8276979523a753a81dbe06c6e792abe0f549bad808593d5967cf7370e43f6b7a` | |
| `0433/chunks-1000.pages` | [0433: Writing other chunk sizes](../experiments/0433-writing-chunk-sizes.md) | 398,350 | `288e196a81e1849ab49d7c964870b4b41119d3f8e9020ac1cabc0a2bced2197e` | |
| `0433/chunks-1000000.pages` | [0433: Writing other chunk sizes](../experiments/0433-writing-chunk-sizes.md) | 395,012 | `7d649ed002444498c38b8f617224e8235f2c72b206243bb8110742a174bb9f62` | |
| `0433/chunks-65536.pages` | [0433: Writing other chunk sizes](../experiments/0433-writing-chunk-sizes.md) | 395,046 | `08e2b36153e26defc175bbb71e432b0b837f3b5c973e6da58e7bc7ad71d021b9` | |
| `0434/no-history.pages` | [0434: Leaving out package files](../experiments/0434-leaving-out-package-files.md) | 89,903 | `b61f02589c7814ea344d8d3561e6da1b09efe25c5a784f32b8bd9360d3d2ba85` | |
| `0434/no-identifier.pages` | [0434: Leaving out package files](../experiments/0434-leaving-out-package-files.md) | 90,152 | `3b4c763034a4b2fe7d4fd5b336b6a9d9f81bd4f45c7ba7a85b50fb3dfe235ee2` | |
| `0434/no-metadata-folder.pages` | [0434: Leaving out package files](../experiments/0434-leaving-out-package-files.md) | 89,086 | `bd2c84091a4928c1bae884be26022f65f00b57ac0d6e9522472bf86d217b5bce` | |
| `0434/no-previews.pages` | [0434: Leaving out package files](../experiments/0434-leaving-out-package-files.md) | 73,802 | `a79abdcbacfb29ebfb7b96b7b31a9562eb1be41e14e9b8e07e53150da996bf61` | |
| `0434/no-properties.pages` | [0434: Leaving out package files](../experiments/0434-leaving-out-package-files.md) | 89,667 | `4cc086b16b80c4d90915fe539efcd8dfa70190c424939b25376aa5e355e09ada` | |
| `0434/no-viewstate.pages` | [0434: Leaving out package files](../experiments/0434-leaving-out-package-files.md) | 89,481 | `bcdc75bd7071da86c3632069d90cd5fbf9bb4566f0489f072edea4d26b41dd22` | |
| `0434/only-index.pages` | [0434: Leaving out package files](../experiments/0434-leaving-out-package-files.md) | 72,570 | `88e243e9f6e4bfefa594a689937c7521a2ddbbeb970fa00747c6501f488e78be` | |
| `0435/extra-listed-saved.pages` | [0435: Writing a data file that nothing uses](../experiments/0435-writing-an-unused-data-file.md) | 91,245 | `a267d8b25552ffed0b26da95eea05227817eaba6aacffa66992484a8ed2e41f2` | |
| `0435/extra-unlisted-saved.pages` | [0435: Writing a data file that nothing uses](../experiments/0435-writing-an-unused-data-file.md) | 91,245 | `4bf9a0f56f35d7b861a220d24ffab4d8bed5f8c2e7c98a7bc26364c0f815a512` | |
| `0436/plain.pages` | [0436: Writing a soft hyphen](../experiments/0436-writing-a-soft-hyphen.md) | 395,221 | `d20dc70c2f41e71b02ad7897bf69c01da53c2c71670e912c9d04d3bb53b43050` | |
| `0436/soft-hyphens.pages` | [0436: Writing a soft hyphen](../experiments/0436-writing-a-soft-hyphen.md) | 395,225 | `ae4c48fbca1933d251cdb13b204f5a21efb53b9064e90b77e1300c98f41203e2` | |
| `0437/count-0.numbers` | [0437: Writing a tile's row count](../experiments/0437-writing-a-tile-row-count.md) | 457,165 | `8311052c6817f5589e94774fa0f48dd2165a9805d9613b8212ebad39d9a8749e` | |
| `0437/count-2.numbers` | [0437: Writing a tile's row count](../experiments/0437-writing-a-tile-row-count.md) | 457,165 | `6f9517cac1cc6a85d398046571eb35350a4e3e47ddca3060d3e50628a239943a` | |
| `0437/count-9.numbers` | [0437: Writing a tile's row count](../experiments/0437-writing-a-tile-row-count.md) | 457,165 | `dedb71dea1e665e4cb0cfd390d59a94190d6c2b725d56410b987b8b2d12ae9ee` | |
| `0437/field6-2.numbers` | [0437: Writing a tile's row count](../experiments/0437-writing-a-tile-row-count.md) | 457,165 | `8bff05cd4a2628ab7e4f6fb07e89fdf01e7c818b03b839ad9f1d175b34fc48a9` | |
| `0437/original.numbers` | [0437: Writing a tile's row count](../experiments/0437-writing-a-tile-row-count.md) | 138,837 | `317c41bb605f4f3e2e492fdee400ab0f24f0989884239cee3a3f2ac7f2dcedd1` | |
| `0438/image-package.pages` | [0438: Writing a document as a package](../experiments/0438-writing-a-package.md) | 90,292 | `9132c2597dbefedd85d3ea03a4ac02dfbaeae49acc199ef68a7404aec8f541c6` | a folder package |
| `0439/box-100.key` | [0439: Writing a Keynote line](../experiments/0439-writing-a-keynote-line.md) | 1,221,006 | `71bf2796d20d8eaeb21f5f6845485c4d05ec2f1f8e5405df2978a127894dc042` | |
| `0439/natural-100.key` | [0439: Writing a Keynote line](../experiments/0439-writing-a-keynote-line.md) | 1,221,006 | `d1c96dc5d59a599f990ab5b6bac651d33cd4ad81ed2de99438f9de10a778c275` | |
| `0439/original.key` | [0439: Writing a Keynote line](../experiments/0439-writing-a-keynote-line.md) | 883,432 | `b927affb08322ac6affda34e08a1a82cb444a483971c5d6297cf8fe884895c4f` | |
| `0439/rot-90.key` | [0439: Writing a Keynote line](../experiments/0439-writing-a-keynote-line.md) | 1,221,006 | `86fb04240677143fc6fd7ed4208956074159fd4dd052957e641732b112f1deb1` | |
| `0441/arabic.pages` | [0441: Writing right-to-left text](../experiments/0441-writing-right-to-left-text.md) | 395,066 | `fe380084e82d9e768a9c0c1d0f31d083d20438a07031c7a27415c0e7113f7d96` | |
| `0441/latin.pages` | [0441: Writing right-to-left text](../experiments/0441-writing-right-to-left-text.md) | 395,052 | `84773a195257061f456367dfafa40efebcc7e5c2ef4088a20700a47a6c4acd90` | |
| `0441/mixed.pages` | [0441: Writing right-to-left text](../experiments/0441-writing-right-to-left-text.md) | 395,071 | `7383829065578e3c4d6c6dbd312a04712fe9879db5b7e8053f967d8648f07a1b` | |
| `0443/c-0-0-0.pages` | [0443: The colours tracked changes are drawn in](../experiments/0443-author-colours.md) | 395,730 | `cb8acfe0770188bab0462ed2bc5001644d1962d48186872802da23a969d9a488` | names its author |
| `0443/c-0-1-1.pages` | [0443: The colours tracked changes are drawn in](../experiments/0443-author-colours.md) | 395,730 | `8be42f2ea4e364ef318b2372373fe3c5cf1febfc95748d2be51a329ddb8ab004` | names its author |
| `0443/c-0.36-0.78-0.69.pages` | [0443: The colours tracked changes are drawn in](../experiments/0443-author-colours.md) | 395,730 | `dcd08eb0e5bb38f87799159544397417eaa5cd204c35db0e1a96ff9fa5db165a` | names its author |
| `0443/c-0.5-0-1.pages` | [0443: The colours tracked changes are drawn in](../experiments/0443-author-colours.md) | 395,730 | `0a9418e1bd1fd45489aeab631f92300eeee3f4c7f9f0c05b0ce5ca063a332ba3` | names its author |
| `0443/c-0.5-0.5-0.5.pages` | [0443: The colours tracked changes are drawn in](../experiments/0443-author-colours.md) | 395,730 | `652726ccf232e2063903f32c15753e60b913e7cd8d6aaf900a9a21cc50b85bed` | names its author |
| `0443/c-0.98-0.6-0.21.pages` | [0443: The colours tracked changes are drawn in](../experiments/0443-author-colours.md) | 395,730 | `f101f8c317a64b343c2564eccc4c2e92b17f1b8938c79096184785f39771fc3a` | names its author |
| `0443/c-1-0-1.pages` | [0443: The colours tracked changes are drawn in](../experiments/0443-author-colours.md) | 395,730 | `ee2660861b4970adf230ea4855c9ab7a78ab39a3ef701e5610e91904c8cc97f6` | names its author |
| `0443/c-1-0.5-0.pages` | [0443: The colours tracked changes are drawn in](../experiments/0443-author-colours.md) | 395,730 | `a4ed6afe2ef5b4aaf1af16dbb9706ee75223fca7bc25c1db7d5f5f635691e1a8` | names its author |
| `0443/c-1-1-0.pages` | [0443: The colours tracked changes are drawn in](../experiments/0443-author-colours.md) | 395,730 | `725a601399ec1054b57cbcbf262cb8108079caad1a93bd6263088087808487d0` | names its author |
| `0443/c-1-1-1.pages` | [0443: The colours tracked changes are drawn in](../experiments/0443-author-colours.md) | 395,730 | `45b162aadde32185ec2dc91fe01ea3249d377ffbc282b57c44a4e3e9e99a52e2` | names its author |
| `0444/angle-0.pages` | [0444: Where a radial gradient is centred](../experiments/0444-where-a-radial-gradient-is-centred.md) | 398,470 | `f49c4dae711ea8cbc24577cc460df4eabad26090758bb375946a6fcd29dedf69` | |
| `0444/angle-135.pages` | [0444: Where a radial gradient is centred](../experiments/0444-where-a-radial-gradient-is-centred.md) | 398,470 | `754b40d7f586840eb3daee878a1d705d591ab3e7ae65bf65ba3b9d9395400c05` | |
| `0444/angle-180.pages` | [0444: Where a radial gradient is centred](../experiments/0444-where-a-radial-gradient-is-centred.md) | 398,470 | `25781c800278ddc1de43f6ed9cc4fa5691b1c46b891c4506307ddce85b5c7fd9` | |
| `0444/angle-225.pages` | [0444: Where a radial gradient is centred](../experiments/0444-where-a-radial-gradient-is-centred.md) | 398,470 | `d78a66731a4502254d5ccc10a1e3a147903f49001342f880a7e4fd1fd180968c` | |
| `0444/angle-270.pages` | [0444: Where a radial gradient is centred](../experiments/0444-where-a-radial-gradient-is-centred.md) | 398,470 | `a793bc73927a6b76a6487880354cf932e6ff978bf00643c03216eb5507975ebb` | |
| `0444/angle-315.pages` | [0444: Where a radial gradient is centred](../experiments/0444-where-a-radial-gradient-is-centred.md) | 398,470 | `619f4f8dd0c6d22b63d07765d91e54833425f121119ed44a3d9e4fc59cfd1c9d` | |
| `0444/angle-45.pages` | [0444: Where a radial gradient is centred](../experiments/0444-where-a-radial-gradient-is-centred.md) | 398,470 | `aa6e6bbf7d4bf34ca23cf928360f7445f42584f0a638a0e8499dd1be0ccce2b6` | |
| `0444/angle-90.pages` | [0444: Where a radial gradient is centred](../experiments/0444-where-a-radial-gradient-is-centred.md) | 398,470 | `6d8fd7317de8a760eec55fca1e9ae3d16ba841464dc28b0391c7544efa136fab` | |
| `0445/wide-0.pages` | [0445: A radial gradient in a wide shape](../experiments/0445-a-radial-gradient-in-a-wide-shape.md) | 398,470 | `fc3a4a3b1c01432cc36481e671216161cb54ac226e54f4f6e4c3aabe63cc5f7d` | |
| `0445/wide-225.pages` | [0445: A radial gradient in a wide shape](../experiments/0445-a-radial-gradient-in-a-wide-shape.md) | 398,470 | `be37f77e7d540a288ba6332a6cfa5fb37c865c666338713c5d8fec7d86f19ebb` | |
| `0445/wide-270.pages` | [0445: A radial gradient in a wide shape](../experiments/0445-a-radial-gradient-in-a-wide-shape.md) | 398,470 | `e14bf8fa132f4ed01be0d96416301ab228e3864bcfc296d4321d508e7b8fda0d` | |
| `0445/wide-315.pages` | [0445: A radial gradient in a wide shape](../experiments/0445-a-radial-gradient-in-a-wide-shape.md) | 398,470 | `c4e9c5d9fd73ff8d20beb76592e565b03017927d1265f9677bf0d2aa36e3ee1b` | |
| `0445/wide-45.pages` | [0445: A radial gradient in a wide shape](../experiments/0445-a-radial-gradient-in-a-wide-shape.md) | 398,470 | `944a6348b833e9753198adcd804f8d132b789ec96fbcdddcbbbaf8e69838b7db` | |
| `0445/wide.pages` | [0445: A radial gradient in a wide shape](../experiments/0445-a-radial-gradient-in-a-wide-shape.md) | 398,470 | `e14bf8fa132f4ed01be0d96416301ab228e3864bcfc296d4321d508e7b8fda0d` | |
| `0446/blue.pages` | [0446: Writing a removed background](../experiments/0446-writing-a-removed-background.md) | 398,021 | `229c458c1e5e8d74d752aa189883af451a1753c7f553463e8624dc045b2cb842` | |
| `0446/no-10-19-22.pages` | [0446: Writing a removed background](../experiments/0446-writing-a-removed-background.md) | 397,715 | `f43d21de6bd6c3ba088db063cdc8a8d07910a6698d93143441d0512d80cd9466` | |
| `0446/no-19.pages` | [0446: Writing a removed background](../experiments/0446-writing-a-removed-background.md) | 397,934 | `19a37540de0ac2af032e2743e5f5c7b0f0e21608cf9a77c70576eb38eec0a260` | |
| `0446/no-5-10-19-22.pages` | [0446: Writing a removed background](../experiments/0446-writing-a-removed-background.md) | 397,709 | `52107eb29276c3af918cb39fdfdecc636a9369792b804cd6735e0001f42a4bf2` | |
| `0446/no-5-10-19.pages` | [0446: Writing a removed background](../experiments/0446-writing-a-removed-background.md) | 397,712 | `264a03d5f1c7c77396809bacc7f301d24e60dbdccfe2c08fdd5f64dd64c5e701` | |
| `0446/no-5-10.pages` | [0446: Writing a removed background](../experiments/0446-writing-a-removed-background.md) | 397,800 | `dc996eadc08e590a3bb2a0d6dddc147c211f6eafe99a6c12701b3b6278b6c132` | |
| `0446/no-5-19-22.pages` | [0446: Writing a removed background](../experiments/0446-writing-a-removed-background.md) | 397,925 | `eaa65cd57186a4921b1e91367260b73821b69a6d45835248f68a6789a2dd8089` | |
| `0446/no-5-19.pages` | [0446: Writing a removed background](../experiments/0446-writing-a-removed-background.md) | 397,928 | `86b43132e76b7753e0db63b512bd17b85b0ce18da0582423962421513936c0e1` | |
| `0446/no-5-22.pages` | [0446: Writing a removed background](../experiments/0446-writing-a-removed-background.md) | 398,012 | `a3bf46ea6b35a6f78064326bead360431de292c430a496be91affc93393ea935` | |
| `0446/no-5.pages` | [0446: Writing a removed background](../experiments/0446-writing-a-removed-background.md) | 398,015 | `a7f9e127edb4c9f89a2e9543772b58c6506739dd9c4c95be7ef73899ecfc22a2` | |
| `0447/both-80.pages` | [0447: Writing an image's three sizes](../experiments/0447-writing-an-image-s-sizes.md) | 395,956 | `7a757912829cab3ee7f6fef6940cb1315dad2b325e677d3dd27fe56edd2e40c4` | |
| `0447/field4-80.pages` | [0447: Writing an image's three sizes](../experiments/0447-writing-an-image-s-sizes.md) | 395,956 | `d365d562c97d3fdd183b11b9582611cd861294178d250abf9a805f4d369f770b` | |
| `0447/field9-80.pages` | [0447: Writing an image's three sizes](../experiments/0447-writing-an-image-s-sizes.md) | 395,956 | `d58b718a322ef7de11853f9d0f418be39c103b6ed25dee74b9ce60d511dff182` | |
| `0447/geometry-80.pages` | [0447: Writing an image's three sizes](../experiments/0447-writing-an-image-s-sizes.md) | 395,956 | `ede60495bcd20bdd17ca180b6baeb9f7228263079d69f3730931159ce0d3fc2e` | |
| `0447/original.pages` | [0447: Writing an image's three sizes](../experiments/0447-writing-an-image-s-sizes.md) | 91,240 | `8276979523a753a81dbe06c6e792abe0f549bad808593d5967cf7370e43f6b7a` | |
| `0448/build.key` | [0448: Writing a build's stages](../experiments/0448-writing-a-build-s-stages.md) | 889,263 | `f7b55015a602e2dcd67058a1d8cb34707fb232d220c81b505e2fb06da801f63f` | |
| `0448/no-builds-no-stages.key` | [0448: Writing a build's stages](../experiments/0448-writing-a-build-s-stages.md) | 1,226,704 | `bece001e3caabae26020f4cfedb1c8cde31f71df3165ae094473214a8845e5ca` | |
| `0448/no-builds.key` | [0448: Writing a build's stages](../experiments/0448-writing-a-build-s-stages.md) | 1,226,712 | `294d623641389177195f0790f11fb888ba9441ffae8e6ed6674c60ba7e943fdf` | |
| `0448/no-stages.key` | [0448: Writing a build's stages](../experiments/0448-writing-a-build-s-stages.md) | 1,226,711 | `53710da65459973138caa869797f704ef1f6cc6e8a5098a491a1c2f82ac65117` | |
| `0448/plain.key` | [0448: Writing a build's stages](../experiments/0448-writing-a-build-s-stages.md) | 885,372 | `c5873f36ac3fe9d4300a36d42530f144b27def4a7f620bdd2697327c0c72d800` | |
| `0448/stage-twice.key` | [0448: Writing a build's stages](../experiments/0448-writing-a-build-s-stages.md) | 1,226,727 | `025c9e8231ba177d98a29c6ece9f99e24f9a4f3c164180f1acb8d45a2614afec` | |
| `0449/out.key` | [0449: Writing a build's direction](../experiments/0449-writing-a-build-direction.md) | 1,226,720 | `dd36fd9ccefbd30936575711ad0d7021803714670fa55f3bfe379faf243aa0dd` | |
| `0449/plain.key` | [0449: Writing a build's direction](../experiments/0449-writing-a-build-direction.md) | 885,372 | `c5873f36ac3fe9d4300a36d42530f144b27def4a7f620bdd2697327c0c72d800` | |
| `0450/body-text.key` | [0450: Writing which object a build moves](../experiments/0450-writing-a-build-s-object.md) | 1,226,731 | `762fe83ce8f7edfecb9c3a89bae8468a6aea3c902c4f602e9c5d26eebdca010c` | |
| `0450/build-body.key` | [0450: Writing which object a build moves](../experiments/0450-writing-a-build-s-object.md) | 1,226,731 | `bb88c4c90a9648bd253ade2d3bbe2ee5dc378c61a2fc548f53de72adeec1d763` | |
| `0450/no-build.key` | [0450: Writing which object a build moves](../experiments/0450-writing-a-build-s-object.md) | 1,226,716 | `a725ee0542e73ce9d35a5736ebf21e28481c2aabd9d00c3c18087dfc3201256f` | |
| `0451/body-kind-1.pages` | [0451: Writing what a text storage is for](../experiments/0451-writing-a-text-storage-kind.md) | 395,046 | `06766f90be48d7660c4623e43f477d12e56abc2329f630dbd23f6a3f384f109e` | |
| `0451/body-kind-2.pages` | [0451: Writing what a text storage is for](../experiments/0451-writing-a-text-storage-kind.md) | 395,046 | `28bc3ca37ee5e9bb68b499d87f0f1d0dd2e2a0510ff6e45b7d707bbfe49cb4f2` | |
| `0451/body-kind-7.pages` | [0451: Writing what a text storage is for](../experiments/0451-writing-a-text-storage-kind.md) | 395,046 | `a1bbd350754993c4ce06cf62dd00c5591d89362450a02591f68dffed37bcf4e0` | |
| `0451/header-kind-0.pages` | [0451: Writing what a text storage is for](../experiments/0451-writing-a-text-storage-kind.md) | 395,059 | `bfafeb005db8acc915b472c411ae201a55a45a040ccf1201bf733f9405c9598b` | |
| `0451/header-text.pages` | [0451: Writing what a text storage is for](../experiments/0451-writing-a-text-storage-kind.md) | 395,059 | `20ca7693f5be80f056f7816f3a8901c0c9c9019597661fcad430c5f690a29895` | |
| `0452/original.key` | [0452: Writing a hidden title](../experiments/0452-writing-a-hidden-title.md) | 885,748 | `3e5e6327488684553880bebce619f933855b3727106f0e9f003c61b5c312a432` | |
| `0452/title-hidden.key` | [0452: Writing a hidden title](../experiments/0452-writing-a-hidden-title.md) | 1,223,050 | `060908f4088210d784a3c58326c80bc9279d83557f120d165c903345a0bf0881` | |
| `0453/fill-blue.numbers` | [0453: Writing a highlighting rule's style](../experiments/0453-writing-a-highlighting-style.md) | 459,075 | `06497041da8a6362f1141f61162cb8082037e202bdd3215bee2c51525433930b` | |
| `0453/original.numbers` | [0453: Writing a highlighting rule's style](../experiments/0453-writing-a-highlighting-style.md) | 140,220 | `92adee3afad6131393013c3e77656ad82a57caddfe8913b82aa3f1ea4e78891c` | |
| `0453/text-red.numbers` | [0453: Writing a highlighting rule's style](../experiments/0453-writing-a-highlighting-style.md) | 459,075 | `84e629dd48e9ef23e5a7ccf127c9a1b863140c62fdea4bce23ba4ef256cdf655` | |
| `0454/kind-0.numbers` | [0454: Writing a rule's comparison](../experiments/0454-writing-a-rule-s-comparison.md) | 459,075 | `633dfc57b0546f435408aa55c243caf9fad30250afee60726527e781ee600fd0` | |
| `0454/kind-1.numbers` | [0454: Writing a rule's comparison](../experiments/0454-writing-a-rule-s-comparison.md) | 459,075 | `d68156a7642d774f15c23a1879100f6e4d45952bb8b49a44430933a3fb40ad8b` | |
| `0454/kind-10.numbers` | [0454: Writing a rule's comparison](../experiments/0454-writing-a-rule-s-comparison.md) | 459,075 | `aaf6875f9d08817b6c6f541ea788af4640166976bb8a2beec722c7616d3aa942` | |
| `0454/kind-11.numbers` | [0454: Writing a rule's comparison](../experiments/0454-writing-a-rule-s-comparison.md) | 459,075 | `e4f1efbefe86b9e01cdb22651743d01045c247f0ed7368dc6d564dd6066e17b9` | |
| `0454/kind-12.numbers` | [0454: Writing a rule's comparison](../experiments/0454-writing-a-rule-s-comparison.md) | 459,075 | `c9a6a19704ae97dabada4e1067365f94ea950efae746fe3a0093dfad2d77c883` | |
| `0454/kind-2.numbers` | [0454: Writing a rule's comparison](../experiments/0454-writing-a-rule-s-comparison.md) | 459,075 | `3df996c50773c1e3fb7cb22b27e0fb1d674b29707d3129d76b6759e509010d69` | |
| `0454/kind-3.numbers` | [0454: Writing a rule's comparison](../experiments/0454-writing-a-rule-s-comparison.md) | 459,075 | `af4981591e096ef1e4040d9ab5ca19f8f40d121720f5c0833ef40bd0a2f3b214` | |
| `0454/kind-4.numbers` | [0454: Writing a rule's comparison](../experiments/0454-writing-a-rule-s-comparison.md) | 459,075 | `d2793b03a0ac238028bd7e786ed3f5568f37d38bf4e59ece21f11487988f849f` | |
| `0454/kind-5.numbers` | [0454: Writing a rule's comparison](../experiments/0454-writing-a-rule-s-comparison.md) | 459,075 | `cbddd12b15fcfd93cba6b9d9210580ab00cf533fa796d57842c5b37aa66fbb64` | |
| `0454/kind-6.numbers` | [0454: Writing a rule's comparison](../experiments/0454-writing-a-rule-s-comparison.md) | 459,075 | `1a159532eaddefab44595ca4a87cfbb5dcfab91b900fff5f5a318492a7d73523` | |
| `0454/kind-7.numbers` | [0454: Writing a rule's comparison](../experiments/0454-writing-a-rule-s-comparison.md) | 459,075 | `102c11bdf0a6851f1040da9cc944b5c93fd7c4dbc0bb7275946e7b6fa2f9e055` | |
| `0454/kind-8.numbers` | [0454: Writing a rule's comparison](../experiments/0454-writing-a-rule-s-comparison.md) | 459,075 | `a6344a33e3c24437854ecf52ff3e538402ba4c07489c70e9a4d838e83d5aa79a` | |
| `0454/kind-9.numbers` | [0454: Writing a rule's comparison](../experiments/0454-writing-a-rule-s-comparison.md) | 459,075 | `c3a1867c93918426b8f7b65ac7c04b8dc48304d84e6c068d7172bff6cab26744` | |
| `0455/kind-11-2-3.numbers` | [0455: Looking for a rule's second value](../experiments/0455-looking-for-a-second-rule-value.md) | 459,088 | `811c7bf78f1ff17288974990e97dbf0cb4d8213111acf49cd2080d30801d70f0` | |
| `0455/kind-12-2-3.numbers` | [0455: Looking for a rule's second value](../experiments/0455-looking-for-a-second-rule-value.md) | 459,088 | `791af756163895c91ff5710e46099da0605cc7b4cb34ecb1b1072f24bfa31441` | |
| `0456/baseline.key` | [0456: Writing a chart series' colour](../experiments/0456-writing-a-series-colour.md) | 904,201 | `a595c00777b5da2f922d7efd0241ca7e46e3994814a45107dc0553b0576c080e` | |
| `0456/prop-10.key` | [0456: Writing a chart series' colour](../experiments/0456-writing-a-series-colour.md) | 1,242,316 | `75f8fbd211f1cb5bfd6cd602ea090480b3f2cad12656a107530d42d10c0bedfc` | |
| `0456/prop-11.key` | [0456: Writing a chart series' colour](../experiments/0456-writing-a-series-colour.md) | 1,242,316 | `4c5b7e67ce0b3c32c485e3112e167bb6a8d75c1e41d9e09e36aa9334557a00ff` | |
| `0456/prop-12.key` | [0456: Writing a chart series' colour](../experiments/0456-writing-a-series-colour.md) | 1,242,316 | `3d976635cec881d573d19f9b131a109bab73a05df3a2693d37819f2d14d9de6f` | |
| `0456/prop-13.key` | [0456: Writing a chart series' colour](../experiments/0456-writing-a-series-colour.md) | 1,242,316 | `bbde9ea4362eda138c4de239eec242af35da07b5d3b460c7fee0ca0184da4853` | |
| `0456/prop-14.key` | [0456: Writing a chart series' colour](../experiments/0456-writing-a-series-colour.md) | 1,242,316 | `19bbb19905a4990982b26ac44e6d4e68a638773cd477d8dc9873f431d780ce64` | |
| `0456/prop-15.key` | [0456: Writing a chart series' colour](../experiments/0456-writing-a-series-colour.md) | 1,242,316 | `54cb08559798253b670894408065cf016b18efae5fb89fa809158358dbfa0978` | |
| `0456/prop-16.key` | [0456: Writing a chart series' colour](../experiments/0456-writing-a-series-colour.md) | 1,242,316 | `4ffc1f2db365ddf198d4e8887fb328a52cfebb5e4daa3f6fa55c37a46a92d6ad` | |
| `0456/prop-17.key` | [0456: Writing a chart series' colour](../experiments/0456-writing-a-series-colour.md) | 1,242,316 | `2f437d986bb5b4ac840dc3e301984b56e8c24dbdff57de5ee8e016c733d867f0` | |
| `0456/prop-6.key` | [0456: Writing a chart series' colour](../experiments/0456-writing-a-series-colour.md) | 1,242,316 | `e2301242d1aec3cf0ba896019a9970f558b646b335cc4cb2002637e0fd68e4fb` | |
| `0456/prop-7.key` | [0456: Writing a chart series' colour](../experiments/0456-writing-a-series-colour.md) | 1,242,316 | `64e5a44658db343b7b9f324ae9882ec0a82e683a466deb0a16964f2c1c6ae0ab` | |
| `0456/prop-8.key` | [0456: Writing a chart series' colour](../experiments/0456-writing-a-series-colour.md) | 1,242,316 | `7755dd719dbce83ae4058845eca36204c75f2525ff1d7f168ef26f073de42fde` | |
| `0456/prop-9.key` | [0456: Writing a chart series' colour](../experiments/0456-writing-a-series-colour.md) | 1,242,316 | `be51768b740264c64a011df04bb009707de8dc54d15138f82e19e262a20ca726` | |
| `0457/palette.key` | [0457: A series' colours by chart type](../experiments/0457-series-colours-by-chart-type.md) | 1,242,316 | `79996da5e846cfc7f62e0306a0a4526b13769136aed7355947a5e2d68007265f` | |
| `0457/type-1.key` | [0457: A series' colours by chart type](../experiments/0457-series-colours-by-chart-type.md) | 1,242,316 | `79996da5e846cfc7f62e0306a0a4526b13769136aed7355947a5e2d68007265f` | |
| `0457/type-3.key` | [0457: A series' colours by chart type](../experiments/0457-series-colours-by-chart-type.md) | 1,242,316 | `a43e939582f319c26dfe93e643a5f5a5ad8fb0f3ceafdccab12fb401101e6d41` | |
| `0457/type-4.key` | [0457: A series' colours by chart type](../experiments/0457-series-colours-by-chart-type.md) | 1,242,316 | `5a90575b31ffe586385470c5ed993c185860cd9ac3c6fec6a1423f859ea844c0` | |
| `0457/type-5.key` | [0457: A series' colours by chart type](../experiments/0457-series-colours-by-chart-type.md) | 1,242,316 | `189696ae29f5239ae09e6b7648b3b25d7364c3a538db28cc6f629309bb87ee62` | |
| `0457/type-9.key` | [0457: A series' colours by chart type](../experiments/0457-series-colours-by-chart-type.md) | 1,242,316 | `9a118b4419ca942da895d007825dcff4cf3e892fc4eadae45488a66bd7af2f66` | |
| `0458/line-47.key` | [0458: A series' line in a line chart](../experiments/0458-a-series-line-stroke.md) | 1,242,316 | `fc290bbab5d053f7ce6f2537eb74c1a848925e50481ee630b3e1db33748616fa` | |
| `0458/line-48.key` | [0458: A series' line in a line chart](../experiments/0458-a-series-line-stroke.md) | 1,242,316 | `5b4ee0c8fcf69800a309f6fbf4ad2f1b7496312ffb708433b253f609e6483298` | |
| `0458/line-50.key` | [0458: A series' line in a line chart](../experiments/0458-a-series-line-stroke.md) | 1,242,316 | `68ea36427313b5415b7d3d67d6dbe608a2df99d65dfdb9c6ae215cc9a4f850d7` | |
| `0458/line-51.key` | [0458: A series' line in a line chart](../experiments/0458-a-series-line-stroke.md) | 1,242,316 | `c2aa7b38cd031a0de464fffe99d0cf8eb7920623272defebf0a804e3b6e3dc07` | |
| `0458/line-53.key` | [0458: A series' line in a line chart](../experiments/0458-a-series-line-stroke.md) | 1,242,316 | `577dd11302757239c3bac2301f293bafa2d7d64cad17e599f1f3ebe20bd2bd4c` | |
| `0458/line.key` | [0458: A series' line in a line chart](../experiments/0458-a-series-line-stroke.md) | 1,242,316 | `c1596247fbbddda17f29d5819aeb3de66d150c16796d316ece3747845b1bb47c` | |
| `0459/scatter-54.key` | [0459: A series' points in a scatter chart](../experiments/0459-a-series-points.md) | 1,242,316 | `a8530a6d8574e92a9caf92ab53482fd45cd9ab8ab9f7b4f6246f5de493d41a9d` | |
| `0459/scatter-55.key` | [0459: A series' points in a scatter chart](../experiments/0459-a-series-points.md) | 1,242,316 | `b0e03bd288b6e01659c353c10a36e29c4b67241bd72466ce4dc5d9242e2d47fd` | |
| `0459/scatter-56.key` | [0459: A series' points in a scatter chart](../experiments/0459-a-series-points.md) | 1,242,316 | `3fde49ea7f301660a29e87e6a32adcda53626d00d296f68673ceca2d82e6ac8c` | |
| `0459/scatter-57.key` | [0459: A series' points in a scatter chart](../experiments/0459-a-series-points.md) | 1,242,316 | `3f3c898b64cdadc0e9d5b304f4359f687621b2bda612bd5a51566ecfb08a29ce` | |
| `0459/scatter-58.key` | [0459: A series' points in a scatter chart](../experiments/0459-a-series-points.md) | 1,242,316 | `de0447865e7ba242dbe584ecbd03ffc34b24b47d8a1b0def6e96b040632c2371` | |
| `0459/scatter-s47.key` | [0459: A series' points in a scatter chart](../experiments/0459-a-series-points.md) | 1,242,316 | `44efef06576f02a8ff48239ffedd2ce9558f56fa21b570b000462b3b66da55e2` | |
| `0459/scatter-s48.key` | [0459: A series' points in a scatter chart](../experiments/0459-a-series-points.md) | 1,242,316 | `54d52532f81fbdc860af7a8dd1c96aba01d5a9b2797b79aa9f6fcc8e98cc389a` | |
| `0459/scatter-s50.key` | [0459: A series' points in a scatter chart](../experiments/0459-a-series-points.md) | 1,242,316 | `52829087103f5d7223e20479b25256b1db5647488d999afc861da39e4a161efe` | |
| `0459/scatter-s51.key` | [0459: A series' points in a scatter chart](../experiments/0459-a-series-points.md) | 1,242,316 | `20bf14bc94f43929d1f145c3e1baa5d2549e4d456aea4a88232dd440490d73ac` | |
| `0459/scatter-s53.key` | [0459: A series' points in a scatter chart](../experiments/0459-a-series-points.md) | 1,242,316 | `396113966280642b45430a5d4ddf2d0898e9ae6e6dfd70e40680cae632a5f38b` | |
| `0459/scatter.key` | [0459: A series' points in a scatter chart](../experiments/0459-a-series-points.md) | 1,242,316 | `6edb48a40ea3c4ea3b1b2846272827db3c3558054f56a5c5efd7fa8192dd6955` | |
| `0461/cells.numbers` | [0461: New documents in Pages and Numbers 14.5](../experiments/0461-new-documents-in-14-5.md) | 136,057 | `9c56eab5503fadce84faf9d75c9343e09ddfd58ec43edf983aa4ddba267ae593` | saved by 14.5 |
| `0461/empty.pages` | [0461: New documents in Pages and Numbers 14.5](../experiments/0461-new-documents-in-14-5.md) | 88,266 | `85c2ac607762ca3c1fff21a5a2995423fa8b08c94d0b1261f2961e67bbbe78e7` | saved by 14.5 |
| `0461/hello.pages` | [0461: New documents in Pages and Numbers 14.5](../experiments/0461-new-documents-in-14-5.md) | 88,938 | `acc5ffacde510034d15337b9dda4c8e9c9ff41b5bd4891def40f763e8729ea70` | saved by 14.5 |
| `0464/0030-row-300.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 170,480 | `244fae08ea8cbce5fee51a252e5705d3199cd174b4e6c0725fff71e072a7d47f` | saved by 14.5 |
| `0464/0031-kinds.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 138,795 | `f9c08124d00a71f65307cdbc13f0b980bce9daa0fe947b50ab38b5c76fbbcbdc` | saved by 14.5 |
| `0464/0035-formulas.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 136,937 | `e77ff2d5a4cbc3fa0a5dbf044ee4527b472f2c5a099f7054752974d93f984565` | saved by 14.5 |
| `0464/0036-formats.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 138,515 | `eae8a96193694d3f34608b8d4d5a6c1f52558ca7a66b2e45d2450e90e1b34f06` | saved by 14.5 |
| `0464/0037-two-sheets.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 143,976 | `9a6f4dae085c6041c84278492affcc0407b2582b2fa468e3f3a6ca22e8e22b82` | saved by 14.5 |
| `0464/0043-styles.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 138,339 | `0cf4b5ea560047dbfbcf04b418ef6a241ca5a94e2f7eafb71f423dba03f37388` | saved by 14.5 |
| `0464/0044-merged.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 136,086 | `5a07e7c781e97331809974ba8ef9e1c861b2b9cb3508d241d091512422424e9c` | saved by 14.5 |
| `0464/0045-sizes.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 133,582 | `5e1e2f77f5b3916eacdcfb1ccedff27b2e8d24823fb3fc9e2948028c79b90226` | saved by 14.5 |
| `0464/0047-two-tables.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 142,951 | `63a7a523df85c0ea3c7a61c26667ca389c0ce830507c77c1886d5a6a5be83bfe` | saved by 14.5 |
| `0464/0049-text-box.pages` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 89,694 | `26d35c26ea0202607a43fca7c429ae3cb67130fb754705aae04cc1caaeea613d` | saved by 14.5 |
| `0464/0050-shape.pages` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 91,430 | `5f788061de71efbd20be7fb180671c17210f7ba3ebd6652d691974ee9ef000b7` | saved by 14.5 |
| `0464/0051-line.pages` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 91,932 | `2f12f40a2a762f6a618ccc082fdb6b35d0f042de05ba283d4163ba40d6502826` | saved by 14.5 |
| `0464/0052-table.pages` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 103,074 | `0304fca773c64ad087a40926d0dfa11be504a0b8c7301f618981f3acdf7624e0` | saved by 14.5 |
| `0464/0053-font.pages` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 89,784 | `b717c5c085605f88c1ceb2eac063908779f040b5fdf1cb756e5b2d1bfd1978aa` | saved by 14.5 |
| `0464/0054-sizes.pages` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 90,391 | `0e3214d5c0e879cebe29c03a8d9f4aab77ab27a0479014d76f6cf615c001c342` | saved by 14.5 |
| `0464/0058-tab.pages` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 88,949 | `da78ed48d0a449f96a60339028534b228ed083ae6223d80079c76c4368d90358` | saved by 14.5 |
| `0464/0059-geometry.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 122,808 | `4daad043cebe6337499dffd66197c062c19602152dfee0f9022aac112e467ee8` | saved by 14.5 |
| `0464/0060-headers.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 135,092 | `f7f0e9dc3c2acd8f9e114d24dcd0f98728831abab4fad900daf712e64d9037e6` | saved by 14.5 |
| `0464/0063-sparse.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 209,925 | `b9536fe3b783ac7e302b7b90c51e94b8860a99cb7f818c0c7b68cb7ad20ce0f7` | saved by 14.5 |
| `0464/0064-functions.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 138,179 | `b76045b152ecc449167f99255d9f906f8fee05eaf47630b415d75a937bb21a0d` | saved by 14.5 |
| `0464/0065-cross.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 143,940 | `58fc7bf77e55f39d8a9f04240d6c61e0f93cbcae1193cf88d80ff8d8e0e77204` | saved by 14.5 |
| `0464/0066-if.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 138,407 | `34a5ee240665c21e33126de3faa007a2f99fde032f37f65cce0af5ee60e0f616` | saved by 14.5 |
| `0464/0078-error.numbers` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 135,617 | `dfa7189b9df1f426efda6b8254cfe9443da0c9c1388c613d044109aece6175dd` | saved by 14.5 |
| `0464/0198-book.pages` | [0464: The recipes rerun in 14.5](../experiments/0464-recipes-rerun-in-14-5.md) | 84,519 | `a4eb8a7407c1ae6cbed880f449fd47beeb4f25b9c1941f73aacb661a970ee9cf` | saved by 14.5 |
| `0469/0030-row-300.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 170,107 | `b54f8f2074c6ada662d4eb5afd2a7a83630603b10242430eed16f2af7e320f22` | saved by 16.0 |
| `0469/0031-kinds.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 140,154 | `94863c66322f522d7266c8f68a84d6721244fdbc7210998d8c2c31dc8abb2737` | saved by 16.0 |
| `0469/0035-formulas.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 138,289 | `3a047e91d1b28c9912258cddaa00995dadf2df53978885781f5da7e987604630` | saved by 16.0 |
| `0469/0036-formats.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 139,869 | `7b9ad190d0696684c80baa66d50eb8540c5a577cdb752226fb4cfe89f9f2f111` | saved by 16.0 |
| `0469/0037-two-sheets.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 145,324 | `9c5ced78f037e1b43c308984d00c103ede958669dfb61dfb54f5b8b416fc73ab` | saved by 16.0 |
| `0469/0043-styles.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 139,715 | `032c85601b893a24353e0e5c75be6854808fd1706a515497911ea707dc755581` | saved by 16.0 |
| `0469/0044-merged-run2.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 137,332 | `357ae6ccd743f445961aab7cb686da207bcb4d6466c6c0ebdcc2f28380082657` | saved by 16.0 |
| `0469/0044-merged-run3.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 137,274 | `8ba29dfc5a539a63ef5b3f0e300ebbc7272263f7f73ed78728bc0fdf9b4c1dab` | saved by 16.0 |
| `0469/0044-merged.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 137,361 | `875844ca5fb5198d2fa4f53560b9cac01811c8fc7c91f069922e8474a7e7e4c4` | saved by 16.0 |
| `0469/0045-sizes.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 134,909 | `ba417190d232a96be750861d196d6e85b62be314d7af6a3b4c927056bd91a7d6` | saved by 16.0 |
| `0469/0047-two-tables-run2.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 144,441 | `3dd86fc1e7cd805492e390119e88e11693a939d22dff9ece4cbe626b4aa8cf36` | saved by 16.0 |
| `0469/0047-two-tables-run3.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 144,423 | `17f935bd0e951ac11a3f0a332304d025980ada3860db82e661d579fefd0c1b3a` | saved by 16.0 |
| `0469/0047-two-tables.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 144,809 | `29c85442c7e0adb19bf62de6cce76a687fbf902184a074a442ff795ab8edd097` | saved by 16.0 |
| `0469/0049-text-box.pages` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 91,279 | `8ca069fd620427a04aaa1547b9516c41e3b020b9db93ddb6ffec74dcb8540e5c` | saved by 16.0 |
| `0469/0050-shape.pages` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 93,338 | `caeaf9ee9d9bdc4f8214eb2713bd7cf5d980b43e914a5cf1721b3e79073eefa4` | saved by 16.0 |
| `0469/0051-line.pages` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 93,430 | `181ca1a3a4e345cb896b0b3df8b555afd896f7f07277ad9e9fa35a7385e8b9da` | saved by 16.0 |
| `0469/0052-table.pages` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 104,237 | `73a203aeed403dbeaeea4ad628cffd9c68f535cae9f48fe8cc250b22269b3e3c` | saved by 16.0 |
| `0469/0053-font.pages` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 91,222 | `d4b1ae6e545eb23d8587e00bd0b2db7e5ac5f325afb7c3b6ce75428f98ca2827` | saved by 16.0 |
| `0469/0054-sizes.pages` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 91,862 | `549f209ad9071e02f01da57e0cb30166cb04b6fbed2b581cce5b5b918a199604` | saved by 16.0 |
| `0469/0058-tab.pages` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 90,437 | `e7c8ccd560f3f7bc0c3099196b058e94398ac6173cf6dfaf8e624e144e2029d5` | saved by 16.0 |
| `0469/0059-geometry.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 124,137 | `d5478c2371c2cd1b3bc5199714df20c09d6aff1aa794e6d8225da198a5908d56` | saved by 16.0 |
| `0469/0060-headers.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 136,409 | `031ee4cff0c52bc732d3a219b3dc6e0b6e9aaa2f3508a066f012d805d17a1812` | saved by 16.0 |
| `0469/0063-sparse.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 204,360 | `e058ea1fc62e4c5f26590f066bfb9301678bb70192ad509fe874259ff601457e` | saved by 16.0 |
| `0469/0064-functions.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 139,548 | `2358da00eaddb318de8a46d5790d013972380b39b3cbe1decc480df5a429d712` | saved by 16.0 |
| `0469/0065-cross.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 145,502 | `b00ff75e5ae5ba7108685c8f69fa008588a543cec27b2b67b7be125d3b6ff659` | saved by 16.0 |
| `0469/0066-if.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 139,781 | `c9ab3c347462f25c013a3dfdf6fa7712f3186fa895d5226fda525ba996d2f0bb` | saved by 16.0 |
| `0469/0078-error-run2.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 136,894 | `ba13a3572479b8be8c87ad710ba199853baa6998f64a45697bf9dbaef1b600a2` | saved by 16.0 |
| `0469/0078-error-run3.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 136,894 | `e9f97c154cfb0fcb1eda0d58ad16864da9348d6e1984c4ebf0c321ba17dd1b02` | saved by 16.0 |
| `0469/0078-error.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 136,894 | `f1a28d4259a027a53362ae55a960268c66f9041793a73e2f3abb029918c6546f` | saved by 16.0 |
| `0469/0198-book.pages` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 84,838 | `2a5968d5f5bea150f457ad4c8944dec2b074b230b0083a05d3763ed7346e53d2` | saved by 16.0 |
| `0469/cells.numbers` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 137,366 | `5e920246070b99e5ab6480c222d5830ee204b3d1de9cc91b0d99e2ebf02f46f6` | saved by 16.0 |
| `0469/empty.pages` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 89,785 | `314ed10636c298e2fd2a237ea263526e76327940acba5f838d1159cf8aed014a` | saved by 16.0 |
| `0469/hello.pages` | [0469: New documents in the 16.0 apps](../experiments/0469-the-16-0-apps.md) | 90,429 | `908f31d5fec8299ce16093ad55a0441927f21668521dc36b0896dacaef0b766e` | saved by 16.0 |
| `0473/0047-two-tables-run4.numbers` | [0473: Every scripted sample in 16.0](../experiments/0473-every-scripted-sample-in-16-0.md) | 144,831 | `1dbdf3d712cab7eb46ab8c369017b3e13374df6d94bd5145d7f14fee0638e987` | saved by 16.0 |
| `keynote/0024/empty-a.key` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 882,066 | `912b4de37a6cd26f79bf830b1fe894e608e2cccfefa0cadc626d92e0f0358a85` | |
| `keynote/0024/empty-b.key` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 882,065 | `95a5a1cbe9b95a8b5fb33a29d585e0fc999983bd08a717ed3e3eaa84af118085` | |
| `keynote/0025/empty.key` | [0025: Text on a Keynote slide](../experiments/0025-keynote-title.md) | 882,066 | `912b4de37a6cd26f79bf830b1fe894e608e2cccfefa0cadc626d92e0f0358a85` | |
| `keynote/0025/hello.key` | [0025: Text on a Keynote slide](../experiments/0025-keynote-title.md) | 885,748 | `3e5e6327488684553880bebce619f933855b3727106f0e9f003c61b5c312a432` | |
| `keynote/0025/hullo.key` | [0025: Text on a Keynote slide](../experiments/0025-keynote-title.md) | 885,329 | `dfdbbbb6c86fbf17185fc6cc5aadfbb3837548ca1adf65776634876af729174e` | |
| `keynote/0038/two-slides.key` | [0038: A second slide](../experiments/0038-second-slide.md) | 887,226 | `bb870b75de92baf4860b48c35b4713e52dd7279b9ea646a78fa434972c37ce40` | |
| `keynote/0039/notes.key` | [0039: Presenter notes](../experiments/0039-presenter-notes.md) | 882,091 | `ddcdf332262622a443d14e4e3333955bb9a1e89afe403d579200a0c75875d69a` | |
| `keynote/0046/blank-layout.key` | [0046: A slide's layout](../experiments/0046-slide-layout.md) | 881,763 | `7a69b6c26622fb474a31ea0f542f711d2b48e8518895524637c7d5efce819df5` | |
| `keynote/0067/chart.key` | [0067: A chart](../experiments/0067-chart.md) | 904,209 | `b9f75ae887c62a549d95b8bb83ea26225e7fd6df6a1da15945a4f82e3ffb8f78` | |
| `keynote/0068/textbox.key` | [0068: A text box in Keynote](../experiments/0068-keynote-text-box.md) | 883,350 | `14116e76600381bab60a966e46ef8fd241f3c3e230586e9ecec1cb0c2c93866d` | |
| `keynote/0069/image.key` | [0069: An image in Keynote](../experiments/0069-keynote-image.md) | 882,859 | `e13a4d931b293e7ef2e59dda6c3d3b7362882866a1692a6d15b8af3d8f2b07d9` | |
| `keynote/0070/skipped.key` | [0070: A skipped slide](../experiments/0070-skipped-slide.md) | 882,079 | `c0fbf83985087464103a2a113313b98052e56b3a74887a0342cce5762668a44b` | |
| `keynote/0071/transition.key` | [0071: A transition](../experiments/0071-transition.md) | 881,923 | `205b36b80cb7119bc73fbb6abb5d291bbd6b91c92630e22bb238cebb33ecf1e0` | |
| `keynote/0072/bullets.key` | [0072: Bulleted text in Keynote](../experiments/0072-keynote-bullets.md) | 885,783 | `24f9ef5d878fd684eced45f812bca2de0811149edc978dba6b020ea3b9965088` | |
| `keynote/0073/table.key` | [0073: A table in Keynote](../experiments/0073-keynote-table.md) | 905,768 | `3e992788e9cbf8aa3dfcd95fddf838bb553ea65ad4ab416cf12781ad319e6254` | |
| `keynote/0074/slidenumbers.key` | [0074: Slide numbers](../experiments/0074-slide-numbers.md) | 882,412 | `101a22aded5c991839ae5499565b6ccb87a7a51c16934b47837bd23a981ff7eb` | |
| `keynote/0075/size.key` | [0075: Slide size](../experiments/0075-slide-size.md) | 883,357 | `9bb8e7e15624da2fb5fde0f2c8d7cf074e40054389a3e0f4e4828ed2faa22491` | |
| `keynote/0079/pie_2d-row.key` | [0079: Pie chart](../experiments/0079-pie-chart.md) | 894,238 | `9ab8c109c6a723774599189b630108ebe1cd2ef0c2e26b4a3d966e65d98c0a18` | |
| `keynote/0080/horizontal_bar_2d-row.key` | [0080: Horizontal bar chart](../experiments/0080-horizontal-bar-chart.md) | 908,423 | `14d7be423ea8ee583d92102017296ea3ced8601781fbefd9c504cb6ea1f5da52` | |
| `keynote/0081/stacked_vertical_bar_2d-row.key` | [0081: Stacked vertical bar chart](../experiments/0081-stacked-vertical-bar-chart.md) | 903,387 | `817afc4f6dc5a0f5d672536bfcc64241ffe097198e034c0472603867247c03de` | |
| `keynote/0082/line_2d-row.key` | [0082: Line chart](../experiments/0082-line-chart.md) | 905,882 | `cf74e080cdf9da796bc9a7006e3595415413cc63e961e6b919dffc9f21ae38e0` | |
| `keynote/0083/area_2d-row.key` | [0083: Area chart](../experiments/0083-area-chart.md) | 901,431 | `3ac185e4226622aeb9f011bb14fb8570885cc9baadafa74a6b09e1655c98016b` | |
| `keynote/0084/scatterplot_2d-row.key` | [0084: Scatter chart](../experiments/0084-scatter-chart.md) | 904,986 | `033cad24da6f9284d4a3ae36bb61729c8890929cb1668d9fac506cb241a09b16` | |
| `keynote/0085/vertical_bar_3d-row.key` | [0085: 3D vertical bar chart](../experiments/0085-3d-vertical-bar-chart.md) | 910,311 | `35b7b9fadaf1bf52e7298fe4706aab0d2c5c48de82ada5d3dc28bd3c885f50c1` | |
| `keynote/0086/vertical_bar_2d-column.key` | [0086: Chart grouped by column](../experiments/0086-chart-grouped-by-column.md) | 902,887 | `d984a0a3bc448e7e829f21425a391f69249b3b864bca3422edf508d1330098b6` | |
| `keynote/0087/autoplay.key` | [0087: Auto play](../experiments/0087-auto-play.md) | 882,071 | `d327b5317ae33a9bc1f1d75bdfe3726760fa310fee9db0c44d87e02984398479` | |
| `keynote/0088/autoloop.key` | [0088: Auto loop](../experiments/0088-auto-loop.md) | 881,899 | `0228e23ee7f62b875506c3edc3cc23c0c5ed5064a4f1408b46bc4c8bedcb380c` | |
| `keynote/0089/autorestart.key` | [0089: Auto restart](../experiments/0089-auto-restart.md) | 882,083 | `f8cf2f3bcadd48791948a9d873a981689dcd63ec90d803394d868cf69f083bcb` | |
| `keynote/0091/movein.key` | [0091: The move in transition](../experiments/0091-move-in-transition.md) | 881,932 | `6716c4d646373f9600a2468d67172f66fa96c8d932754930c18f5ce1a75a2726` | |
| `keynote/0092/push.key` | [0092: The push transition](../experiments/0092-push-transition.md) | 881,916 | `e5f50295da20b025e80d068063d8d2791f77b3a0bfc017159242eeb03564bb1d` | |
| `keynote/0093/cube.key` | [0093: The cube transition](../experiments/0093-cube-transition.md) | 882,109 | `9d1e31b7034a49ba01e6ff27430670bb68fb05fb265aef7b60e8dd09bd6a11de` | |
| `keynote/0094/auto.key` | [0094: An automatic transition](../experiments/0094-automatic-transition.md) | 881,921 | `b7ca9e89ce11099a521a0d313623d53a85e0dfdd759610af790aa61c3d44d28f` | |
| `keynote/0095/magicmove.key` | [0095: Magic Move](../experiments/0095-magic-move.md) | 882,146 | `a6295fbc66d62027c7fdc1409561358e64eae376047422b5723d75744fbe2810` | |
| `keynote/0096/textstyle.key` | [0096: Formatting a whole text box](../experiments/0096-keynote-text-style.md) | 886,406 | `3114cbea56cb47227ca4e32a000094f4bfc2e4728cfd2a98ea15d3ed9fa41cf3` | |
| `keynote/0097/rotation.key` | [0097: Rotating a shape in Keynote](../experiments/0097-keynote-shape-rotation.md) | 884,304 | `be292a1ce9396cff4d6ad47cabdbe926765716b7832ed00f9cac9d83448a26e6` | |
| `keynote/0098/opacity.key` | [0098: A shape's opacity](../experiments/0098-keynote-shape-opacity.md) | 883,185 | `02197a48831e0a0e8ab5f8852b9c7ed9525d98c267599340dcbd5319ba2a2e65` | |
| `keynote/0099/reflection.key` | [0099: An image reflection](../experiments/0099-image-reflection.md) | 882,974 | `5ce9c8dd8cbadbb9acf0b50b755ea645775ec3ff539f3f559e28815e012b5667` | |
| `keynote/0100/locked.key` | [0100: A locked object](../experiments/0100-locked-object.md) | 882,866 | `42040b30e5d3da23d4fcd50f0db47c74b7903713857dd039730555ec23b23b8c` | |
| `keynote/0101/notitle.key` | [0101: A hidden title](../experiments/0101-hidden-title.md) | 882,115 | `e93f61dca08de27cad2d00d6e013f2ef6614e96264b9d788eb45efc228af9ff7` | |
| `keynote/0102/description.key` | [0102: An image's description](../experiments/0102-image-description.md) | 882,865 | `934b40284e147ea879e08acd7e33e646ddd02f086df7bae1b999446ade0fb653` | |
| `keynote/0134/cells.key` | [0134: Cells in a Keynote table](../experiments/0134-keynote-table-cells.md) | 927,184 | `636c441088165a31bf27767125822e3249a974ea70eb0dd132b269c3f8ac1510` | |
| `keynote/0135/formula.key` | [0135: A formula in a Keynote table](../experiments/0135-keynote-table-formula.md) | 928,084 | `6e35b80247b66fff7fd36ac6851ef0282e714cac972db8da38dfd6f46d6087b1` | |
| `keynote/0137/currency.key` | [0137: A currency cell in Keynote](../experiments/0137-keynote-currency.md) | 927,372 | `4444a4dff41b2756d2eb976c4deeb801183beddcbf0fc76287fc63f18acedc21` | |
| `keynote/0146/package.key` | [0146: Keynote in the package format](../experiments/0146-keynote-package.md) | 876,707 | `6e070b60fde904ef53683a202c55f05594a4143b9db98264ddda5750dea65d56` | a folder package |
| `keynote/0159/dup.key` | [0159: A duplicated slide](../experiments/0159-duplicated-slide.md) | 885,220 | `a69c19e916ebec88d72da713c68ee5a90f439fd7d566335da38f6455464774b1` | |
| `keynote/0160/move.key` | [0160: A moved slide](../experiments/0160-moved-slide.md) | 886,912 | `1e56d02d37f1b4ddc4cb0135f4695009337753f77782592d38f5a209e421f2a2` | |
| `keynote/0161/delete.key` | [0161: A deleted slide](../experiments/0161-deleted-slide.md) | 885,253 | `69a9ce9bab9ba92a3641d4be6feb4a16e960fa1bb868c783c43d6ba9251dc9fb` | |
| `keynote/0162/ten.key` | [0162: Ten slides](../experiments/0162-ten-slides.md) | 899,035 | `3f54c5ffe49d18c3119149e4b499aaa4641a2e9500a9aab8760677169e04596f` | |
| `keynote/0163/notes.key` | [0163: Presenter notes with several paragraphs](../experiments/0163-multi-paragraph-notes.md) | 882,104 | `89ce29009dc0e47eb557952cc42bbe6cabc075d9fa5e3ccc97f5a0acf3e70bf6` | |
| `keynote/0164/titlebreak.key` | [0164: A title on two lines](../experiments/0164-two-line-title.md) | 887,963 | `069fb567af20efb3a5a3cdaa7c7566554aed883574ab83d1a1bd76da13acb272` | |
| `keynote/0165/layouts.key` | [0165: The first six slide layouts](../experiments/0165-slide-layouts.md) | 891,860 | `79a5d288c711ed0fd1397a4b27f6d777a0eb6792d367637b3aab40fec818a41c` | |
| `keynote/0166/line.key` | [0166: A line on a slide](../experiments/0166-keynote-line.md) | 883,432 | `b927affb08322ac6affda34e08a1a82cb444a483971c5d6297cf8fe884895c4f` | |
| `keynote/0167/shapetext.key` | [0167: A shape with text on a slide](../experiments/0167-keynote-shape-text.md) | 883,998 | `28f515342cd4c5aaf42f9e15eec794c80b4760a238c00ea9443e2aa24d16418f` | |
| `keynote/0168/untouched.key` | [0168: A title never set](../experiments/0168-untouched-title.md) | 882,064 | `b1f0feaf16df38317fd8771690acbd632ec1f3793a1b8444d553e1a39956d8cb` | |
| `keynote/0180/locked.key` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 872,091 | `d4a5bbc5410b003f1bf66480058640487a16473b2351276a63af93584da5753c` | password `pw1234` |
| `keynote/0185/audio.key` | [0185: A sound in Keynote](../experiments/0185-keynote-audio.md) | 888,506 | `a861ecf036250c83cb2c09672a9817368290b964ce6b26f23ffae539a4661a6e` | |
| `keynote/0185/loop.key` | [0185: A sound in Keynote](../experiments/0185-keynote-audio.md) | 888,485 | `b5b6c6db658863de4062d821ea4427e2cc68eceba4d3e10cac7d6888b773ecb9` | |
| `keynote/0185/movie.key` | [0185: A sound in Keynote](../experiments/0185-keynote-audio.md) | 886,685 | `6a410d7d46b169533d31a90c23353968a617fc27b0a3dda07384251f3312d13c` | |
| `keynote/0195/area_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 908,783 | `ca295136836009a00f653628a6f82be48df46723b5c617274e8ddae9d09a8eec` | |
| `keynote/0195/horizontal_bar_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 920,011 | `3673a40e6af8871278194641d0acad58bb55c42b823f12c5f2dcc0b4f2a85cee` | |
| `keynote/0195/line_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 922,511 | `856b1c9c519dfd9763305b188a204193d8f2f23e91b1b6740627557cc5a5dff6` | |
| `keynote/0195/pie_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 895,932 | `42f7a82025bde3b1de472f88531c667792674000152457ba6a64b449c6c7019b` | |
| `keynote/0195/stacked_area_2d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 901,894 | `7ce21e61adc4656713148bd8288846b8ed31e8cafef288f30dd5083a0ddc4d64` | |
| `keynote/0195/stacked_area_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 905,564 | `eccf52eb6d9debc7044f389a794eb30966a7fa83b72d96b5c78eabe256cb96ad` | |
| `keynote/0195/stacked_horizontal_bar_2d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 905,423 | `21d592d2e92faca1d4d3cafc27802a494fb99d2a0353d53c5b74f3353b9e7d82` | |
| `keynote/0195/stacked_horizontal_bar_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 925,772 | `5749437e915de91093dc3a7c9da7113eee37995d02ba7a963872a31ae5d1b543` | |
| `keynote/0195/stacked_vertical_bar_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 909,491 | `ebda2da622ac4d1b64447362c5473d69095ed39dfc63e567cb1be625a7689989` | |
| `keynote/0196/all.key` | [0196: Every transition effect](../experiments/0196-every-transition.md) | 956,390 | `a598fa7d674b2a28a2873aaeb470ea893b70248ce47e9c436e0927cc532bdfc8` | |
| `keynote/0197/default.key` | [0197: The idle time without auto restart](../experiments/0197-idle-time.md) | 882,068 | `35ef91a6ea6e8452af7778f1d523e9cb819a38c184d148e2549323df73cfa450` | |
| `keynote/0197/idle.key` | [0197: The idle time without auto restart](../experiments/0197-idle-time.md) | 882,070 | `70aa8eea1d18a49dba0320a6427907c137e0e9677730a2ce8324b7c0c3ef4832` | |
| `keynote/0243/body.key` | [0243: A hidden body placeholder](../experiments/0243-hidden-body.md) | 883,827 | `6652f65ac086803e925fbab1d4bf717811318407498444d20d45b8b4bd5c8520` | |
| `keynote/0243/no-body.key` | [0243: A hidden body placeholder](../experiments/0243-hidden-body.md) | 883,943 | `c7d7551b9bf10ab1fa2e8da76fc0f4964aada43f3e5688766bf1dc7af3c49228` | |
| `keynote/0257/build.key` | [0257: A build](../experiments/0257-build.md) | 889,263 | `f7b55015a602e2dcd67058a1d8cb34707fb232d220c81b505e2fb06da801f63f` | |
| `keynote/0257/plain.key` | [0257: A build](../experiments/0257-build.md) | 885,372 | `c5873f36ac3fe9d4300a36d42530f144b27def4a7f620bdd2697327c0c72d800` | |
| `keynote/0263/build-out.key` | [0263: A build-out](../experiments/0263-build-out.md) | 889,262 | `1c05e163431e53caf4634f134a6ae17b40592c5da286a2533c6617b2499128e2` | |
| `keynote/0264/action.key` | [0264: An action build](../experiments/0264-action-build.md) | 889,267 | `ce9e081278b3f946a875352b7592667b8f4879e766a953de2d9b4dc1bd6c5e3c` | |
| `keynote/0271/plain.key` | [0271: A dynamic background](../experiments/0271-dynamic-background.md) | 882,060 | `1ddcdbfe366a7f435e5eb48f353fc1fdaee0b43039f085541168b625d252ca59` | |
| `keynote/0272/self-playing.key` | [0272: A self-playing presentation](../experiments/0272-self-playing.md) | 882,092 | `652970768c781348d0f410f358f55f97fd7abae5fe06583c90e698e1233eb8bb` | |
| `keynote/0472/0024-empty-a.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,475,380 | `3774d3ed4a547439c26f625cbe37a2d32053b0581fc82c61b6fb30a948f96397` | saved by 16.0 |
| `keynote/0472/0025-hello.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,479,034 | `0cb0298d8219b35a65d484c51971c42cb95acc973e9a3450c70eec03dd336063` | saved by 16.0 |
| `keynote/0472/0038-two-slides.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,480,499 | `29702babf323e196abb3359784a33a57fdac4abfac052d245438eb17b201884a` | saved by 16.0 |
| `keynote/0472/0039-notes.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,475,377 | `f83cd3fa8935e229aca0b7b9123cb822f7eddd1656f1c1fa902c965e61d2f76b` | saved by 16.0 |
| `keynote/0472/0046-blank-layout.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,475,047 | `d08296106de5cdcc39576aeed9653310dbd77440caf947a7df584b0caf2b354f` | saved by 16.0 |
| `keynote/0472/0067-chart.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,497,479 | `a49c0da367bd4e494d8bdeda961b46ade3fc5a8fb3f53cce8f43bd890ed9845e` | saved by 16.0 |
| `keynote/0472/0068-textbox.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,476,661 | `793332c3edc00f5a34d9387f039aa252cd8693ad2784a1d29f3bfc3bd6274832` | saved by 16.0 |
| `keynote/0472/0087-autoplay.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,475,345 | `7e809e9f08031c3844fe22180f944b97c06a962de9ab64b810b9b9942ded170f` | saved by 16.0 |
| `keynote/0472/0091-movein.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,475,361 | `6aecae781e2d231ff004824b5fdcc67c4dc64826df247c9051baeab563531b25` | saved by 16.0 |
| `keynote/0472/0096-textstyle.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,476,678 | `79a4dd9574e4c3db9fb415faff86a171de3f938e602f59e0883beb6f7f061ba1` | saved by 16.0 |
| `keynote/0472/0159-dup.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,478,467 | `b6becd6d50a1846c1b48c89373fd1cff27b3749a99b64e3d0fc14ac3ca608a3a` | saved by 16.0 |
| `keynote/0472/0196-all.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,549,678 | `12f7c65bc18aee64bea5f2981730ae2d829ad15527fe337ee4e2d09d714ce421` | saved by 16.0 |
| `keynote/0472/0197-default.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,475,363 | `3208e5aeba00ebf80b00a98384449ea8f746f592d5afbf25e9fc186f5d4881b4` | saved by 16.0 |
| `keynote/0472/0197-idle.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,475,361 | `8b560784f2ecf6f1459ee70a7fa3629dbde6a046b014dd5f9cb1b3cae05c56cb` | saved by 16.0 |
| `keynote/0472/0243-body.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,477,232 | `1307699c1c7c04137eb7d07a8c5d67355c5957a8f757a84d374300d12afdb2af` | saved by 16.0 |
| `keynote/0472/0243-no-body.key` | [0472: Keynote 16.0 with the test theme](../experiments/0472-keynote-16-0-with-the-test-theme.md) | 2,477,220 | `68ea3c2b41439e97784888a9c005985725d64c32ca8389f1c50b17c4a5bc7205` | saved by 16.0 |
| `keynote/0474/0024-empty-a.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,474,158 | `4e7c027bbfc54d62762bb4eccfe03ae1237a5d199aa39271bdc8e25480526bee` | saved by 14.5 |
| `keynote/0474/0025-hello.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,477,810 | `ae370aea444495215fefa78b3d3dd04480a98632c68105e799ea1838ef9a0530` | saved by 14.5 |
| `keynote/0474/0038-two-slides.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,479,283 | `cfbf072d0c00de0cd12f85300aa72bd857517924b5249d9d0c7b3811b1e7ed95` | saved by 14.5 |
| `keynote/0474/0039-notes.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,474,127 | `9dce747c190c40e812470daece0ac631792a855a9ad0b0ada679cc377a01ff2a` | saved by 14.5 |
| `keynote/0474/0046-blank-layout.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,473,846 | `7311499dd2e992109b24142f7f7bf214b34f7799073317ac7884ccd5bfa114b6` | saved by 14.5 |
| `keynote/0474/0067-chart.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,496,262 | `e0d4fb54b975d01bf9bf5a01e5a8a2b5a34ac2b844829488e598f01edc636ee9` | saved by 14.5 |
| `keynote/0474/0068-textbox.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,475,436 | `61b1c5cb535240e692204083370bc55cddea6c725ae9608f453c87a02ac8e3c3` | saved by 14.5 |
| `keynote/0474/0087-autoplay.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,474,147 | `7e3f766915cf579356f299e9b0a1e16b15c899295dcf98d390816e038711d5ce` | saved by 14.5 |
| `keynote/0474/0091-movein.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,474,143 | `190fe63dbcbc35867c1f5eb24e90ff9e545741d0a947c743fb81f4027b029f53` | saved by 14.5 |
| `keynote/0474/0096-textstyle.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,475,364 | `f1a3d2e3b402e2c7adaddfd5873f820403ec5856585a7a73dc18629b2cfe7655` | saved by 14.5 |
| `keynote/0474/0159-dup.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,477,043 | `3a72ecf3cbe98ee48b952d09c838bc1c508e649d26a119efa9167e9b5882a40a` | saved by 14.5 |
| `keynote/0474/0196-all.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,546,832 | `0a2e6b967eab99b454f1ec3a62bed3337c94502077b42e3f537742ecb18569aa` | saved by 14.5 |
| `keynote/0474/0197-default.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,474,128 | `dd183e7dcfb1e3b95cd6c0601121f2c0ddf8f9abdd621599894e0c1fdc6bf71d` | saved by 14.5 |
| `keynote/0474/0197-idle.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,474,120 | `2b06b44eb3c46927c55a2bd4a5ceb00727783ca6b069bc8aacc7965d25193682` | saved by 14.5 |
| `keynote/0474/0243-body.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,476,027 | `15db9e3befc2e25c79a4c0ef35364ef778c738d2c01677712161772837bf2c36` | saved by 14.5 |
| `keynote/0474/0243-no-body.key` | [0474: Keynote 14.5 with the test theme](../experiments/0474-keynote-14-5-with-the-test-theme.md) | 2,476,009 | `fb905584c3975f4efc7958310d419c3c5c171baad4006c67272a6d5768f61ca5` | saved by 14.5 |
| `release/14.5/0001/empty-a.pages` | [0001: An empty document](../experiments/0001-empty-document.md) | 88,272 | `2331d6f04f9964fd52af3c143727d40ebf7353ecafb7d9ea9594a84e49648c21` | saved by 14.5 |
| `release/14.5/0001/empty-b.pages` | [0001: An empty document](../experiments/0001-empty-document.md) | 88,273 | `a33cc0c5c76d6076d9f6ead28731ba15cab572247119ead3050565a32e3423bb` | saved by 14.5 |
| `release/14.5/0002/hello.pages` | [0002: One word](../experiments/0002-one-word.md) | 88,943 | `bc9ddfb93b515d55d086a919c4a8ea40addadf347e5a5b7e29193fc6efb60465` | saved by 14.5 |
| `release/14.5/0002/hullo.pages` | [0002: One word](../experiments/0002-one-word.md) | 88,948 | `d2d1efb67b6d3b5e58a4512a8b16e63404cbc0893f6acdab42074e28d719ce2e` | saved by 14.5 |
| `release/14.5/0003/blabaer.pages` | [0003: A word that isn't ASCII](../experiments/0003-non-ascii-word.md) | 89,205 | `0418adef98c34fe2ad04fac20945355df7097dcf1c6698e302a397d43e6cda69` | saved by 14.5 |
| `release/14.5/0003/emoji.pages` | [0003: A word that isn't ASCII](../experiments/0003-non-ascii-word.md) | 88,900 | `ff0b242a9f0f60ca3875eb4c35d76ea19ba3900f6d11a4ad4fcf7f3d41bc7e7a` | saved by 14.5 |
| `release/14.5/0004/emoji-large.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 90,117 | `434fccb65c978723218b0da19512ecad3e68e1024b3ae71057f621d29a4f899a` | saved by 14.5 |
| `release/14.5/0004/emoji-plain.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 89,450 | `71ac470ece51926f04d017f6075f417923c1f40aeba6c716892b46e6ef96d6f5` | saved by 14.5 |
| `release/14.5/0004/large.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 90,586 | `8d45eec1e70e424bc42b7a149f1d112611e5781dd1d21fb8cf932a0da31d94f3` | saved by 14.5 |
| `release/14.5/0004/plain.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 89,543 | `5e6f63a4caefa4503ad47722652a30bc933ddcbe0c800afb9f36ce369238e980` | saved by 14.5 |
| `release/14.5/0005/one.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 89,095 | `20f3d129d12d1729790e976cbbe15e71646241f6cea36e182175aa897e44afa5` | saved by 14.5 |
| `release/14.5/0005/three-cr.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 89,628 | `9cee87e53ba2e405ac27dd220ca5a4ff651effcaa194967a5bc210d08614ef8f` | saved by 14.5 |
| `release/14.5/0005/two-cr.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 89,069 | `65d3de1ab71f53d86446f420904681c12fe97e472a47087d5e4d570d6ecaf140` | saved by 14.5 |
| `release/14.5/0005/two-lf.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 89,070 | `098f87db86056cbfc970d21b60afc0e68cf102d8f90cc53bba81d9581617b3ea` | saved by 14.5 |
| `release/14.5/0013/blue.pages` | [0013: Text colour](../experiments/0013-text-colour.md) | 89,924 | `327c4374b736fd67d0986804aff8bd4909fa2434fd440fca1f2a14d59e75e178` | saved by 14.5 |
| `release/14.5/0013/mixed.pages` | [0013: Text colour](../experiments/0013-text-colour.md) | 89,851 | `dc0fa17b66e7ccc62e0a1a3db1c8911d603b6dd63687a5de7a0bee2b3e9bdf3f` | saved by 14.5 |
| `release/14.5/0013/red.pages` | [0013: Text colour](../experiments/0013-text-colour.md) | 89,904 | `73cc897fa65a4b6a894b96e515b6d9f3aeefeacd1746da90c4d1cad5920df942` | saved by 14.5 |
| `release/14.5/0020/plain.pages` | [0020: A table](../experiments/0020-a-table.md) | 88,801 | `dd14a363cd2cc256a9daf426985f8cff03e1923f9a0c55eb6cd6dc3cc887f1ad` | saved by 14.5 |
| `release/14.5/0023/image.pages` | [0023: An image](../experiments/0023-an-image.md) | 89,680 | `fbdc4a1754d39016207f5a2f70ee2d584156179d0745fad770e14cebd13463d5` | saved by 14.5 |
| `release/14.5/0023/plain.pages` | [0023: An image](../experiments/0023-an-image.md) | 88,800 | `ed57dc5bb8fb3dfc7fde852f56990af09fc59c29336035589334ca42170f65ad` | saved by 14.5 |
| `release/14.5/0024/empty-a.key` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 2,474,158 | `6b649651df833db19fbb4ee117c73dfbf970adac518a33a274d0093cbe0148f3` | saved by 14.5 |
| `release/14.5/0024/empty-a.numbers` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 135,237 | `b5a67ffec0fb7e05565f4a5ababeda83a618796f19be693ba76b0ead7272ab29` | saved by 14.5 |
| `release/14.5/0024/empty-b.key` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 2,474,160 | `638822ed09af3fef61f448fc990cf464efe2964f3507eafb06782c5e04de5fd2` | saved by 14.5 |
| `release/14.5/0024/empty-b.numbers` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 135,397 | `91a30c289bc1fe348d867243623274e937297852b562dcecbdb284e8e57b459a` | saved by 14.5 |
| `release/14.5/0025/hello.key` | [0025: Text on a Keynote slide](../experiments/0025-keynote-title.md) | 2,477,808 | `0030eb7ff6eaca7ab64602b7b5675b65e6f94842a8c87769bc81eece3625e9d2` | saved by 14.5 |
| `release/14.5/0025/hullo.key` | [0025: Text on a Keynote slide](../experiments/0025-keynote-title.md) | 2,477,384 | `014472b5dd272345e24480ff250f6790c62ed276a2af8810688c230d492d7ef9` | saved by 14.5 |
| `release/14.5/0026/cells.numbers` | [0026: Cells in Numbers](../experiments/0026-numbers-cells.md) | 136,068 | `6ad2591a523ce48c9e3a47162a4e1f412a88f6836cb2a3eb49ef70ae67cebf68` | saved by 14.5 |
| `release/14.5/0030/row-300.numbers` | [0030: A second tile](../experiments/0030-tiles.md) | 170,433 | `bd5b3b6e8f1687f919b50a702626a92cc524f24ad0e7c0f33ca26e21e420316a` | saved by 14.5 |
| `release/14.5/0031/kinds.numbers` | [0031: Kinds of cell](../experiments/0031-cell-kinds.md) | 138,800 | `c80225ab2705f062a68b1acf4d0d484e8b9d781850511fc3b1c2dfab0d4744e9` | saved by 14.5 |
| `release/14.5/0035/formulas.numbers` | [0035: Cell references in formulas](../experiments/0035-formula-references.md) | 136,926 | `b2fa924f31b9a79d8c13034b05b50baea63a11466b69c7324b90fe3f6322cd1a` | saved by 14.5 |
| `release/14.5/0036/formats.numbers` | [0036: More cell formats](../experiments/0036-more-cell-formats.md) | 138,526 | `328a1ebd8f124ce8f11348ce93d4b928fbebfa91c266d7cc4e86c5f65f48f0cd` | saved by 14.5 |
| `release/14.5/0037/two-sheets.numbers` | [0037: A second sheet](../experiments/0037-second-sheet.md) | 143,988 | `1afd5c0089e207336e5d91df4f91d5386f686c2154fdf52c971c2d33f1d5174e` | saved by 14.5 |
| `release/14.5/0038/two-slides.key` | [0038: A second slide](../experiments/0038-second-slide.md) | 2,479,289 | `6c4981617edae96a4b90e436193cc1434316a170323c8bb76a6a9a128abeb49e` | saved by 14.5 |
| `release/14.5/0039/notes.key` | [0039: Presenter notes](../experiments/0039-presenter-notes.md) | 2,474,149 | `a51c62802122a72462651d41022bd2da2ba11c3428727be90299325f3f88616e` | saved by 14.5 |
| `release/14.5/0043/styles.numbers` | [0043: Cell styles](../experiments/0043-cell-styles.md) | 138,340 | `4aeeb1b35e8e14d6d7d24b52699aba5ea8ab59d5e911d0fd772834e4f5d4d9f1` | saved by 14.5 |
| `release/14.5/0044/merged.numbers` | [0044: Merged cells](../experiments/0044-merged-cells.md) | 136,078 | `02be149926ed8108d013179d73ee73e52ea3f73750a297a7f94879cfe99a4670` | saved by 14.5 |
| `release/14.5/0045/sizes.numbers` | [0045: Row and column sizes](../experiments/0045-row-and-column-sizes.md) | 133,580 | `db693e94eccd5956302d711ee10ea6e198c36b759dc1f3e3ae6268001b9c1c6b` | saved by 14.5 |
| `release/14.5/0046/blank-layout.key` | [0046: A slide's layout](../experiments/0046-slide-layout.md) | 2,473,829 | `7a5b6c95fe911b32aae40c13f69dbc2389925a7976ef2e3dedcf7554f7dd642b` | saved by 14.5 |
| `release/14.5/0047/two-tables.numbers` | [0047: A second table on a sheet](../experiments/0047-second-table.md) | 142,986 | `06e2d0d17f15a10e024c7fe10539400dbe9e1e35f075edc4ec7885d22775a82d` | saved by 14.5 |
| `release/14.5/0049/text-box.pages` | [0049: A text box](../experiments/0049-text-box.md) | 89,700 | `589ae32266e572844e68578497a16ae4a22efd570f5279238188dbeaa6be2966` | saved by 14.5 |
| `release/14.5/0050/shape.pages` | [0050: A shape](../experiments/0050-shape.md) | 91,436 | `d9e47421b3966eb5b69413ee3d9dbce93972a9eccc15f99612c5372ff0df6d2b` | saved by 14.5 |
| `release/14.5/0051/line.pages` | [0051: A line](../experiments/0051-line.md) | 91,941 | `62445c70f0968d46588c9e3f5c4edb98abb286a6446940343e1c4a5e1b2e4d29` | saved by 14.5 |
| `release/14.5/0052/table.pages` | [0052: A floating table](../experiments/0052-floating-table.md) | 103,059 | `73b905d6577b5d89838b1eab8455f143beab9f4e5c0898c871ee1ebade728e4a` | saved by 14.5 |
| `release/14.5/0053/font.pages` | [0053: A different font](../experiments/0053-font.md) | 89,792 | `dfc418f8fc13e0b07753f0be6b0da5350938c708b877148ae9f0b6e9ed38b97d` | saved by 14.5 |
| `release/14.5/0054/sizes.pages` | [0054: Shared sizes](../experiments/0054-shared-sizes.md) | 90,389 | `8770e87eb3d198eeb76b05d48ca6586411d8ba029524e2a8cf4e0f36add2f05d` | saved by 14.5 |
| `release/14.5/0055/size.pages` | [0055: Resizing an image](../experiments/0055-image-size.md) | 91,256 | `2a6a70b484c6cd471419956eea9fb720a4bb3be739d4b6a2c8a2555c4588425c` | saved by 14.5 |
| `release/14.5/0056/rotation.pages` | [0056: Rotating an image](../experiments/0056-image-rotation.md) | 89,807 | `8ba30617744791feafcb26737014297db6b1d7d5eec0afacecf793807e5b0946` | saved by 14.5 |
| `release/14.5/0057/opacity.pages` | [0057: An image's opacity](../experiments/0057-image-opacity.md) | 89,689 | `f28dbe40ab3cac78d9e798c5bb08414ae3d39323fbcba31a77c748a60c5be3a6` | saved by 14.5 |
| `release/14.5/0058/tab.pages` | [0058: A tab and a non-breaking space](../experiments/0058-tab-and-nbsp.md) | 88,952 | `ec68dbdb52ebcd158cc6f5702794f143d0bc4c5ff6cdb832ac6dcc70cca16d6d` | saved by 14.5 |
| `release/14.5/0059/geometry.numbers` | [0059: A table's position and size](../experiments/0059-table-geometry.md) | 122,809 | `e10bbacb1b22cc69149354859c38b0023850b5ecb24cfb9bb0d3b7d26544249e` | saved by 14.5 |
| `release/14.5/0060/headers.numbers` | [0060: Header and footer rows](../experiments/0060-header-rows.md) | 135,094 | `78f8cce2f7f1ce07054026343c143be61e4daef14a2efa8bdf2cad85e4a73467` | saved by 14.5 |
| `release/14.5/0061/center.numbers` | [0061: Centring a cell](../experiments/0061-cell-alignment.md) | 136,042 | `c9cb2b703793f5d7c2cae42985c7e924889b5160275d0d8f174eed4448ea71e6` | saved by 14.5 |
| `release/14.5/0062/top-nowrap.numbers` | [0062: Text wrap in a cell](../experiments/0062-text-wrap.md) | 135,999 | `6b993080b4d589a19c179360755506e2c74018839c2febc7d99236f2e641a14c` | saved by 14.5 |
| `release/14.5/0063/sparse.numbers` | [0063: Tiles for a sparse table](../experiments/0063-sparse-tiles.md) | 209,209 | `cd6b8ba46801ae4c5db32edcc5c71333e222c1ef601381b97a1c72e8cebe5d2b` | saved by 14.5 |
| `release/14.5/0064/functions.numbers` | [0064: Operators and functions](../experiments/0064-operators-and-functions.md) | 138,176 | `93c379f5d1fefd7dcb8a47b73ae287424c0c0bf936482e5328791b2abee5395e` | saved by 14.5 |
| `release/14.5/0065/cross.numbers` | [0065: A reference to another table](../experiments/0065-cross-table-reference.md) | 144,016 | `d7c2e32dde4c93838fcef14b7110e1c86a36baf4636303efc5192d0b3ea0a2f0` | saved by 14.5 |
| `release/14.5/0066/if.numbers` | [0066: Comparisons and IF](../experiments/0066-comparisons-and-if.md) | 138,409 | `c9471feb999cac3694f6a14d249ebf8f8c16e3166886f5ecf726ecc1be8091a4` | saved by 14.5 |
| `release/14.5/0067/chart.key` | [0067: A chart](../experiments/0067-chart.md) | 2,506,013 | `a365a40025dddace6adf4d7fa984ecfdfc55ea2a242fb2fa8df0cf7f4be5ba2f` | saved by 14.5 |
| `release/14.5/0068/textbox.key` | [0068: A text box in Keynote](../experiments/0068-keynote-text-box.md) | 2,475,440 | `86f9552fa869da2318922002f6a0825fee9151362c746db8529d01f573139ca4` | saved by 14.5 |
| `release/14.5/0069/image.key` | [0069: An image in Keynote](../experiments/0069-keynote-image.md) | 2,474,907 | `4824d3e08d273f0757fab917e4be14629d82c6bf6fcf9011bf2d9d83bd7d975a` | saved by 14.5 |
| `release/14.5/0070/skipped.key` | [0070: A skipped slide](../experiments/0070-skipped-slide.md) | 2,474,127 | `ad1aac0733f62f43922bc9289c844bf883cf950939db68e91b98a3c349a25e2c` | saved by 14.5 |
| `release/14.5/0071/transition.key` | [0071: A transition](../experiments/0071-transition.md) | 2,474,130 | `a18b536d1b1a224269b310475428d5eb10139f74e719b3a1fba023f025d86ac9` | saved by 14.5 |
| `release/14.5/0072/bullets.key` | [0072: Bulleted text in Keynote](../experiments/0072-keynote-bullets.md) | 2,477,844 | `8cacccece63c4310f480e6a3cb1de2514091cf25ea74e7089b4a74ce4d415e2c` | saved by 14.5 |
| `release/14.5/0073/table.key` | [0073: A table in Keynote](../experiments/0073-keynote-table.md) | 2,497,793 | `f2b8008ec852253bbd5637aab934acf710c6c4a7a858b5992cfa46403ceef89d` | saved by 14.5 |
| `release/14.5/0074/slidenumbers.key` | [0074: Slide numbers](../experiments/0074-slide-numbers.md) | 2,474,417 | `840fb48fba304e6b3ea266821c0f0c728f105693bda0dc8943aa1b6cca3b065d` | saved by 14.5 |
| `release/14.5/0075/size.key` | [0075: Slide size](../experiments/0075-slide-size.md) | 2,475,383 | `72059fa01abf2a6ba1ee27ca5e8ca9741a943f7aea6d1c7e32c60ff05f935412` | saved by 14.5 |
| `release/14.5/0078/error.numbers` | [0078: A formula error](../experiments/0078-formula-error.md) | 135,619 | `69c7d07e1e38ffd18d0102b76f970f148e265a20f9c710838113d763d4131e6d` | saved by 14.5 |
| `release/14.5/0079/pie_2d-row.key` | [0079: Pie chart](../experiments/0079-pie-chart.md) | 2,486,296 | `11838600145b606bb7756f4264010c16d13f22df0382ddce004276be7137c475` | saved by 14.5 |
| `release/14.5/0080/horizontal_bar_2d-row.key` | [0080: Horizontal bar chart](../experiments/0080-horizontal-bar-chart.md) | 2,500,493 | `a1f3ffab002078a8589bc4c44f84bb6846d894b9a7ca7331355799bf755fe14e` | saved by 14.5 |
| `release/14.5/0081/stacked_vertical_bar_2d-row.key` | [0081: Stacked vertical bar chart](../experiments/0081-stacked-vertical-bar-chart.md) | 2,495,462 | `71cb26b6a0625d22a2a9c4c6611579632950768c505ee1a6a6fc1f44de0f1103` | saved by 14.5 |
| `release/14.5/0082/line_2d-row.key` | [0082: Line chart](../experiments/0082-line-chart.md) | 2,497,970 | `7c85e2807f7f15ddc91402cd400334071f488c7bc476e58c15a85771347dec44` | saved by 14.5 |
| `release/14.5/0083/area_2d-row.key` | [0083: Area chart](../experiments/0083-area-chart.md) | 2,493,508 | `97ed4face7cd05d73e8c95b296934f58b823eae39fd908ee320b9cdbea3b6aae` | saved by 14.5 |
| `release/14.5/0084/scatterplot_2d-row.key` | [0084: Scatter chart](../experiments/0084-scatter-chart.md) | 2,490,181 | `58561c302f9b2bdb4dab1dea3712c35f0a3635b15ce0485cdc87fab2f47af33c` | saved by 14.5 |
| `release/14.5/0085/vertical_bar_3d-row.key` | [0085: 3D vertical bar chart](../experiments/0085-3d-vertical-bar-chart.md) | 2,512,821 | `5a9cb9d5ec58da140e1641f8f8847824f914047546dca3cf10d6cf4e6c0f40bf` | saved by 14.5 |
| `release/14.5/0086/vertical_bar_2d-column.key` | [0086: Chart grouped by column](../experiments/0086-chart-grouped-by-column.md) | 2,494,999 | `14e61e9a2fb8c60a963fda3a18b53b1531a760d68423a269f7f8336b24e10583` | saved by 14.5 |
| `release/14.5/0087/autoplay.key` | [0087: Auto play](../experiments/0087-auto-play.md) | 2,474,119 | `200196616c2b7717afb09dd64e48961c8f401f6eaa9c39694005ea10c05e26fb` | saved by 14.5 |
| `release/14.5/0088/autoloop.key` | [0088: Auto loop](../experiments/0088-auto-loop.md) | 2,474,151 | `c431c94abddd2a5a97409d8dd499d2097b937a32dbaf6b5c59228d77eed14cd0` | saved by 14.5 |
| `release/14.5/0089/autorestart.key` | [0089: Auto restart](../experiments/0089-auto-restart.md) | 2,473,966 | `258a3b0418a4a37ce4ba3fadef4648d5147fefc5915a2191966fb6e3a92b7329` | saved by 14.5 |
| `release/14.5/0091/movein.key` | [0091: The move in transition](../experiments/0091-move-in-transition.md) | 2,474,172 | `c043bc40e2dac9dc7f639ac652f38402b2b03239486700408e2807881116b70f` | saved by 14.5 |
| `release/14.5/0092/push.key` | [0092: The push transition](../experiments/0092-push-transition.md) | 2,474,130 | `218839d11a4883542382cb29bf10afda259eb08246a33948f4ea094c107001a5` | saved by 14.5 |
| `release/14.5/0093/cube.key` | [0093: The cube transition](../experiments/0093-cube-transition.md) | 2,474,138 | `adb274b7ce8f838f4bbc7193b3959c7d511c376f9175064c7e22bebbac035efe` | saved by 14.5 |
| `release/14.5/0094/auto.key` | [0094: An automatic transition](../experiments/0094-automatic-transition.md) | 2,474,127 | `75ee9ebc509a3f2aafd3039caddf03a8932de310aab1f0e2a644546e94a636da` | saved by 14.5 |
| `release/14.5/0095/magicmove.key` | [0095: Magic Move](../experiments/0095-magic-move.md) | 2,474,202 | `b63035eb74fbc63da1ff9ea96b4c876b2f60e1eea88f652f19048d7d0249d25a` | saved by 14.5 |
| `release/14.5/0096/textstyle.key` | [0096: Formatting a whole text box](../experiments/0096-keynote-text-style.md) | 2,475,357 | `7cfb7cc03ae5a2042c0261324f1165cbfa889fcccc1488c70f10d7f11401eba0` | saved by 14.5 |
| `release/14.5/0097/rotation.key` | [0097: Rotating a shape in Keynote](../experiments/0097-keynote-shape-rotation.md) | 2,476,376 | `34626f7deefb259210107707bf46b38588a2c151db133608db73886a0bf40ce8` | saved by 14.5 |
| `release/14.5/0098/opacity.key` | [0098: A shape's opacity](../experiments/0098-keynote-shape-opacity.md) | 2,475,208 | `cdb20e9f4b42b3e5176db55bfc91acec28a34f84c2b855ebb6040efb9dbf946e` | saved by 14.5 |
| `release/14.5/0099/reflection.key` | [0099: An image reflection](../experiments/0099-image-reflection.md) | 2,474,983 | `55ff95ea956acb74a37cf01d61e481210c60c79ada1762a1134b51e20f5c5009` | saved by 14.5 |
| `release/14.5/0100/locked.key` | [0100: A locked object](../experiments/0100-locked-object.md) | 2,474,929 | `d6cca646bd7b1bbab1d32252896b7a7fdbb403d42cdfb5668964af99cdc09feb` | saved by 14.5 |
| `release/14.5/0101/notitle.key` | [0101: A hidden title](../experiments/0101-hidden-title.md) | 2,474,147 | `503807419303be04485288ecb7f8c597ebfa6baf22dde4bc2024d18292a58b5e` | saved by 14.5 |
| `release/14.5/0102/description.key` | [0102: An image's description](../experiments/0102-image-description.md) | 2,474,939 | `385eb0f2e3660ec361270bddb359b77be69be5c91b5dd6d55428a7b1a228a707` | saved by 14.5 |
| `release/14.5/0103/round.numbers` | [0103: ROUND](../experiments/0103-round.md) | 136,181 | `efe45c4616967c3cfc063101b7b846ee45d7fe7aeaa39adea9b2bfccb0a2fe77` | saved by 14.5 |
| `release/14.5/0104/nested.numbers` | [0104: Nested functions](../experiments/0104-nested-functions.md) | 136,252 | `f2035009c786ff8027f96eaa0c8f5c11fe66521a21ae94efb60975713cccadb1` | saved by 14.5 |
| `release/14.5/0105/whole-column.numbers` | [0105: A whole-column reference](../experiments/0105-whole-column.md) | 136,009 | `1bc0a33b22793588510947a112f108ccf95657abd5ad61b9404a14f789b8c017` | saved by 14.5 |
| `release/14.5/0106/mixed.numbers` | [0106: Mixed references](../experiments/0106-mixed-references.md) | 136,056 | `5df72b714fe5efbde5476cd871d8fb225b3945b66f9e88ee522cff2802845e86` | saved by 14.5 |
| `release/14.5/0107/other-sheet.numbers` | [0107: A reference to another sheet](../experiments/0107-other-sheet.md) | 145,318 | `58bac3f8addf9d478a143e98635c000af975b7da57d31c4ebd99056f6ba5264c` | saved by 14.5 |
| `release/14.5/0108/today.numbers` | [0108: TODAY](../experiments/0108-today.md) | 136,648 | `bdc2089c3065f414cf7d8de049cf1f7fa79040ad0a309f8b3d0faa0d414b80df` | saved by 14.5 |
| `release/14.5/0109/len.numbers` | [0109: A text literal](../experiments/0109-string-literal.md) | 136,025 | `d96310f9b4699fed10630122024c045353f0de2a5dc59a4103d4dcfd34f1d901` | saved by 14.5 |
| `release/14.5/0110/join.numbers` | [0110: A text result](../experiments/0110-text-result.md) | 136,152 | `8f20f65819f89c8fc2c934e60f8772726abbfe0389d03e5a6b9415e4fb2a2366` | saved by 14.5 |
| `release/14.5/0111/percent.numbers` | [0111: A percentage literal](../experiments/0111-percent-literal.md) | 136,055 | `fd770605e440e7b54081d6d7c55471443d1d6db225e8472fda7e96f2176a583a` | saved by 14.5 |
| `release/14.5/0112/minus.numbers` | [0112: Unary minus](../experiments/0112-unary-minus.md) | 136,060 | `ad52c07f2ae676b98045b23cb2a9a6b3c233516cf4744fd821a484ddbc927c9e` | saved by 14.5 |
| `release/14.5/0113/samestring.numbers` | [0113: The same text twice](../experiments/0113-shared-string.md) | 136,074 | `a9d3a28ec03460397df98453cf23fb3c4d8c525cc01db9b432e9ef2bec7a0592` | saved by 14.5 |
| `release/14.5/0114/cleared.numbers` | [0114: A cleared cell](../experiments/0114-cleared-cell.md) | 135,321 | `d89238392260786ab586dd41d06603a19f735148f18467a3a0b8ea116b328741` | saved by 14.5 |
| `release/14.5/0115/newline.numbers` | [0115: A line break in a cell](../experiments/0115-line-break-in-cell.md) | 135,717 | `1a20cd87f30347baa51ad73744cc8c989c94f5a4656747cd966b5c7e8c745416` | saved by 14.5 |
| `release/14.5/0116/extremes.numbers` | [0116: Very large and very small numbers](../experiments/0116-extreme-numbers.md) | 137,358 | `7f3db11af23c5d3bd09406609cf8fff768bf0476f8628f1f4d56518739be6f4c` | saved by 14.5 |
| `release/14.5/0117/dateonly.numbers` | [0117: A date without a time](../experiments/0117-date-only.md) | 136,596 | `5cad903f56d7ea87a6df3996ac8fea4919908bc19f6b3f666b50c0ab25a4c16b` | saved by 14.5 |
| `release/14.5/0118/emoji.numbers` | [0118: An emoji in a cell](../experiments/0118-emoji-in-cell.md) | 135,324 | `4bfbf92a5cdd8bc0cbf8b48583a4d98c5b1fe57f3db003d1a153fd730d6ea555` | saved by 14.5 |
| `release/14.5/0119/sort.numbers` | [0119: Sorting rows](../experiments/0119-sorted-rows.md) | 136,490 | `8dac24f567574e5f8dc119ee1e7eeb2fd58ec256ea5f30b531822897c3814878` | saved by 14.5 |
| `release/14.5/0120/fewerrows.numbers` | [0120: Fewer rows](../experiments/0120-fewer-rows.md) | 101,461 | `a2ec368936c30d784f76ed9422b9da980535dfb41e03b64d94c97770927f9eff` | saved by 14.5 |
| `release/14.5/0121/emptyref.numbers` | [0121: A reference to an empty cell](../experiments/0121-reference-to-empty.md) | 135,625 | `2935d6021cce0a190fc1087d7c9d15ced0166eacf2bb1fc71b323bf4dbb4e79a` | saved by 14.5 |
| `release/14.5/0122/tablename.numbers` | [0122: Renaming a table](../experiments/0122-table-name.md) | 135,194 | `36a47d505dbf583f11b33af23f82701e824f4c36a1e98c3a006d2046fac7496c` | saved by 14.5 |
| `release/14.5/0123/fewercols.numbers` | [0123: Fewer columns](../experiments/0123-fewer-columns.md) | 120,072 | `6d3613e37f4f754a00c27941b7a97f6edb5175753c35f0a11849fc3ec6edcdaf` | saved by 14.5 |
| `release/14.5/0124/sheetname.numbers` | [0124: Renaming a sheet](../experiments/0124-sheet-name.md) | 134,923 | `23dd444571751ccbc8619977ad3e7e5d231f98630b1aeb74118acae1846f4738` | saved by 14.5 |
| `release/14.5/0125/unfrozen.numbers` | [0125: Header rows not frozen](../experiments/0125-unfrozen-headers.md) | 135,135 | `eafb7d0e9016caeaa5e88f00e206b3faaab37ed1b6fd787dc2e0ab229101f041` | saved by 14.5 |
| `release/14.5/0126/origin.numbers` | [0126: A table at the origin](../experiments/0126-table-at-origin.md) | 135,119 | `ca73427eb865393cea2c6abafa3a743f816cfec714ec751a58a6719d845b7000` | saved by 14.5 |
| `release/14.5/0127/textbox.numbers` | [0127: A text box on a sheet](../experiments/0127-text-box-on-sheet.md) | 135,638 | `964f769b189bddea60419bd6ddb3ad2cc96d0c75a98cf9d6f0c71793d3d9db1f` | saved by 14.5 |
| `release/14.5/0128/image.numbers` | [0128: An image on a sheet](../experiments/0128-image-on-sheet.md) | 135,794 | `9fe0fb71fb47b390559db1f1e7cbc7dbd8c209d38b5e8f158983aa1cf05926c5` | saved by 14.5 |
| `release/14.5/0129/shape.numbers` | [0129: A shape on a sheet](../experiments/0129-shape-on-sheet.md) | 135,197 | `d7fdd2bf83c8bfa9fba51ee22c5f538c3e02182446a80af54d8dbbbf10b29c1d` | saved by 14.5 |
| `release/14.5/0130/longtext.numbers` | [0130: A long text in a cell](../experiments/0130-long-text.md) | 139,713 | `e0cd9ad644874e97ab724ff430d8c84f2dd0d2c20c885bd5e951458fee252a64` | saved by 14.5 |
| `release/14.5/0131/cells.pages` | [0131: Cells in a Pages table through AppleScript](../experiments/0131-pages-table-cells.md) | 107,385 | `108504d7bf64aa65715abc4452e4f98a94ec7a14c95929f531a306163ce5809f` | saved by 14.5 |
| `release/14.5/0132/formula.pages` | [0132: A formula in a Pages table](../experiments/0132-pages-table-formula.md) | 107,368 | `5e1ffeb6addfeace96e6e33c9a792c44c6faaf94fdd50219454f3fa6607bcf5d` | saved by 14.5 |
| `release/14.5/0133/merge.pages` | [0133: Merged cells in a Pages table](../experiments/0133-pages-merge.md) | 107,005 | `a2eda7ea31ea213fee8a0fcf0abde35acd65850955cf88d1b683c2456e110d01` | saved by 14.5 |
| `release/14.5/0134/cells.key` | [0134: Cells in a Keynote table](../experiments/0134-keynote-table-cells.md) | 2,506,686 | `cfebc635eec5952fcda8fa065209674bcf96e673cffbd180338955161a703740` | saved by 14.5 |
| `release/14.5/0135/formula.key` | [0135: A formula in a Keynote table](../experiments/0135-keynote-table-formula.md) | 2,506,782 | `d4b2baf9210ab2c2a7ecbaf504a3097e2a20804d1b06a882b759ed498ab97ee1` | saved by 14.5 |
| `release/14.5/0136/headers.pages` | [0136: Header rows in a Pages table](../experiments/0136-pages-header-rows.md) | 105,943 | `28c0b5ebfdbbc09a65789a707f6e20cf83c5e8f14b2da440f1b89fe54280cbf2` | saved by 14.5 |
| `release/14.5/0137/currency.key` | [0137: A currency cell in Keynote](../experiments/0137-keynote-currency.md) | 2,506,862 | `335ed5e191de81ba789f0039a17d16caf6261f8db7caad5b57cf951684d54dc2` | saved by 14.5 |
| `release/14.5/0138/fill.pages` | [0138: A styled empty cell](../experiments/0138-empty-styled-cell.md) | 107,255 | `d748d5fe79b2231f166e267be82452ff51e21e601b77a453837373cf82e52acf` | saved by 14.5 |
| `release/14.5/0139/resaved.pages` | [0139: Saving an existing document again](../experiments/0139-resave.md) | 88,943 | `8221845338c27f48b4d9555debfa2e06311f7876bb3c5f597414e6ef1e9bec39` | saved by 14.5 |
| `release/14.5/0140/edited.pages` | [0140: Editing and saving in place](../experiments/0140-edit-and-save.md) | 89,292 | `ccebea08975eb8ed3f71068f07b995f618b9d7a6f437718973c37638324bc36b` | saved by 14.5 |
| `release/14.5/0141/big.pages` | [0141: A large body text](../experiments/0141-large-text.md) | 388,448 | `38c581fa601442fe1eba9a583a5493babea2f3ac89e2e1eb779e4e1166dafd8f` | saved by 14.5 |
| `release/14.5/0142/twice.pages` | [0142: The same image twice](../experiments/0142-same-image-twice.md) | 90,082 | `421dbc1fa5abea692fe40099e248dfadb17a8c801c7dd91321478b9d8033bc1c` | saved by 14.5 |
| `release/14.5/0143/jpeg.pages` | [0143: A JPEG image](../experiments/0143-jpeg-image.md) | 90,376 | `f31cfa023d74bb57607f784ca39f58dddb35b9756df2c814de471d312c5eeaf9` | saved by 14.5 |
| `release/14.5/0144/odd-name.pages` | [0144: A file name with spaces and ø](../experiments/0144-non-ascii-file-name.md) | 89,691 | `f60ac60e0d54ee5423ded05729115a9f93ef0b3697869c5c71d0b228eac9ea5b` | saved by 14.5 |
| `release/14.5/0145/deleted.pages` | [0145: A deleted image](../experiments/0145-deleted-image.md) | 88,823 | `c542e6210d383826175ad83ca91c18ab296bc72eba0db1726d419a4051493fb4` | saved by 14.5 |
| `release/14.5/0148/large.pages` | [0148: A large image](../experiments/0148-large-image.md) | 1,818,731 | `960c12984d2c116293da970cec9e9e8ccd716f9464ca0368bbc7b73a2d9e59a5` | saved by 14.5 |
| `release/14.5/0149/zwj.pages` | [0149: A family emoji](../experiments/0149-family-emoji.md) | 89,928 | `51052753f7445848b1adb46207f30c165a9c4f5eae0aec5e21bfa8788c3fcd9e` | saved by 14.5 |
| `release/14.5/0150/rtl.pages` | [0150: Arabic text](../experiments/0150-arabic-text.md) | 89,224 | `69818803dd42630ec42c7e13142e7711296f2571bf932a69e85d840748754519` | saved by 14.5 |
| `release/14.5/0151/paras.pages` | [0151: A thousand paragraphs](../experiments/0151-thousand-paragraphs.md) | 120,560 | `adc7cfce84202b356e1270c69d6d15641527582cc89a18ee9b26980bc7e24c68` | saved by 14.5 |
| `release/14.5/0152/sizecolour.pages` | [0152: Size and colour on one word](../experiments/0152-size-and-colour.md) | 90,264 | `7ff6354f10ca58322d2d205a35e5bc70f68f481de6af9f57bcd11495f61cf41a` | saved by 14.5 |
| `release/14.5/0153/defaultsize.pages` | [0153: Setting a size a word already has](../experiments/0153-same-size-again.md) | 89,658 | `77ead8d6a01a2e5bfc70e9dd35f4f2af49d8952687f35a7fe96dda64c0ec0383` | saved by 14.5 |
| `release/14.5/0154/replace.pages` | [0154: Replacing formatted text](../experiments/0154-replaced-text.md) | 89,282 | `90dbc02e1043f056e1d0f03d41a644e2337e148f00972dcf49f70bb6592a491d` | saved by 14.5 |
| `release/14.5/0155/landscape.pages` | [0155: The landscape template](../experiments/0155-landscape-template.md) | 83,340 | `645e80540ff82a8fc52ae7a4864b6abf6c244dc5f323e28e56f4dc42fa4fb243` | saved by 14.5 |
| `release/14.5/0156/layout.pages` | [0156: The page layout template](../experiments/0156-page-layout-template.md) | 88,414 | `07d612eb58699b391b588d0881b7e2e488ed640db1aafc6afe535374e4a1033d` | saved by 14.5 |
| `release/14.5/0157/black.pages` | [0157: The black template](../experiments/0157-black-template.md) | 81,359 | `44de04eb4d50eb3d8403c8be904b542577824e2e76855b1dc8c31c68477e428a` | saved by 14.5 |
| `release/14.5/0159/dup.key` | [0159: A duplicated slide](../experiments/0159-duplicated-slide.md) | 2,477,041 | `b687b77a903952aa0a3cb7fadea4d21725140aed384710791ced913596acd2c1` | saved by 14.5 |
| `release/14.5/0160/move.key` | [0160: A moved slide](../experiments/0160-moved-slide.md) | 2,479,014 | `bd886594291239fbdb636482f51be1750dfc030baf4edf96530fd4190204aee5` | saved by 14.5 |
| `release/14.5/0161/delete.key` | [0161: A deleted slide](../experiments/0161-deleted-slide.md) | 2,477,301 | `ff2c730309274e82a55744cb754cd5cb1c0a1fe9e1288ca291b2517f5a80e38e` | saved by 14.5 |
| `release/14.5/0162/ten.key` | [0162: Ten slides](../experiments/0162-ten-slides.md) | 2,491,039 | `d77d271882b0af56a2ba09d5762020158ef37dfc72696cd65baa76163fae2a59` | saved by 14.5 |
| `release/14.5/0163/notes.key` | [0163: Presenter notes with several paragraphs](../experiments/0163-multi-paragraph-notes.md) | 2,474,163 | `826fe676f905bfe62e7a80d8df9c3b5c2d4cc507084036edc02a6b16609ce9b5` | saved by 14.5 |
| `release/14.5/0164/titlebreak.key` | [0164: A title on two lines](../experiments/0164-two-line-title.md) | 2,480,017 | `894502ff79b024d79431e0a8163965b0d345fd8b9bc1b28ddb4cb630ee9f59be` | saved by 14.5 |
| `release/14.5/0165/layouts.key` | [0165: The first six slide layouts](../experiments/0165-slide-layouts.md) | 2,483,914 | `dbf16bfe5bdeb33f0696fc54583b3d82a497cc0e3f3d33dd0b4bee26e2a267d0` | saved by 14.5 |
| `release/14.5/0166/line.key` | [0166: A line on a slide](../experiments/0166-keynote-line.md) | 2,475,302 | `d44c8ec9d0c69bd59a3026bb322df1abecca14d7487e555cec8491f359e39f96` | saved by 14.5 |
| `release/14.5/0167/shapetext.key` | [0167: A shape with text on a slide](../experiments/0167-keynote-shape-text.md) | 2,476,068 | `0c4905740d3e7584cfec89dd695deb196fbc03efb59f8ee2cfccdc927fc55f49` | saved by 14.5 |
| `release/14.5/0168/untouched.key` | [0168: A title never set](../experiments/0168-untouched-title.md) | 2,474,159 | `0761277b1ee6d3bd34f1c9542db8ac10adc95ef9efe94bcaae18394f9afe7b3c` | saved by 14.5 |
| `release/14.5/0169/checkfalse.numbers` | [0169: An unchecked checkbox](../experiments/0169-unchecked-checkbox.md) | 135,815 | `5fa7d544eedfbd02c696ff1d0a6300f8bf7760aac9d86dd606907ceedd40ce4b` | saved by 14.5 |
| `release/14.5/0170/rating0.numbers` | [0170: A rating of zero](../experiments/0170-zero-rating.md) | 136,513 | `b7fe292c041019e5bca91756b6a9a5cf6d82d2d5c69d55ae81087352091c9d66` | saved by 14.5 |
| `release/14.5/0171/slider.numbers` | [0171: A slider](../experiments/0171-slider.md) | 135,823 | `d0ad215b65c2322ecc106774bf0d432ab2e19b2afb9e8655da1d6c507d383eca` | saved by 14.5 |
| `release/14.5/0172/stepper.numbers` | [0172: A stepper](../experiments/0172-stepper.md) | 135,804 | `04d5cfcd2095ae46abd6138f09f76d698c67b6ec7deff4d798072aceec6cf824` | saved by 14.5 |
| `release/14.5/0173/popup.numbers` | [0173: A pop-up menu](../experiments/0173-pop-up-menu.md) | 135,727 | `b52887edf83fa3013bcc482c4ce7a50d6cef3f4d1b4281463492f9646f3ef330` | saved by 14.5 |
| `release/14.5/0174/negative.numbers` | [0174: A negative number](../experiments/0174-negative-number.md) | 135,637 | `54511c4e035ea40946cdf440335508eae6e6f6155a28dd1edab4306f4d6ca896` | saved by 14.5 |
| `release/14.5/0175/boolformula.numbers` | [0175: A formula with a boolean result](../experiments/0175-boolean-formula.md) | 136,033 | `af107256a71bb91273592263bf918f7b256228f08c34215a148dfa4a2036977c` | saved by 14.5 |
| `release/14.5/0176/numtext.numbers` | [0176: A number typed as text](../experiments/0176-number-as-text.md) | 135,721 | `53a2cd99e26dceeccc82e8863c7e74a69c904da9942513f9e5935462d0a21bae` | saved by 14.5 |
| `release/14.5/0177/described.pages` | [0177: An image description in Pages](../experiments/0177-pages-image-description.md) | 89,707 | `5f9f5e030fc3b0ade8c77e943e262a86b38f6b6046dd8e295e4682b2e2638f2f` | saved by 14.5 |
| `release/14.5/0179/locked.pages` | [0179: A password](../experiments/0179-password.md) | 73,164 | `fad1284311f0f9fbcfdf727b57b8907865bb90b9647beb2f389aea4f0d40ddaa` | password `pw1234`; saved by 14.5 |
| `release/14.5/0179/locked2.pages` | [0179: A password](../experiments/0179-password.md) | 73,164 | `f873945c09de6edefe015d1c76cdbf08c51ed6ea70c0f54662340f713b7453a3` | password `pw1234`; saved by 14.5 |
| `release/14.5/0179/plain.pages` | [0179: A password](../experiments/0179-password.md) | 88,805 | `5ef548f1b8aa5833ce2c36a5a27e7eeffd77eb6ef32c1bff580b49195cbf7a5a` | saved by 14.5 |
| `release/14.5/0179/unlocked.pages` | [0179: A password](../experiments/0179-password.md) | 88,801 | `34ab92324ef62c32ed2090c47d9037a2f26d6447cb3d30c09609aea090c0c113` | saved by 14.5 |
| `release/14.5/0180/accent.pages` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 73,164 | `2aacacf11b55789bf48205e632475a13481a0d489666ea7972edbb36c09da419` | password `påss`; saved by 14.5 |
| `release/14.5/0180/image.pages` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 73,856 | `d31b706031f1be0ca00f2619a174cdd4e609af2c2445baee1e07cc0d5e462085` | password `pw1234`; saved by 14.5 |
| `release/14.5/0180/locked.key` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 2,464,188 | `dcba47efe97d6484eb1dae48c31f3f6ba3b420fedba3d4c01219861ffc8dad11` | password `pw1234`; saved by 14.5 |
| `release/14.5/0180/locked.numbers` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 81,934 | `051757c698fcf9a099457ed1267ed41c80804a08af915197abd7877365ef3154` | password `pw1234`; saved by 14.5 |
| `release/14.5/0181/numeral.numbers` | [0181: The numeral system format](../experiments/0181-numeral-system.md) | 135,713 | `c941faeec36623a02f3dec7fe56e8f9cb7ab4b3bff71314fd056f6650090bbe6` | saved by 14.5 |
| `release/14.5/0181/plain.numbers` | [0181: The numeral system format](../experiments/0181-numeral-system.md) | 135,380 | `db047e29fc4b9022b8f8bf6e845995f59333a20e1a01d07d12efc4eaaf875a07` | saved by 14.5 |
| `release/14.5/0182/transpose.numbers` | [0182: A transposed table](../experiments/0182-transposed-table.md) | 103,722 | `bbc1dbc3e89533394eff3a85050e5c1de66f33f55b6202ec175768aa8cf7470b` | saved by 14.5 |
| `release/14.5/0183/frozencols.numbers` | [0183: Unfrozen header columns](../experiments/0183-unfrozen-header-columns.md) | 135,133 | `ab64dda0ebfbb14394210a6a89065ce58bb0f53fdca6ecc7d5aff6f3d5ba0674` | saved by 14.5 |
| `release/14.5/0184/footer.numbers` | [0184: A footer row](../experiments/0184-footer-row.md) | 135,982 | `9087dd2370f94150cb75a75655776a4dd33dfb1b053e384a093c196d5b2beda7` | saved by 14.5 |
| `release/14.5/0185/audio.key` | [0185: A sound in Keynote](../experiments/0185-keynote-audio.md) | 2,480,537 | `c041a63b2820a86154ea2f51ce27957ad2fc9e266042f9c10ef2f057d6fd14d7` | saved by 14.5 |
| `release/14.5/0185/loop.key` | [0185: A sound in Keynote](../experiments/0185-keynote-audio.md) | 2,480,567 | `6fe367f2c93a97c3a52bbb7db840ea057f7e036483c68ae4628e19198a2f4014` | saved by 14.5 |
| `release/14.5/0185/movie.key` | [0185: A sound in Keynote](../experiments/0185-keynote-audio.md) | 2,478,748 | `d222178fdee7e4924a62c706cc99da84387ffab49e44ff4c8613e35b28c4ebd3` | saved by 14.5 |
| `release/14.5/0188/movie.pages` | [0188: Media in Pages and Numbers](../experiments/0188-media-in-pages-and-numbers.md) | 94,194 | `916b9b4673f1e50f9a00841dd23bb79e1edafc33eac98d917b6d4f0d9caca021` | saved by 14.5 |
| `release/14.5/0188/sound.numbers` | [0188: Media in Pages and Numbers](../experiments/0188-media-in-pages-and-numbers.md) | 141,208 | `20edd8e8cd21bb744691602982afcea298fed4f166154f377aecb71b1e22b87e` | saved by 14.5 |
| `release/14.5/0195/area_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,500,821 | `67c899eac30151ac6b627f7ce76b43e48422ca0c75a04d2ba7d9d0c330aa03ee` | saved by 14.5 |
| `release/14.5/0195/horizontal_bar_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,512,044 | `2e40361b18ace0d8db7ce73b4b082bbcf14e2c2af2278c71c2e81b6909be2503` | saved by 14.5 |
| `release/14.5/0195/line_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,514,582 | `4104d1e74a12f36a575f4c1e5d67823687e60027fe18f9f381d5b3610f507dfd` | saved by 14.5 |
| `release/14.5/0195/pie_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,494,543 | `48bcee0c48da7dbee5fd94ed851fc1a4fd3eb2cc9880ff26b9b2be1b781b600a` | saved by 14.5 |
| `release/14.5/0195/stacked_area_2d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,493,965 | `376dc8928f8f85c883174e7f6c4bebcf3d49a4559cf1fdd059f06296bf01f9ee` | saved by 14.5 |
| `release/14.5/0195/stacked_area_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,497,639 | `054ac427b4517c4aa5b29f9dee070fc4a961ce7c4a150126fbee95a81f82a56a` | saved by 14.5 |
| `release/14.5/0195/stacked_horizontal_bar_2d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,497,489 | `466c59591413acd627e685a4f57f88a727893927cda0e1e6093774147284c5e8` | saved by 14.5 |
| `release/14.5/0195/stacked_horizontal_bar_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,507,145 | `1a8fa5f1c129f9d3daeb54d28f9ea1e5c26cddff0700ee13e68dae561de5cd50` | saved by 14.5 |
| `release/14.5/0195/stacked_vertical_bar_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,501,560 | `8afe7d0e152f781d7353dfd4c6b611d5dd06e53501cd8f8d05fd205dddcb1193` | saved by 14.5 |
| `release/14.5/0196/all.key` | [0196: Every transition effect](../experiments/0196-every-transition.md) | 2,546,859 | `d9d42aab0fb6079b48e3ebe5ddaabff30f6c9a28932c704b499a77699f3a0ece` | saved by 14.5 |
| `release/14.5/0197/default.key` | [0197: The idle time without auto restart](../experiments/0197-idle-time.md) | 2,474,132 | `5b1aa0a80f46b89f2424131cf9dbbb26c269569c1fcadebe1080d63cc92499c5` | saved by 14.5 |
| `release/14.5/0197/idle.key` | [0197: The idle time without auto restart](../experiments/0197-idle-time.md) | 2,474,145 | `93f59890f6ce9f5e5d11b216680d78d7ef81b98203dacf885c2ed33e8a69c763` | saved by 14.5 |
| `release/14.5/0198/book.pages` | [0198: The blank book template](../experiments/0198-book-template.md) | 84,524 | `d224ecccaccd9e5a83688bae21829778da879f5ff0c2f1098f88e5419f02948a` | saved by 14.5 |
| `release/14.5/0223/ABS.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,014 | `fafaaa92ec932654631a48498056b5de0d9d26ba3b17b9b413e2a3d50f3574b1` | saved by 14.5 |
| `release/14.5/0223/AND.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,394 | `5beb790a3681c629a67154ef1aa1fc1332573824414220d744d0f56f37533452` | saved by 14.5 |
| `release/14.5/0223/AVERAGEIF.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,215 | `0cc64bd50a96ffd376a9539aab9beb8950c525d64aee39785afcf30ae5896ba4` | saved by 14.5 |
| `release/14.5/0223/CHOOSE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,071 | `e7e81d162af6e847230353c74ea16a61d7d02b1ea17eebaa22c70432d9ee1913` | saved by 14.5 |
| `release/14.5/0223/CONCATENATE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,155 | `ae155e6e8fd3540b4df98550202e213128946ccb081a1d5af498bc3321f4dbcc` | saved by 14.5 |
| `release/14.5/0223/COUNTA.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,179 | `2d2b8fe0420082b8f1b4af4b434af5ad721d04b38661c97e91ab9eb5369ad546` | saved by 14.5 |
| `release/14.5/0223/COUNTIF.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,181 | `af6951db849c9a0ca8989621a84416000a0069880a2f9aee9ea420a13376d9a1` | saved by 14.5 |
| `release/14.5/0223/DATE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,661 | `9b5c3b6c73df5ab2645837a2b95d8d7ed8fdcf550fd8c371078cde7fddb843b2` | saved by 14.5 |
| `release/14.5/0223/DAY.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,158 | `a439a217984126056855ca49c93cea7256e09d7fe3fcacea5cc397525d522497` | saved by 14.5 |
| `release/14.5/0223/EXP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,132 | `bb9131a1294c2baa59475dbe35411003237362567f3c10ec154cdaa827e2ea64` | saved by 14.5 |
| `release/14.5/0223/FALSE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,438 | `b200cad607f59b26c21a53b7019a7ca976c94b0c71fbb6f544e451a9bce47ab0` | saved by 14.5 |
| `release/14.5/0223/IFERROR.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,058 | `db2920ff4ced0a39c6e5da7a68e4a388af806ef14ba2c71aeae453b32b0d77dd` | saved by 14.5 |
| `release/14.5/0223/INDEX.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,144 | `eec16a0f022456806830107158ccf72bad0688b06146db12ffcf7e865b9c8321` | saved by 14.5 |
| `release/14.5/0223/INT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,027 | `9654b7eb15177f80093f6906280174ec821e1d4c577d5819d86aac92f50fea2b` | saved by 14.5 |
| `release/14.5/0223/LEFT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,067 | `1123814ed37c20b9a9324fac03c1f3e7c9fd36dd8309ce584f559e3fc458a9db` | saved by 14.5 |
| `release/14.5/0223/LN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,056 | `7ddc549f0ae14f0c6c675ecb118786d86c827f9483581b462fa361c2425ee305` | saved by 14.5 |
| `release/14.5/0223/LOG10.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,208 | `5c7d0d441e92e53ec3f33838ae7481c6d2101b7ae21de1496a9fecffea7375d6` | saved by 14.5 |
| `release/14.5/0223/LOWER.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,243 | `8d8a11e8ec68bf32e94d44b91f49dae49dee1883ba9b6ce1e91b7b0be1ed44b2` | saved by 14.5 |
| `release/14.5/0223/MATCH.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,194 | `b880c263eedc519960c1caa988579bfd7a62de61a64c0b98f02379e46327b060` | saved by 14.5 |
| `release/14.5/0223/MEDIAN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,995 | `fbaafbb2c7d176da83cee17d1f4299cd333e2b36447dd5448197e6aa11cffd79` | saved by 14.5 |
| `release/14.5/0223/MID.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,071 | `3021cbd5a44fd4efedf4d9dc28c9640bf637f2a60121a7a0894f36784ca46404` | saved by 14.5 |
| `release/14.5/0223/MOD.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,036 | `e702aacae44107c6d38b6193d1f03061cc92ce00f4dbf2c2f8558a1b5d5c4f85` | saved by 14.5 |
| `release/14.5/0223/MONTH.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,040 | `4af053f822544460d90b4ec8a636c104978b645d593d8a777d3b3f6cafac80c6` | saved by 14.5 |
| `release/14.5/0223/NOT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,490 | `b65f8ab45df13e1ae825efd55bb886765e32fc6908937f4f0fb0d78adef48f3a` | saved by 14.5 |
| `release/14.5/0223/NOW.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,078 | `90087c4326b5c02dc8958f3ec292110d396ba252cccaa49c336fb16910696644` | saved by 14.5 |
| `release/14.5/0223/OR.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,394 | `c5793ac67d030979f922117c07a22ac09f92846f71c2d39c80daeeade1a7b506` | saved by 14.5 |
| `release/14.5/0223/PI.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,105 | `44f02b8991757557a63a3aae28e2cd138a8c068a42d77b88a458a45f80b098d7` | saved by 14.5 |
| `release/14.5/0223/POWER.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,082 | `0a7d8c6f7c999ab5b5f9d68c7a5a5f3ecef781372f23b31fc9fdade5ed0f0f62` | saved by 14.5 |
| `release/14.5/0223/PRODUCT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,054 | `18b3402d33128d90ac244acdfc67f55a67aacd3629a686d01d4579af54ca287c` | saved by 14.5 |
| `release/14.5/0223/RAND.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,203 | `6171a5c3e5c00555d29a784420900c404c5d135f3a84b459c448b778e4fef82d` | saved by 14.5 |
| `release/14.5/0223/RIGHT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,040 | `f202cda7972bc284b5fcfca19b6720190d01c3b15677dee21e43fd8f759ab8d6` | saved by 14.5 |
| `release/14.5/0223/ROUNDDOWN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,195 | `0242c6fb488e62ba76b8876c3e14e4f819cf51fe5b4050396baad66d0cce9098` | saved by 14.5 |
| `release/14.5/0223/ROUNDUP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,183 | `c8b08032c3bc48cf2e9da0b837e1d16b42937e4751fc9dbcab682edb2e67fe4a` | saved by 14.5 |
| `release/14.5/0223/SIGN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,009 | `e0ca0e327ddb2c7507c92ce3ab60e31ef65989df3f10614d8d4252e9c164e563` | saved by 14.5 |
| `release/14.5/0223/SQRT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,011 | `7e0ca32e2e0aed6da654cdd3d7b1099f4364715a8f534d0b8b4378a3fe04e713` | saved by 14.5 |
| `release/14.5/0223/STDEV.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,023 | `d8c6e6e509480e7ca805ec8c10d7861d431abeddf634c5fd8712b81d0eda2cb2` | saved by 14.5 |
| `release/14.5/0223/SUMIF.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,204 | `fa0c4b4854e665aa777e0cd015523eaab34750d31aebdc58504856d913e49233` | saved by 14.5 |
| `release/14.5/0223/TEXTJOIN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,193 | `e31a1aa7ae0274b384d6b0046fa560cf34e4ab35dc28a19bd2caa413ea63f3fb` | saved by 14.5 |
| `release/14.5/0223/TRIM.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,030 | `40529b366371abaf1150023a599fb6beb79d85b54ae03d007f6297dde54b9e6f` | saved by 14.5 |
| `release/14.5/0223/TRUE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,334 | `ff4bb86aa39c6aef09727e4bba4b5554b57ee1c68fbb99e79f7116176f436448` | saved by 14.5 |
| `release/14.5/0223/UPPER.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,277 | `7606f3d3aaefd9221d1d9d103fb17beaa07f5ab66243265e9fc162debae619ca` | saved by 14.5 |
| `release/14.5/0223/VLOOKUP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,280 | `db4fe5ddc479a5b6ba3d6f637b5588d5887d7f07a91f569aab0bf6661d943e64` | saved by 14.5 |
| `release/14.5/0223/XLOOKUP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,236 | `e7de8a5d3888e87e7d5366c9043e273f52f96bfdd7b423adf830f9fdb64b79b2` | saved by 14.5 |
| `release/14.5/0223/YEAR.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 136,274 | `086d56d723611b75069090a98f065ee8539213ffcba387f09c172d4b4203ae3e` | saved by 14.5 |
| `release/14.5/0243/body.key` | [0243: A hidden body placeholder](../experiments/0243-hidden-body.md) | 2,476,015 | `0ae95bd57c7c75065dae981474aa1dcc3fb9328d7e4842b7caf9f4bb0cc12e48` | saved by 14.5 |
| `release/14.5/0243/no-body.key` | [0243: A hidden body placeholder](../experiments/0243-hidden-body.md) | 2,476,017 | `2c1e9ff4b9f2560bacf866fb495bcfd1fe0f8a9c167607cd189d3f89c20f63b6` | saved by 14.5 |
| `release/14.5/0248/ACOS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,051 | `c6e8e25d1bc0d15f069b304cd031a3a725ecdbdec62b047478b9a52b848a532e` | saved by 14.5 |
| `release/14.5/0248/ASIN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,032 | `a094a6e2da7a88968783a3a2482a094d1848e6e2b976482d2e35529d24098311` | saved by 14.5 |
| `release/14.5/0248/ATAN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,238 | `49898c075773555847c02b6ce05139f119521439bf45b4447bc6c1e754acd1a6` | saved by 14.5 |
| `release/14.5/0248/AVERAGEIFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,199 | `e5617723f2fcb1549015d71f3e12e2eec59978f8f4019cf5b0322203318d2111` | saved by 14.5 |
| `release/14.5/0248/CEILING.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,066 | `8206364faf4ba1af83666ddea7fb9afa24ffdc6b3314e76d51d2f0b4d50c39fd` | saved by 14.5 |
| `release/14.5/0248/CHAR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,101 | `b0e316b1cb1d90565c69002db159f5f888278b3184196904fd4fb714b1059ae7` | saved by 14.5 |
| `release/14.5/0248/CODE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,121 | `e10a8770467cd02c393d37137c01c4b263cd492408e2b37eb93f6b2dc81a979f` | saved by 14.5 |
| `release/14.5/0248/COLUMN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,012 | `e8255d94ec38f6d1692439f4523d6d000a9992c324154362fd7dabb3ad4812fb` | saved by 14.5 |
| `release/14.5/0248/COLUMNS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,090 | `7982d4309a116022312971a25c54b5d93b7ce4f7849f8d1b12899dee7259f6c8` | saved by 14.5 |
| `release/14.5/0248/COS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,010 | `cd6342488f2a9eabfb8dfce119142ef61a2c9e1feaf07de3d3aef5e7467e317a` | saved by 14.5 |
| `release/14.5/0248/COUNTBLANK.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,178 | `f28f7a8db8aa6151b23a9c6cdfd94c9a3acd30cf257f08651a9a74a00f44d91c` | saved by 14.5 |
| `release/14.5/0248/COUNTIFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,182 | `9a8016151053078d6abeea00dd7d10e5a66f4287a205e17590070d2bc7fb551f` | saved by 14.5 |
| `release/14.5/0248/DATEDIF.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,253 | `8a5a4b0ab509b04306b7d15151ecc8fa8f73eb625eaf33aeb1c2248795d4047c` | saved by 14.5 |
| `release/14.5/0248/DAYS360.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,378 | `36b9a2cd32835c0ef81b48a991e409ef6f9fb9e657f827b77903cd33ee02b743` | saved by 14.5 |
| `release/14.5/0248/DEGREES.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,144 | `3be49efd219d205f27efb2b7f480dbaf4c795d99161ce5fa225a5f6c9e4e366f` | saved by 14.5 |
| `release/14.5/0248/EDATE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,687 | `a50a5a282d54942c2861d1f8357be33b64b37a1eb4c19d00f012f61f99ebac40` | saved by 14.5 |
| `release/14.5/0248/EOMONTH.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,672 | `e6a4677d9a19b10b4f78207a2942f9478af5914944f978a6c3c44d3dc5952ab8` | saved by 14.5 |
| `release/14.5/0248/EVEN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,007 | `f4b129c375b50b2c5292fe8ed00dcf731ec5d40f40229bf0ab1d291196e7d2e8` | saved by 14.5 |
| `release/14.5/0248/EXACT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,332 | `801fb24e0f69ecece4516a0b703e4c7850295b6e806100c8f52768eb964c6a8a` | saved by 14.5 |
| `release/14.5/0248/FACT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,138 | `349e0887d02bb179425fb3284809b28a266901b2fd67ddfb70ca8ab8fe7c5c5b` | saved by 14.5 |
| `release/14.5/0248/FIND.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,004 | `662f8414d9ebc4aadc086b752a4da406d93f97b39598fe4b07a1cd55d62905fe` | saved by 14.5 |
| `release/14.5/0248/FLOOR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,051 | `c3d8b14e0f5056f0c823b557ba4e7d7faeabfafc7a31840f76d37061960b10ed` | saved by 14.5 |
| `release/14.5/0248/FV.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,678 | `c9fc69001ad47b9ab9dcde3d78f5d8b4ad631cbea28267927b4678e7bdcd62b8` | saved by 14.5 |
| `release/14.5/0248/GCD.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,030 | `f1532eb9ba0c04c0dc5656dcfb612b240c139b7a75df7fdf1bf8506f671efae4` | saved by 14.5 |
| `release/14.5/0248/HLOOKUP.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,253 | `1e194bf5166e15b525067ca691ce3f73d87443be6eee4acad0e6f9d170d239c4` | saved by 14.5 |
| `release/14.5/0248/HOUR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,091 | `f81f08c8eacd50e181b079f7a9c53cce54da10bc346e0de0353eccee7c2ac519` | saved by 14.5 |
| `release/14.5/0248/IFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,109 | `b55a8be31811927254eafbfbff0cc788a5312f5a6690aee350a9ce0ebc042ce0` | saved by 14.5 |
| `release/14.5/0248/ISBLANK.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,342 | `fa892b4075f8a740a4960986923ef30158fc6d748868c1749bd97096fa5edd46` | saved by 14.5 |
| `release/14.5/0248/ISERROR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,379 | `877a4ebaaca6a2646c44e5a7fd2519a42aae266a071973db2b1fbbfeb9153931` | saved by 14.5 |
| `release/14.5/0248/ISEVEN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,340 | `ced644d3e748693a4ed22f9bac68a640cdac911cf5575b287b6ecc6a07eee3dc` | saved by 14.5 |
| `release/14.5/0248/ISNUMBER.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,344 | `730bfae52f01bbf2901ebe8f9f1a01317b4758ed7b4918a3a4f369e3a6798ec9` | saved by 14.5 |
| `release/14.5/0248/ISODD.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,445 | `be3928b13562ad67e9ae37fce3166c0d1859ac7d1401cd685554c70b0f1997f1` | saved by 14.5 |
| `release/14.5/0248/ISTEXT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,451 | `55eaabec5ee8009436fa2d888e3564909c1341408e05e7996b46c606b03fe102` | saved by 14.5 |
| `release/14.5/0248/LARGE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,192 | `59f1bde69b9b8e94f0b5e98d70fe0ed2bdaec7e84b214c96e88091b70a82302c` | saved by 14.5 |
| `release/14.5/0248/LCM.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,021 | `5b09423e4cbb98c23ad719e6dbc7898fd5e2bb424c4c69ee8dca00a7ae3e1258` | saved by 14.5 |
| `release/14.5/0248/LOOKUP.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,211 | `92c11925a4199e680bbc8543ab2e11ee3dadf7516420d466c5189a47d9dcf632` | saved by 14.5 |
| `release/14.5/0248/MINUTE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,164 | `25dff969e23048f081393c6d790d911565090c31195e540ecee19bf069288500` | saved by 14.5 |
| `release/14.5/0248/MODE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,011 | `758e33e4f2d0f3c7d125c98490616af18880557074977e6704df587071281a14` | saved by 14.5 |
| `release/14.5/0248/NETWORKDAYS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,354 | `d427ad8e1c66ae322d616586f69652164bba071f48345d15ae3ed7d176a477dd` | saved by 14.5 |
| `release/14.5/0248/NPV.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,466 | `edc18e2c9339e4d8b2cc18f115f1d7bf2703b6f3a7bc82fa260f53c6a8716bd9` | saved by 14.5 |
| `release/14.5/0248/ODD.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,039 | `01ac224c45e18f6009ef0eb68cded1a3496af0b42a263dfb733fe1a9f052985a` | saved by 14.5 |
| `release/14.5/0248/PMT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,646 | `a57ccbbc85c1baf51a9b5445202022898fe2767f217b9caaa60249034f15cab1` | saved by 14.5 |
| `release/14.5/0248/PROPER.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,386 | `2fa4907e5a6c88496bdf023619ff2f26123523aa9bfd1bc4f77c37165f34e2f4` | saved by 14.5 |
| `release/14.5/0248/PV.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,537 | `3b80ef195c6680bfde81d36ed9b3ff901c05f75d65d1b85118f67688ac6a7f78` | saved by 14.5 |
| `release/14.5/0248/QUOTIENT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,019 | `243212310834d101c0bcf5e898dce8a0fe5400a6bf687559bdb92837d67dc31f` | saved by 14.5 |
| `release/14.5/0248/RADIANS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,057 | `c4eb763620bc9796e3a0a04c97ff44b29de9dd2290e873db3edf17ee73a28ac6` | saved by 14.5 |
| `release/14.5/0248/RANDBETWEEN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,080 | `c77d3db38509a355a4177b39de409c3316c426a1e67eee6b2a01a770de60b997` | saved by 14.5 |
| `release/14.5/0248/RANK.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,180 | `b86ab08b3ef8e9e641a254f3a684ac9d3597c32bc0944c6c1202cfbef5db65c7` | saved by 14.5 |
| `release/14.5/0248/REPLACE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,278 | `ecd767604f6464f07eb0ed581efdab5deb033928629f59f79e68113eb31e816b` | saved by 14.5 |
| `release/14.5/0248/REPT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,267 | `cc14e2990af8cc3e74e07adc6d08fa3554e4a090b98196c439bd3dc7ad6267d1` | saved by 14.5 |
| `release/14.5/0248/ROW.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 135,989 | `ab4cdab6992954cfd6251d9b9c664273524293f7324765c4c8b634d9ba2d5752` | saved by 14.5 |
| `release/14.5/0248/ROWS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,091 | `971bfd4643eb17fa266d30604416de81a9b4d4ee0cc299b8900dd8b631ab6e50` | saved by 14.5 |
| `release/14.5/0248/SEARCH.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,019 | `75aa481c5bffdcb137e642d89cf84d064d9a31ea2abd52abf3286a87e9f169a0` | saved by 14.5 |
| `release/14.5/0248/SECOND.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,133 | `f6669f7a32b66eb09271b5d87961b4c6de3aa1be138ef7dbeb5050616498866e` | saved by 14.5 |
| `release/14.5/0248/SIN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,018 | `ec4cb690771b03cdb7c9f2dcc599aa71b9a9fbbd23e25a11d89429efec10f23d` | saved by 14.5 |
| `release/14.5/0248/SMALL.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,202 | `d96a909ebf4110e89847872bbb3de7e5b97339406d5070a770c1ef4eefd79ba8` | saved by 14.5 |
| `release/14.5/0248/SUBSTITUTE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,268 | `ef89889766cb5de634b22b288b3235eeb8bde0d9c9bb0a15db97e4327a5d8b6b` | saved by 14.5 |
| `release/14.5/0248/SUMIFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,208 | `a9f13950aee561be963f9b30f2f07dc62967bf759392c3fa5d2aefe8c7c7519b` | saved by 14.5 |
| `release/14.5/0248/SUMPRODUCT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,296 | `77ff216cd5bf1e4275e8de09e23429d4e403f469b8332e533a685f89cf1cb0ec` | saved by 14.5 |
| `release/14.5/0248/SWITCH.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,134 | `21bedaf12f36eae844aa785ff5ce9083235a467714754a85fd854656c80bb807` | saved by 14.5 |
| `release/14.5/0248/TAN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,018 | `76ffff0fae5baa5b0eeaeaca4c21508708a0b12c91b13dd3821f776b3792ac14` | saved by 14.5 |
| `release/14.5/0248/TEXTBEFORE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,071 | `217d35daca49b4eeb512314bcd672bb8790b05d35fafff8a2ad417c07a1a7e3d` | saved by 14.5 |
| `release/14.5/0248/TIME.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,004 | `4ef41b9bcfa9f0e47b1bc13523a913e9aea71fcf4c0ffd60d89a9ac67d25a59f` | saved by 14.5 |
| `release/14.5/0248/TRUNC.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,028 | `419077fb23d5f4ee93051821c8288d1e195ec3e67d4352bd73a1f5a89762ed3c` | saved by 14.5 |
| `release/14.5/0248/VALUE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,009 | `e245520f56f9873f72ab892aeb9ba1a9b9d587dc807deaf314133fc080b499c4` | saved by 14.5 |
| `release/14.5/0248/VAR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,020 | `6172fbca196bb14f884da5d37ff7852a379043b89739b1bca2bc56059ae03cf8` | saved by 14.5 |
| `release/14.5/0248/WEEKDAY.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,043 | `cf299877b1526e2b22c8d0ac6effcf6e9159ef5f6db968b968983784a016583e` | saved by 14.5 |
| `release/14.5/0248/WEEKNUM.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,142 | `6a99bdd8df40507a55e42e5568919ff01d34ee5e71bc19c026b755fcb1a157b5` | saved by 14.5 |
| `release/14.5/0248/WORKDAY.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 136,672 | `f49bd9c78d28a53840e10eec69b59688d1fd8f20e3ce26ec004bd84d3ff94ccd` | saved by 14.5 |
| `release/14.5/0248/XOR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 135,999 | `46b43cf89b80edbd0c1e8705fc8480279d8a16f2a4074f3cdf90c96d91790bb1` | saved by 14.5 |
| `release/14.5/0265/MINUTT.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 136,143 | `5553a8ba6b5254b0191bba0dc199541d70f57ce78df493459f6295b130a0cd97` | saved by 14.5 |
| `release/14.5/0265/SUMMER.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 136,042 | `89d79fbd899500bb0c60c05552770e27c1b9bd92f8b0b127350b0ca06a7871ad` | saved by 14.5 |
| `release/14.5/0265/TID.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 136,322 | `ec2b07b68b1f0570a638240ee376944f69d689cc06ab84a21bea98d1228a7a5a` | saved by 14.5 |
| `release/14.5/0265/TIMEVALUE.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 137,189 | `a0affa894370d37ff71b00572ff7ddb69cddcc61add3b7d73083aaca90586517` | saved by 14.5 |
| `release/14.5/0295/baseline.key` | [0295: A chart's title, legend, border and caption](../experiments/0295-chart-options.md) | 2,496,273 | `5207dc68872ff007c8f75f73fd4ae7155ff8b72c275e32220baaa4212fa8c969` | saved by 14.5 |
| `release/14.5/0296/baseline.key` | [0296: A chart's value axis](../experiments/0296-chart-axis.md) | 2,496,262 | `6e8ef84cce1de4ea0a9d615cd1253ea626972393144d05a09408089fc7876629` | saved by 14.5 |
| `release/14.5/0297/baseline.key` | [0297: A chart's category axis, series and text styles](../experiments/0297-chart-category-axis.md) | 2,496,257 | `fac2d8cbc18738d01b4024452fc63e1a73c10ce2ef03fc27cc4b874b0f05eca1` | saved by 14.5 |
| `release/16.0/0001/empty-a.pages` | [0001: An empty document](../experiments/0001-empty-document.md) | 89,786 | `9dc64b68c2555a09faa296d71b3d205ab4c182264b0385a8e815f45a6b6dfed5` | saved by 16.0 |
| `release/16.0/0001/empty-b.pages` | [0001: An empty document](../experiments/0001-empty-document.md) | 89,783 | `72ba1e998dfe71d1ac8a90de63aa0dfed8c8c422d22db4800da3be406bd987a8` | saved by 16.0 |
| `release/16.0/0002/hello.pages` | [0002: One word](../experiments/0002-one-word.md) | 90,425 | `bbf7e843d812bd6e6be5c1b684e50abd6c0e8eb98c457a55565445aea7be6475` | saved by 16.0 |
| `release/16.0/0002/hullo.pages` | [0002: One word](../experiments/0002-one-word.md) | 90,432 | `b11a844fda3dc86b7840bd2e4dc7a9cdf6ca5cff8bcacec1d50c3f4cda79825e` | saved by 16.0 |
| `release/16.0/0003/blabaer.pages` | [0003: A word that isn't ASCII](../experiments/0003-non-ascii-word.md) | 90,689 | `ebc8e57425e09ba7ea27583191b3bd39945e5978ebdef3c09bec5687277e3afc` | saved by 16.0 |
| `release/16.0/0003/emoji.pages` | [0003: A word that isn't ASCII](../experiments/0003-non-ascii-word.md) | 90,388 | `b3dc1f713c273e1f026649db55492da240e9a76d9ad445ccbf6ac1604eaeac76` | saved by 16.0 |
| `release/16.0/0004/emoji-large.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 91,545 | `349e0988adca4c6070557d0a1b4de66bf9a865d29537d272c1dd68ca36b04bb2` | saved by 16.0 |
| `release/16.0/0004/emoji-plain.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 90,933 | `91f2ac30a41703d204d30a4eb9aee3ccf08ece47576e45864e47957efc43c4b4` | saved by 16.0 |
| `release/16.0/0004/large.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 92,004 | `7581bdcdd062f3ce5230fcc1ad9c6edeb209e3f07876fcae665eb72f804ecba1` | saved by 16.0 |
| `release/16.0/0004/plain.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 91,036 | `43fab5225dbb73945615c9f3d8df63a09f7235b9716c6ef1d65364e4554eb87f` | saved by 16.0 |
| `release/16.0/0005/one.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 90,577 | `dfea67ad4fbbf1e69c6dc1156fa3db72915ed781913c16f9627e6db0c6ad1828` | saved by 16.0 |
| `release/16.0/0005/three-cr.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 91,107 | `eaf64fe9e8293efb7292616a9a1022e620bc7c296bffd16f9f76a511ef71a268` | saved by 16.0 |
| `release/16.0/0005/two-cr.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 90,552 | `2b6e0545c34fda6d0fae01da104b1dea8fb459a690ea39848166d2bf35fbd1eb` | saved by 16.0 |
| `release/16.0/0005/two-lf.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 90,554 | `3004cda57af6db47a072616cdcf659e91a2faedf9ad77487448d5071755adc24` | saved by 16.0 |
| `release/16.0/0013/blue.pages` | [0013: Text colour](../experiments/0013-text-colour.md) | 91,355 | `1c5e95b0b1378b143088d5d1ccd9718e963118a3639b410550b2cf5a9a8e1e09` | saved by 16.0 |
| `release/16.0/0013/mixed.pages` | [0013: Text colour](../experiments/0013-text-colour.md) | 91,282 | `aa54b1e5b9efc82e5656fecd20e70e0ffabe15c163fb198cef55e3b6c4c1e619` | saved by 16.0 |
| `release/16.0/0013/red.pages` | [0013: Text colour](../experiments/0013-text-colour.md) | 91,338 | `673403655f766192e6cc6a7bcf09824cf3cc808db9196c6af79ea3f5a378f28c` | saved by 16.0 |
| `release/16.0/0020/plain.pages` | [0020: A table](../experiments/0020-a-table.md) | 90,284 | `1d6e6e5e8196fe9ec5dd1ee3e5cf0036fc8642c6c47bc403512517b6f2220396` | saved by 16.0 |
| `release/16.0/0023/image.pages` | [0023: An image](../experiments/0023-an-image.md) | 91,226 | `27d109c5811d93f08bfe24da9f6ebda9e1a260fc8897e88ad988f1bfe4d4cfdc` | saved by 16.0 |
| `release/16.0/0023/plain.pages` | [0023: An image](../experiments/0023-an-image.md) | 90,283 | `6c1421aeb0ed1997a3fc010f5d4ebe0d08a2e2e2cdb7694dd89b73e6b6585b0c` | saved by 16.0 |
| `release/16.0/0024/empty-a.key` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 2,475,371 | `582aead7819bbc76b0c677b4ef4e36e649179f13220822e84aea1d36cf1a75a7` | saved by 16.0 |
| `release/16.0/0024/empty-a.numbers` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 136,769 | `0f1c2a9a47f784d6c63bde835346500b91252f21537bde9e629e390bd4241317` | saved by 16.0 |
| `release/16.0/0024/empty-b.key` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 2,475,367 | `05e1c7448b32f1309b033e6075759b8264f889bfd5004f5e8bfa427982a1fae0` | saved by 16.0 |
| `release/16.0/0024/empty-b.numbers` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 136,769 | `f4ec51e7a0b7979a169218fba574e7c9cb8b36bc8600b1e7dbd05de5b1ebb516` | saved by 16.0 |
| `release/16.0/0025/hello.key` | [0025: Text on a Keynote slide](../experiments/0025-keynote-title.md) | 2,479,058 | `03fc791f2b375b61e00bf8bf6187e53a8cadadef6b22ec9209c5a67c54eed886` | saved by 16.0 |
| `release/16.0/0025/hullo.key` | [0025: Text on a Keynote slide](../experiments/0025-keynote-title.md) | 2,478,604 | `7ef9560866ec15a924446e83015dca80c3c0728ea015f96ccb5260dcc7a85d37` | saved by 16.0 |
| `release/16.0/0026/cells.numbers` | [0026: Cells in Numbers](../experiments/0026-numbers-cells.md) | 137,402 | `e4c3d255c5b0dfb01f83e315f2f14b58a4c445673dfe45e6b1966268a186919e` | saved by 16.0 |
| `release/16.0/0030/row-300.numbers` | [0030: A second tile](../experiments/0030-tiles.md) | 170,275 | `f8ad42a243241d9dcc8ee99a0fc3e0a71a1fef0a84185c4cd5e6b1349b796b00` | saved by 16.0 |
| `release/16.0/0031/kinds.numbers` | [0031: Kinds of cell](../experiments/0031-cell-kinds.md) | 140,173 | `36c00493f9897dc75ea090c7967738a7c4b60a2b42357341625686df2c6509f5` | saved by 16.0 |
| `release/16.0/0035/formulas.numbers` | [0035: Cell references in formulas](../experiments/0035-formula-references.md) | 138,311 | `aa44d63604798db63eed0defaa654dcb4d09859055a49c3b2eb9fc9c27ff56da` | saved by 16.0 |
| `release/16.0/0036/formats.numbers` | [0036: More cell formats](../experiments/0036-more-cell-formats.md) | 139,890 | `08dd256a5a409366e8c924e165ee51411686c5d3e753fc90d0a30d8fecccea89` | saved by 16.0 |
| `release/16.0/0037/two-sheets.numbers` | [0037: A second sheet](../experiments/0037-second-sheet.md) | 145,328 | `41d3d1bc14e40e9846a21bc6aacf557fc565108ed4b292d990b59b7aca15d3c4` | saved by 16.0 |
| `release/16.0/0038/two-slides.key` | [0038: A second slide](../experiments/0038-second-slide.md) | 2,480,504 | `e5c0d2ea6df263073c2d6d4a9ddea42f5ff38e00eae7d5b9969fd700d4bf51f7` | saved by 16.0 |
| `release/16.0/0039/notes.key` | [0039: Presenter notes](../experiments/0039-presenter-notes.md) | 2,475,373 | `8e0aa3cf729a2faa85714c93bb7f677aedc2ff91622cbafb78b0ba32150dd719` | saved by 16.0 |
| `release/16.0/0043/styles.numbers` | [0043: Cell styles](../experiments/0043-cell-styles.md) | 139,742 | `b65f0fb44c26caec05e4b602424bb4a0c95f5d7d9e55c354960a67fcfe8e65c9` | saved by 16.0 |
| `release/16.0/0044/merged.numbers` | [0044: Merged cells](../experiments/0044-merged-cells.md) | 137,310 | `bf39b54aa77458be8d3aa0e1fe1a3f1e069608ff7df722aa00abae7380ff5b23` | saved by 16.0 |
| `release/16.0/0045/sizes.numbers` | [0045: Row and column sizes](../experiments/0045-row-and-column-sizes.md) | 134,928 | `02f2a617e626b2c05a29c5c2f939b2539f8cb881cf2aea746263fce4dba9d332` | saved by 16.0 |
| `release/16.0/0046/blank-layout.key` | [0046: A slide's layout](../experiments/0046-slide-layout.md) | 2,475,047 | `77d33882f3d11a01005f16356bc803c3b32f1fd9511d04f5ce73403205ff0ee6` | saved by 16.0 |
| `release/16.0/0047/two-tables.numbers` | [0047: A second table on a sheet](../experiments/0047-second-table.md) | 144,888 | `b3e37dedead7af11c8db2329ae0d31506f8272dc6e7d7624fbdd11bfdec1ed86` | saved by 16.0 |
| `release/16.0/0049/text-box.pages` | [0049: A text box](../experiments/0049-text-box.md) | 91,257 | `739c7053c7031e82f886cdcf29766fbf4f7ba5994f135e5253ab01289ce833f5` | saved by 16.0 |
| `release/16.0/0050/shape.pages` | [0050: A shape](../experiments/0050-shape.md) | 93,283 | `f83831aea6d9d538dcc50d9a6c9df3a2d50a69232932c0c1af6b083dc07c1e8d` | saved by 16.0 |
| `release/16.0/0051/line.pages` | [0051: A line](../experiments/0051-line.md) | 93,434 | `33e7053e2df0f9d91b55ba49cb23f6cb1a368e4369f5eff4907537b8c19a4fcd` | saved by 16.0 |
| `release/16.0/0052/table.pages` | [0052: A floating table](../experiments/0052-floating-table.md) | 104,535 | `bceebc6c09b31428475f8feaf53ae6b5b84dc34f0fadbc337475b22d7c615dd3` | saved by 16.0 |
| `release/16.0/0053/font.pages` | [0053: A different font](../experiments/0053-font.md) | 91,219 | `dda9b90f70baa06054c3aa28f672feefb3f199077ebb7dbdc264867c018325e7` | saved by 16.0 |
| `release/16.0/0054/sizes.pages` | [0054: Shared sizes](../experiments/0054-shared-sizes.md) | 91,861 | `4c8a5614bb8c40b3212a7b730ea9941599dfca6fe28b96ef9209814b6e2f8f46` | saved by 16.0 |
| `release/16.0/0055/size.pages` | [0055: Resizing an image](../experiments/0055-image-size.md) | 92,714 | `af923e1ad16453badfe2844ad7e86fe4339495a3f2bb076400fc0b8355070665` | saved by 16.0 |
| `release/16.0/0056/rotation.pages` | [0056: Rotating an image](../experiments/0056-image-rotation.md) | 91,275 | `916180ecd219a87729861a7b37431408e74ca4f89965e20472b5f2057a581fae` | saved by 16.0 |
| `release/16.0/0057/opacity.pages` | [0057: An image's opacity](../experiments/0057-image-opacity.md) | 91,179 | `48186e0830a7618136bed3bb0e5a3452a39515c34505cc557e8516bd957bdba8` | saved by 16.0 |
| `release/16.0/0058/tab.pages` | [0058: A tab and a non-breaking space](../experiments/0058-tab-and-nbsp.md) | 90,433 | `2c0793c14394060f7dbb1db84dd384617a2168d62fc1246d8e7e917dc000ebd7` | saved by 16.0 |
| `release/16.0/0059/geometry.numbers` | [0059: A table's position and size](../experiments/0059-table-geometry.md) | 124,120 | `c0583cb6624c0478c954a96fbdcdcac209c4b169e6f750d47114df933900b487` | saved by 16.0 |
| `release/16.0/0060/headers.numbers` | [0060: Header and footer rows](../experiments/0060-header-rows.md) | 136,430 | `e39d11d11603ab9a0c98308da9743c1087f269cd080847cc9495999557cccd02` | saved by 16.0 |
| `release/16.0/0061/center.numbers` | [0061: Centring a cell](../experiments/0061-cell-alignment.md) | 137,293 | `09590d97486f2b77e49648a8fb586c1677d3a0d5a61876216978598151ea150c` | saved by 16.0 |
| `release/16.0/0062/top-nowrap.numbers` | [0062: Text wrap in a cell](../experiments/0062-text-wrap.md) | 137,224 | `47916cbf6aeaf9e1d1418bc39fba901612247b7f6e3f36e616a94ffc5782b580` | saved by 16.0 |
| `release/16.0/0063/sparse.numbers` | [0063: Tiles for a sparse table](../experiments/0063-sparse-tiles.md) | 203,692 | `35666a901e139f30be651536468921d50fc518c895d89017a10b9cfa6f068ec8` | saved by 16.0 |
| `release/16.0/0064/functions.numbers` | [0064: Operators and functions](../experiments/0064-operators-and-functions.md) | 140,520 | `eaf5a547de2310ace080796b4451e8bcd2f257c412cdffd8e532d7a4d01139af` | saved by 16.0 |
| `release/16.0/0065/cross.numbers` | [0065: A reference to another table](../experiments/0065-cross-table-reference.md) | 145,544 | `ccefa34f8fac8f652f6536a2737d89dbb52e43e1f4e0a2967a8eb286a6dfc47f` | saved by 16.0 |
| `release/16.0/0066/if.numbers` | [0066: Comparisons and IF](../experiments/0066-comparisons-and-if.md) | 139,790 | `975b24848bf0ca05c38950608dfbe99402a2bd6430b685260cf6d25c5bedf992` | saved by 16.0 |
| `release/16.0/0067/chart.key` | [0067: A chart](../experiments/0067-chart.md) | 2,507,195 | `d9a0d828d0d5b77cb0bdf6e86e878d66a87f490a21f821f5704436d2948d4a4c` | saved by 16.0 |
| `release/16.0/0068/textbox.key` | [0068: A text box in Keynote](../experiments/0068-keynote-text-box.md) | 2,476,665 | `5c858bf95d33d0f8a36d3b4289d80886cacbcc2be34503e7cdc0df161620f68c` | saved by 16.0 |
| `release/16.0/0069/image.key` | [0069: An image in Keynote](../experiments/0069-keynote-image.md) | 2,476,164 | `1e9ffe800d760905301d7e2ad1a04eb0371614e733db50e21dbfa2828d7cd92d` | saved by 16.0 |
| `release/16.0/0070/skipped.key` | [0070: A skipped slide](../experiments/0070-skipped-slide.md) | 2,475,353 | `71f1602559cd3f095da87f655429b51c89f7cd84c11e5a463a652efe1eaccf93` | saved by 16.0 |
| `release/16.0/0071/transition.key` | [0071: A transition](../experiments/0071-transition.md) | 2,475,354 | `d1a6c28944573e0ce603aa983597955e99096014804f993a0b94ce540a7a84ee` | saved by 16.0 |
| `release/16.0/0072/bullets.key` | [0072: Bulleted text in Keynote](../experiments/0072-keynote-bullets.md) | 2,479,047 | `e074bb4cfc35a07746e47e6e55187abc8a1881eb3f47f78eedf1b088069d7d38` | saved by 16.0 |
| `release/16.0/0073/table.key` | [0073: A table in Keynote](../experiments/0073-keynote-table.md) | 2,498,981 | `5f46b86687b2aa29823a99d0a2a39510747d5d260641ec427ce918f1da749306` | saved by 16.0 |
| `release/16.0/0074/slidenumbers.key` | [0074: Slide numbers](../experiments/0074-slide-numbers.md) | 2,475,658 | `d09aa6d5a086719013e3a8aa90cca5f96e872b3a4d62567e198e4ca1a2230b06` | saved by 16.0 |
| `release/16.0/0075/size.key` | [0075: Slide size](../experiments/0075-slide-size.md) | 2,476,626 | `7408323c81b5b7d771dd9e1ba2ddfcafe9f44c28e222c796280a5111914370f3` | saved by 16.0 |
| `release/16.0/0078/error.numbers` | [0078: A formula error](../experiments/0078-formula-error.md) | 136,985 | `83c5f2d6598942a74b3c49186ded32080c90a9da02a1a190539e6ddce72be7e5` | saved by 16.0 |
| `release/16.0/0079/pie_2d-row.key` | [0079: Pie chart](../experiments/0079-pie-chart.md) | 2,487,527 | `486496c2f86e636c11b61d52f97f5dddbc2d5bebc2ea26820baf0a8df74ec2cd` | saved by 16.0 |
| `release/16.0/0080/horizontal_bar_2d-row.key` | [0080: Horizontal bar chart](../experiments/0080-horizontal-bar-chart.md) | 2,501,705 | `8030bb8a062db46131b4f643615d7155f22c4221d2589b1a14fb62db069d8ab4` | saved by 16.0 |
| `release/16.0/0081/stacked_vertical_bar_2d-row.key` | [0081: Stacked vertical bar chart](../experiments/0081-stacked-vertical-bar-chart.md) | 2,496,650 | `8418f449720321ec18b5f42f9efab6eda8af331ed2e54e0d7826cdfa19a23034` | saved by 16.0 |
| `release/16.0/0082/line_2d-row.key` | [0082: Line chart](../experiments/0082-line-chart.md) | 2,499,170 | `3f5ec049e432dfb01596f14a69e1af53c5de89fe6aa231befbdea36e90d76788` | saved by 16.0 |
| `release/16.0/0083/area_2d-row.key` | [0083: Area chart](../experiments/0083-area-chart.md) | 2,494,706 | `5eeb263cc16dad4b9dd1c40e1c831ffd2508c9eaf2c0fbdf68322ebf91fc54ab` | saved by 16.0 |
| `release/16.0/0084/scatterplot_2d-row.key` | [0084: Scatter chart](../experiments/0084-scatter-chart.md) | 2,491,385 | `ac0afbedef84059994ba50cbd9282c6573f626815eb67bbb2e1d54dd0720c93a` | saved by 16.0 |
| `release/16.0/0085/vertical_bar_3d-row.key` | [0085: 3D vertical bar chart](../experiments/0085-3d-vertical-bar-chart.md) | 2,503,631 | `a010234d65f1b6dc02b46fd24ae84e56f8d4c1e1e4de0f27091f23d062708ee3` | saved by 16.0 |
| `release/16.0/0086/vertical_bar_2d-column.key` | [0086: Chart grouped by column](../experiments/0086-chart-grouped-by-column.md) | 2,496,181 | `2e91a068001347fd2a0d8e0e8808f6b14dddea8c3e79ef93062210b70ad5cd72` | saved by 16.0 |
| `release/16.0/0087/autoplay.key` | [0087: Auto play](../experiments/0087-auto-play.md) | 2,475,340 | `a57af24dba3edd368284eb72c31814008b2524579f73bb044fb34d419bd11507` | saved by 16.0 |
| `release/16.0/0088/autoloop.key` | [0088: Auto loop](../experiments/0088-auto-loop.md) | 2,475,338 | `c03c776b70f3e216e83d3b244af8f0ae43b60f212a14481cbe6484ba178f1386` | saved by 16.0 |
| `release/16.0/0089/autorestart.key` | [0089: Auto restart](../experiments/0089-auto-restart.md) | 2,475,362 | `51550d73da90b75524a82d9b8cf87969e32fca4975662b26f1ae170df2c159a7` | saved by 16.0 |
| `release/16.0/0091/movein.key` | [0091: The move in transition](../experiments/0091-move-in-transition.md) | 2,475,362 | `bd2e3361a5b67b76de80561aafd36a3828fb3eb8549d405a623ec01c9f8843c0` | saved by 16.0 |
| `release/16.0/0092/push.key` | [0092: The push transition](../experiments/0092-push-transition.md) | 2,475,354 | `204a5720bd25c77fbd7cee08c67836ee5e353f35f76f5e1aadb396a68ebee990` | saved by 16.0 |
| `release/16.0/0093/cube.key` | [0093: The cube transition](../experiments/0093-cube-transition.md) | 2,475,360 | `e3dad1cabf2c22b6254e5e9ca32518a08200dec4f545d3c2c41553f1c7f14e12` | saved by 16.0 |
| `release/16.0/0094/auto.key` | [0094: An automatic transition](../experiments/0094-automatic-transition.md) | 2,475,357 | `180b7159114dad67287825b8dcbc64e1893d71075aba44a20c25b485c43ddcbb` | saved by 16.0 |
| `release/16.0/0095/magicmove.key` | [0095: Magic Move](../experiments/0095-magic-move.md) | 2,475,394 | `0a244f7f12f526d6c9b2672fff34a6508e5be42cab281946743decdda1bfc74a` | saved by 16.0 |
| `release/16.0/0096/textstyle.key` | [0096: Formatting a whole text box](../experiments/0096-keynote-text-style.md) | 2,476,693 | `1e6b2a7f355475a6debf0ea16e23544baa22351fbd3df1b351d79d15d8e6f27e` | saved by 16.0 |
| `release/16.0/0097/rotation.key` | [0097: Rotating a shape in Keynote](../experiments/0097-keynote-shape-rotation.md) | 2,477,580 | `96235503918755734d35fb93df7e69bf97703ed3a17bd5a295b9572d7f4bc1a2` | saved by 16.0 |
| `release/16.0/0098/opacity.key` | [0098: A shape's opacity](../experiments/0098-keynote-shape-opacity.md) | 2,476,453 | `91f06e51b4817d40a4a88da7737cedd23448ed0fd968e2a1eb6e2bf8c980299f` | saved by 16.0 |
| `release/16.0/0099/reflection.key` | [0099: An image reflection](../experiments/0099-image-reflection.md) | 2,476,261 | `7e3e8a2972457b55857e120f1797260b94bc8e15170b8162e3bded68a2b398ee` | saved by 16.0 |
| `release/16.0/0100/locked.key` | [0100: A locked object](../experiments/0100-locked-object.md) | 2,476,165 | `7c77a99fe1e26a40c3dc0fc6da9680d84a33463e1dd7595eeddff8d6ba591ce9` | saved by 16.0 |
| `release/16.0/0101/notitle.key` | [0101: A hidden title](../experiments/0101-hidden-title.md) | 2,475,376 | `ab0b8500b297a67349dfcd7032e552703df447d0f9e3fd6a975db22532b5e67b` | saved by 16.0 |
| `release/16.0/0102/description.key` | [0102: An image's description](../experiments/0102-image-description.md) | 2,476,178 | `981db760aa6bbfe689676d6a3375a69a8a7b9e2e76b33b6682a7bd687ab13dbd` | saved by 16.0 |
| `release/16.0/0103/round.numbers` | [0103: ROUND](../experiments/0103-round.md) | 137,615 | `772df1a5bab037ad5ac5d35c44bca4b15f0fb684ec31dd5f9b63f50286f8cfa7` | saved by 16.0 |
| `release/16.0/0104/nested.numbers` | [0104: Nested functions](../experiments/0104-nested-functions.md) | 137,599 | `fc4b1e26b2b2ee44aaca61b25284d6733b348a177ceeec5ba66c043dec8c7983` | saved by 16.0 |
| `release/16.0/0105/whole-column.numbers` | [0105: A whole-column reference](../experiments/0105-whole-column.md) | 138,109 | `0825c1c0c336b1c494d847d94b1ed8a13e21417e19ebf1bfe2f023fd843c8bd5` | saved by 16.0 |
| `release/16.0/0106/mixed.numbers` | [0106: Mixed references](../experiments/0106-mixed-references.md) | 137,992 | `8a0a50832c8b5f66982a66990748c702dce5b075f4ff60981fbeb313a0244f30` | saved by 16.0 |
| `release/16.0/0107/other-sheet.numbers` | [0107: A reference to another sheet](../experiments/0107-other-sheet.md) | 146,813 | `84ca84795363f528b74e8f36be7e213ce7637515fa7a25d65da8a4db9c56545b` | saved by 16.0 |
| `release/16.0/0108/today.numbers` | [0108: TODAY](../experiments/0108-today.md) | 138,064 | `c3d6293a6c20e2764bf31db2d7bf6a40d4162638d6a6873679c6533c0b4af7c9` | saved by 16.0 |
| `release/16.0/0109/len.numbers` | [0109: A text literal](../experiments/0109-string-literal.md) | 138,082 | `27833c4591138ed4c821a8e8624426645ef0555afc582c67ba7d1553099414a4` | saved by 16.0 |
| `release/16.0/0110/join.numbers` | [0110: A text result](../experiments/0110-text-result.md) | 137,565 | `4e953d0159d6bca1e3bc2884c97b8e1be110d5eb69d407fa32636d11c8ba5a10` | saved by 16.0 |
| `release/16.0/0111/percent.numbers` | [0111: A percentage literal](../experiments/0111-percent-literal.md) | 137,462 | `65b9ede6de3f0827f71f5981468c0c2e4cde46aa63e3147522b7ca6442fd7ed9` | saved by 16.0 |
| `release/16.0/0112/minus.numbers` | [0112: Unary minus](../experiments/0112-unary-minus.md) | 137,639 | `21d0cb8b1bbb19b6fa8726b0679d369713f54969f7690ffd16090f4e2079bbe8` | saved by 16.0 |
| `release/16.0/0113/samestring.numbers` | [0113: The same text twice](../experiments/0113-shared-string.md) | 137,461 | `832d9cf9b643b40aab70e5137f1a239557cff7ef6e2374e5a51b6d6fc19b0581` | saved by 16.0 |
| `release/16.0/0114/cleared.numbers` | [0114: A cleared cell](../experiments/0114-cleared-cell.md) | 136,710 | `b84e42a4f63b4e9f0280d61d1a53eff12962c6ab12642698649a61e705586572` | saved by 16.0 |
| `release/16.0/0115/newline.numbers` | [0115: A line break in a cell](../experiments/0115-line-break-in-cell.md) | 137,046 | `b8abc2211f6c8854f5dcbee9a492ed6aec3c14afb11e4a6934ea27eb36a8444b` | saved by 16.0 |
| `release/16.0/0116/extremes.numbers` | [0116: Very large and very small numbers](../experiments/0116-extreme-numbers.md) | 138,743 | `7275789d625d584ac2244307ec09b0601bfed4e2e93c740a0d03f6c1e453f077` | saved by 16.0 |
| `release/16.0/0117/dateonly.numbers` | [0117: A date without a time](../experiments/0117-date-only.md) | 137,980 | `6a6e395917cda06091baeaca6bcfcc0377c0f9c120206d50d2e50987b19e6024` | saved by 16.0 |
| `release/16.0/0118/emoji.numbers` | [0118: An emoji in a cell](../experiments/0118-emoji-in-cell.md) | 136,695 | `f61905337aa2a3b0db3af5a3865ba7d96562ae801f9b4e67b66a1a31c406b5e3` | saved by 16.0 |
| `release/16.0/0119/sort.numbers` | [0119: Sorting rows](../experiments/0119-sorted-rows.md) | 137,830 | `cf54d9aecfb3bf4d384388249d94cf126ca7a31b0781b7b4345acf34695e0f48` | saved by 16.0 |
| `release/16.0/0120/fewerrows.numbers` | [0120: Fewer rows](../experiments/0120-fewer-rows.md) | 102,893 | `0a6b74a4b2eec1056f2543a0b2969231cfbd7c62a71524e3b5614672b88cba83` | saved by 16.0 |
| `release/16.0/0121/emptyref.numbers` | [0121: A reference to an empty cell](../experiments/0121-reference-to-empty.md) | 137,028 | `f2264572d48443fc0b0fcffd2c9fe9b7bdc63b49482e7c432175044be75e432b` | saved by 16.0 |
| `release/16.0/0122/tablename.numbers` | [0122: Renaming a table](../experiments/0122-table-name.md) | 136,578 | `7887ff2acf48c7cb7036eaa188c037ff45d4e31971db30b0bcec964971fbb6e4` | saved by 16.0 |
| `release/16.0/0123/fewercols.numbers` | [0123: Fewer columns](../experiments/0123-fewer-columns.md) | 121,571 | `cdd11d52dd0cb7730d31273d54dee01be00dd66e7c62f6da910c35b404ef8c32` | saved by 16.0 |
| `release/16.0/0124/sheetname.numbers` | [0124: Renaming a sheet](../experiments/0124-sheet-name.md) | 136,347 | `c0068f151e840bc357e4a7f91c3f90c44a822838edeb333f785f860cdaf16aa6` | saved by 16.0 |
| `release/16.0/0125/unfrozen.numbers` | [0125: Header rows not frozen](../experiments/0125-unfrozen-headers.md) | 136,463 | `62417cd43ebc8255f40e65b9572237b8e88c94f6769591597391c334200fa4b5` | saved by 16.0 |
| `release/16.0/0126/origin.numbers` | [0126: A table at the origin](../experiments/0126-table-at-origin.md) | 136,493 | `afb30a7e698e9b3cfb971da07aaa00bc17cf7d5ef8976d352b29a9f022852e76` | saved by 16.0 |
| `release/16.0/0127/textbox.numbers` | [0127: A text box on a sheet](../experiments/0127-text-box-on-sheet.md) | 137,144 | `ddbed7dc285e30c878e70672abcc9090991735ede20c3ed13b3384ab6181b50d` | saved by 16.0 |
| `release/16.0/0128/image.numbers` | [0128: An image on a sheet](../experiments/0128-image-on-sheet.md) | 137,188 | `805af6ed38c4a51b811e096bf800f65576b6f45206b540d266f4de215bde0912` | saved by 16.0 |
| `release/16.0/0129/shape.numbers` | [0129: A shape on a sheet](../experiments/0129-shape-on-sheet.md) | 136,669 | `56a03f5c14f0c9aa108856d06f9068783c31c6ccaa97cbff2622d9d3229f616a` | saved by 16.0 |
| `release/16.0/0130/longtext.numbers` | [0130: A long text in a cell](../experiments/0130-long-text.md) | 141,095 | `be72d39a30214ed34df2e58db713591e32b9faf56b31bdce973030ce1de51c42` | saved by 16.0 |
| `release/16.0/0131/cells.pages` | [0131: Cells in a Pages table through AppleScript](../experiments/0131-pages-table-cells.md) | 108,797 | `79b48fbcd65df118b850611f9807cee0ea639cb201b63b674f3d19bfc80c9b12` | saved by 16.0 |
| `release/16.0/0132/formula.pages` | [0132: A formula in a Pages table](../experiments/0132-pages-table-formula.md) | 108,760 | `0cfe23426f601093807afa565ea7b346cb950d681943542d346bb8e1a71dedb5` | saved by 16.0 |
| `release/16.0/0133/merge.pages` | [0133: Merged cells in a Pages table](../experiments/0133-pages-merge.md) | 108,495 | `e708150d4ab042a0009dbfd9b06cf3bbc530def6e8c456c48106f8d9ab6e22ee` | saved by 16.0 |
| `release/16.0/0134/cells.key` | [0134: Cells in a Keynote table](../experiments/0134-keynote-table-cells.md) | 2,520,515 | `efaf0aca4ff817964b85211fa8a295a748f1f84a420853183eabf0eb622b0d73` | saved by 16.0 |
| `release/16.0/0135/formula.key` | [0135: A formula in a Keynote table](../experiments/0135-keynote-table-formula.md) | 2,520,657 | `4ba4bead4147dd2e8203de359aa80423860db491da2e6801ef9d3511083e7987` | saved by 16.0 |
| `release/16.0/0136/headers.pages` | [0136: Header rows in a Pages table](../experiments/0136-pages-header-rows.md) | 107,377 | `0b6b980c83e09d90f04d4ab12f9165edc7060fb80b6cefa083747b74ebfa3347` | saved by 16.0 |
| `release/16.0/0137/currency.key` | [0137: A currency cell in Keynote](../experiments/0137-keynote-currency.md) | 2,520,714 | `362851c92ce52b41bb5763006167a90278d0be02588e222db6dbde7da88bf179` | saved by 16.0 |
| `release/16.0/0138/fill.pages` | [0138: A styled empty cell](../experiments/0138-empty-styled-cell.md) | 108,698 | `429d875b96a96f2b6d7ca544365132cf587660dffc9e2a43ae2317069d88eb39` | saved by 16.0 |
| `release/16.0/0139/resaved.pages` | [0139: Saving an existing document again](../experiments/0139-resave.md) | 90,442 | `b15e1f46c348c397afb7e9d032ad91243200eee5dbfaa071fa114f6242246a64` | saved by 16.0 |
| `release/16.0/0140/edited.pages` | [0140: Editing and saving in place](../experiments/0140-edit-and-save.md) | 90,794 | `6d3514f664a4d833cf1a10672a65ff407adc4ff60291da4b87f095cf8ec3b746` | saved by 16.0 |
| `release/16.0/0141/big.pages` | [0141: A large body text](../experiments/0141-large-text.md) | 389,965 | `d59fba6ebb6ce584083ac58ef8af895756aa83e4b06d89000f573058265be2db` | saved by 16.0 |
| `release/16.0/0142/twice.pages` | [0142: The same image twice](../experiments/0142-same-image-twice.md) | 91,603 | `9aae147c577ba95d0b2c5c5e12127e88bc7ebecc29db87fb94e108546a0f93f9` | saved by 16.0 |
| `release/16.0/0143/jpeg.pages` | [0143: A JPEG image](../experiments/0143-jpeg-image.md) | 91,936 | `6207a9921639110823a6ec6b7326c88e16e5de9ae64c994ceca48b47aba01e97` | saved by 16.0 |
| `release/16.0/0144/odd-name.pages` | [0144: A file name with spaces and ø](../experiments/0144-non-ascii-file-name.md) | 91,238 | `9f1bde3158791b89213b74acf6cd873c63c07f2ad3e67f31a761ab7ff97d6784` | saved by 16.0 |
| `release/16.0/0145/deleted.pages` | [0145: A deleted image](../experiments/0145-deleted-image.md) | 90,307 | `40fc6df2515f2f3136f4504eeddce48162407aa815489d40853ae94c74b1a5e3` | saved by 16.0 |
| `release/16.0/0148/large.pages` | [0148: A large image](../experiments/0148-large-image.md) | 1,822,314 | `9674eb21bd0850dd2f6029e7d1b33103b1f2bf7cfb5adb580babf55b9cc7a10d` | saved by 16.0 |
| `release/16.0/0149/zwj.pages` | [0149: A family emoji](../experiments/0149-family-emoji.md) | 91,359 | `29ab622ae732a87081a884ef3c24b9e5acc5c911861a973cb71107620f465fab` | saved by 16.0 |
| `release/16.0/0150/rtl.pages` | [0150: Arabic text](../experiments/0150-arabic-text.md) | 90,707 | `51bb641c72c9b780aa1ddbde750aa7e1503ebd2c90b9a0766bc2f50ed124a161` | saved by 16.0 |
| `release/16.0/0151/paras.pages` | [0151: A thousand paragraphs](../experiments/0151-thousand-paragraphs.md) | 122,040 | `eaae9e554e59171406412bac9942a621a38ad9911ac5f032439b6dce70c923ea` | saved by 16.0 |
| `release/16.0/0152/sizecolour.pages` | [0152: Size and colour on one word](../experiments/0152-size-and-colour.md) | 91,760 | `608e559597ab5ff12bafad2b286b6b3c83783b1ee2549d0c81e67e34176b68f7` | saved by 16.0 |
| `release/16.0/0153/defaultsize.pages` | [0153: Setting a size a word already has](../experiments/0153-same-size-again.md) | 91,145 | `67803c03b0dc351bef0f4c95a0a1c015a17650cbc58510ddfc19c5bfe1031fc0` | saved by 16.0 |
| `release/16.0/0154/replace.pages` | [0154: Replacing formatted text](../experiments/0154-replaced-text.md) | 90,731 | `6f9903fce0ac8dad79a45e40b45f6b120e016f996df978f1b4150051e30e9083` | saved by 16.0 |
| `release/16.0/0155/landscape.pages` | [0155: The landscape template](../experiments/0155-landscape-template.md) | 84,723 | `adaacb68a3e6f474c9c9eae30c8700d52aa455b7c4e322346c7265ae27e05e2e` | saved by 16.0 |
| `release/16.0/0156/layout.pages` | [0156: The page layout template](../experiments/0156-page-layout-template.md) | 89,765 | `dd788bf1dbf7fcc067a7546ec39e4cca895753ca7672473c21656eb5ed4b10bc` | saved by 16.0 |
| `release/16.0/0157/black.pages` | [0157: The black template](../experiments/0157-black-template.md) | 82,588 | `dcc8b1f70e769a5dbab602b4065533cef4b5e7abbb147d02683cd7681c28b623` | saved by 16.0 |
| `release/16.0/0159/dup.key` | [0159: A duplicated slide](../experiments/0159-duplicated-slide.md) | 2,478,287 | `46fa0facae3ddb905959606ffb2013e3ba472fa8ca7712dd142b0c8846662d99` | saved by 16.0 |
| `release/16.0/0160/move.key` | [0160: A moved slide](../experiments/0160-moved-slide.md) | 2,480,245 | `3ac04146318852c8d641fc05c192fc25ebc3e0d88cca0f04a5ed96b55eab39de` | saved by 16.0 |
| `release/16.0/0161/delete.key` | [0161: A deleted slide](../experiments/0161-deleted-slide.md) | 2,478,551 | `85b63ed38520de1ee7b2bfb53f7f832d4b24120567d5328ec8b44511dd572050` | saved by 16.0 |
| `release/16.0/0162/ten.key` | [0162: Ten slides](../experiments/0162-ten-slides.md) | 2,492,156 | `d0867e6cd21014a4dfdfb9bb1072b6e4138b7fbb569d5d5376694234f31dd659` | saved by 16.0 |
| `release/16.0/0163/notes.key` | [0163: Presenter notes with several paragraphs](../experiments/0163-multi-paragraph-notes.md) | 2,475,381 | `e448313cfaf6a6f97844a8fa9217e0128925e2c7987a3d917e5bbc544e5f5dae` | saved by 16.0 |
| `release/16.0/0164/titlebreak.key` | [0164: A title on two lines](../experiments/0164-two-line-title.md) | 2,481,235 | `61649bcfeb36bcd56c7e49a6156db48c8381625af96f7d8f3a8d6db23704f1c0` | saved by 16.0 |
| `release/16.0/0165/layouts.key` | [0165: The first six slide layouts](../experiments/0165-slide-layouts.md) | 2,485,118 | `13da345d71a3268ea294177a68dbc4e071d46f28d2e52a7df7f94b82a1624eca` | saved by 16.0 |
| `release/16.0/0166/line.key` | [0166: A line on a slide](../experiments/0166-keynote-line.md) | 2,476,533 | `052db1f8782d68ad4fd3e002b3d9b4c2cff050d8ca902395702fbb1e6df6843b` | saved by 16.0 |
| `release/16.0/0167/shapetext.key` | [0167: A shape with text on a slide](../experiments/0167-keynote-shape-text.md) | 2,477,276 | `f0a79d9510995b91ffb4f4a3420c53a6b86b05fbfb91be9443ca9e782b31df22` | saved by 16.0 |
| `release/16.0/0168/untouched.key` | [0168: A title never set](../experiments/0168-untouched-title.md) | 2,475,363 | `b1a9cb9c1f76baf9f375785af57dc20db8e0b172312cef359bcaa322d48e8759` | saved by 16.0 |
| `release/16.0/0169/checkfalse.numbers` | [0169: An unchecked checkbox](../experiments/0169-unchecked-checkbox.md) | 137,098 | `f9850eb631806af96becf0da27c5cdbd035b9926677765193a144d5496601f2e` | saved by 16.0 |
| `release/16.0/0170/rating0.numbers` | [0170: A rating of zero](../experiments/0170-zero-rating.md) | 137,875 | `390e725bd19a318a342e2244ced5273df773489a1411fa77f23cad34f7335d59` | saved by 16.0 |
| `release/16.0/0171/slider.numbers` | [0171: A slider](../experiments/0171-slider.md) | 137,194 | `dea9614a5306be9c4397e7ab4d48f0f99cb2416e4629b5e9ee718be48009f280` | saved by 16.0 |
| `release/16.0/0172/stepper.numbers` | [0172: A stepper](../experiments/0172-stepper.md) | 137,086 | `021fd58489bcaf00e5d3ef3df8cb12dcaee61b38c13d3cdd3c2348909b83f6ef` | saved by 16.0 |
| `release/16.0/0173/popup.numbers` | [0173: A pop-up menu](../experiments/0173-pop-up-menu.md) | 136,976 | `999ee8bf1e99129b154d703e29b17b4b0e561aa0dad1b6576433cff445d66d08` | saved by 16.0 |
| `release/16.0/0174/negative.numbers` | [0174: A negative number](../experiments/0174-negative-number.md) | 137,063 | `2272a44d1873f908553660aa72ab092071db92023b61c8627929f486522abc54` | saved by 16.0 |
| `release/16.0/0175/boolformula.numbers` | [0175: A formula with a boolean result](../experiments/0175-boolean-formula.md) | 137,432 | `da37bba0ca730a0ba87b68d605eb8a7b9a2c292f576c95dc37aa3c2dc92d1af9` | saved by 16.0 |
| `release/16.0/0176/numtext.numbers` | [0176: A number typed as text](../experiments/0176-number-as-text.md) | 137,147 | `59da3bb1f9577e8d4fcdc86506ba13cea7ee83165c79a9ecc97efcf6798c4c9f` | saved by 16.0 |
| `release/16.0/0177/described.pages` | [0177: An image description in Pages](../experiments/0177-pages-image-description.md) | 91,236 | `7985e49bc0c2a063c1216dec06ac59fcda190638c03f6e835867cd42997d445f` | saved by 16.0 |
| `release/16.0/0179/locked.pages` | [0179: A password](../experiments/0179-password.md) | 74,635 | `52805e944773253e2a1615d87ca282496006b07d0e7dcc88fbe2692e07c58ead` | password `pw1234`; saved by 16.0 |
| `release/16.0/0179/locked2.pages` | [0179: A password](../experiments/0179-password.md) | 74,635 | `7c58f5e96f06679ed0d68fef953ba805b9ef54f6dcfe160f34dcadf729a904c5` | password `pw1234`; saved by 16.0 |
| `release/16.0/0179/plain.pages` | [0179: A password](../experiments/0179-password.md) | 90,283 | `ea4c25766d8313b398f6298e2e7bf5504e1586e8370525c3900d3b7d4a579208` | saved by 16.0 |
| `release/16.0/0179/unlocked.pages` | [0179: A password](../experiments/0179-password.md) | 90,285 | `94779aebe79d358855516239f03483507b767ee52abdc2fb93ee786104dd159e` | saved by 16.0 |
| `release/16.0/0180/accent.pages` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 74,635 | `53d2add2f71381e976398364090015f7c5fa63bfbaf0ce74be30de14d7a47dbf` | password `påss`; saved by 16.0 |
| `release/16.0/0180/image.pages` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 75,359 | `c8230fc364a90ec21e3d6cd460f5ee01e50b66f01bea46d1fcc156554cff8c04` | password `pw1234`; saved by 16.0 |
| `release/16.0/0180/locked.key` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 2,465,419 | `26e59c87909e42482062c4a2b4768b300b60059570c45b822355e1eb4e532f9f` | password `pw1234`; saved by 16.0 |
| `release/16.0/0180/locked.numbers` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 83,325 | `41bbefa7fd76491336274ef3c105128f2037bf89e07f5bfce769b765a0975988` | password `pw1234`; saved by 16.0 |
| `release/16.0/0181/numeral.numbers` | [0181: The numeral system format](../experiments/0181-numeral-system.md) | 137,063 | `8ecfefac26e488f2e7c545b5bd964d1c9dd68fc5a1cef234afe940b456c8e326` | saved by 16.0 |
| `release/16.0/0181/plain.numbers` | [0181: The numeral system format](../experiments/0181-numeral-system.md) | 136,769 | `ca1d92182d1198e548bf3a936ad3054d4e31a8324791454ec3db9f64739d9afb` | saved by 16.0 |
| `release/16.0/0182/transpose.numbers` | [0182: A transposed table](../experiments/0182-transposed-table.md) | 105,140 | `9cc014c040b7e39fd0cddb45f09a25e546bac3e7d1ddc5610e8ec08fa3b14dc8` | saved by 16.0 |
| `release/16.0/0183/frozencols.numbers` | [0183: Unfrozen header columns](../experiments/0183-unfrozen-header-columns.md) | 136,526 | `bcf3d80bff819c95fae892d6381b1146eb58396a936904223ebee92c1d233a84` | saved by 16.0 |
| `release/16.0/0184/footer.numbers` | [0184: A footer row](../experiments/0184-footer-row.md) | 137,288 | `cec10b7a59613a8d4d12c5d5f297c6ea0321405169d2e78c0c5d26a3596c8128` | saved by 16.0 |
| `release/16.0/0185/audio.key` | [0185: A sound in Keynote](../experiments/0185-keynote-audio.md) | 2,481,784 | `c2f96aead571fcc0a19ee7516ed03cc5beb2f5915f72abac97035f44c968e301` | saved by 16.0 |
| `release/16.0/0185/loop.key` | [0185: A sound in Keynote](../experiments/0185-keynote-audio.md) | 2,481,797 | `8408004a06499b5367d5bf6a3ee8c812986e624a6ca2509ef4abc5b2fefdfb2b` | saved by 16.0 |
| `release/16.0/0185/movie.key` | [0185: A sound in Keynote](../experiments/0185-keynote-audio.md) | 2,479,990 | `e567a37e9a0511f3b837bfe10b9aff4e56d7f79b630c7e0687b397d8c1c9a10a` | saved by 16.0 |
| `release/16.0/0188/movie.pages` | [0188: Media in Pages and Numbers](../experiments/0188-media-in-pages-and-numbers.md) | 95,681 | `53b9b23a4b71f872b649b4f89a540c04407bd32cb1cb0911dc93f12d69be362f` | saved by 16.0 |
| `release/16.0/0188/sound.numbers` | [0188: Media in Pages and Numbers](../experiments/0188-media-in-pages-and-numbers.md) | 142,634 | `05a2026c5811371ff0a3279a202996b207558c4b74a21893c3d729fa14988d09` | saved by 16.0 |
| `release/16.0/0195/area_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,502,092 | `37501014df9049ffacabef7c2d11f2cb810d75c250d8fab980fe15c1a3062634` | saved by 16.0 |
| `release/16.0/0195/horizontal_bar_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,524,474 | `cdd1d3e6a472e53111d270418e6f99768cc04779eea78839e77eef81712a6547` | saved by 16.0 |
| `release/16.0/0195/line_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,505,814 | `4ea1da681d9a7cbcf64999e02879a7e935563d721b8c035e89cf2301b9b47a77` | saved by 16.0 |
| `release/16.0/0195/pie_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,489,258 | `bd216ddb046183f4730a0f0ef34039d08017a2d70c829c8a4131c986b34b56da` | saved by 16.0 |
| `release/16.0/0195/stacked_area_2d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,495,211 | `d5f0480fc01e91349e7dbe62afe826caaa6c62b9b7388d747b2e8605e3e89d00` | saved by 16.0 |
| `release/16.0/0195/stacked_area_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,498,869 | `036482b9165f214c4b7fd48d4648e250659350a19cfe3de00a186e0cfb2efea4` | saved by 16.0 |
| `release/16.0/0195/stacked_horizontal_bar_2d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,508,413 | `a1d141fc89db8f75382ac0e934222c74efa77357d6d3b8aa08439bb55afae1ee` | saved by 16.0 |
| `release/16.0/0195/stacked_horizontal_bar_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,519,063 | `97a5d932d75196994df424dd58abed56720746fdf1c055d6c872e518eee20cf6` | saved by 16.0 |
| `release/16.0/0195/stacked_vertical_bar_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 2,502,786 | `622ffee7cbfc7ca63c7eab7c0b7ac64e2b492dbb2fb758e542f8660bcbf566c2` | saved by 16.0 |
| `release/16.0/0196/all.key` | [0196: Every transition effect](../experiments/0196-every-transition.md) | 2,549,843 | `68a4efbb7c3f0231fb93e93852570620ca7abad99200474c0906dc094e9ebca6` | saved by 16.0 |
| `release/16.0/0197/default.key` | [0197: The idle time without auto restart](../experiments/0197-idle-time.md) | 2,475,356 | `3311fe9f48bff9e4805f09162b0f4e3b13c72021a0e000fa658af847c386c4cd` | saved by 16.0 |
| `release/16.0/0197/idle.key` | [0197: The idle time without auto restart](../experiments/0197-idle-time.md) | 2,475,341 | `65b7f7bdc0a30d067b25e6cc46e2b80a2884ceeaa36b34b1c8979397ed022809` | saved by 16.0 |
| `release/16.0/0198/book.pages` | [0198: The blank book template](../experiments/0198-book-template.md) | 84,836 | `5fc19f01d2540ed4848448c994edee9054eee79e83f9b39da092437a71dc5879` | saved by 16.0 |
| `release/16.0/0223/ABS.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,435 | `afffb67ae51790859fbff50c53b07a4d8ee65a31237a63518a7829705973165b` | saved by 16.0 |
| `release/16.0/0223/AND.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,821 | `d83d6049173d06e345150b8d9cb3d7a96125a0056a4a65aa1c8c18a3f33937a1` | saved by 16.0 |
| `release/16.0/0223/AVERAGEIF.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,572 | `64fb79449d087c991af583afa9258cb7b08dce11a853219d2bf41e51e3d963b5` | saved by 16.0 |
| `release/16.0/0223/CHOOSE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,334 | `7313ef82b856f758313986236bcfae9cfa0dc5fea6998e5bbd9b6b7c99393ec5` | saved by 16.0 |
| `release/16.0/0223/CONCATENATE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,579 | `93021ca186fc70b2e9799f1d7fa1e71748d56ae5c7e954761c7e52874fe5e7fe` | saved by 16.0 |
| `release/16.0/0223/COUNTA.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,526 | `720eeecef2ca6fdcd5d7dc5b2562643dc33a7bbbfb0ffb5330abcac4760fc1a1` | saved by 16.0 |
| `release/16.0/0223/COUNTIF.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,498 | `04b136b6e6126766acb8d1766e411f560761686dccc227447b35ea85249ad867` | saved by 16.0 |
| `release/16.0/0223/DATE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,103 | `e09c74e36f560f0a54fa2e6b84f0c16df866ab13309a4c1f28db56d9e0db6fcd` | saved by 16.0 |
| `release/16.0/0223/DAY.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,574 | `3989c10bc1f74c8121d8604f762984aec1c0d4e4b0e60bad1c40a74b4e5e9a40` | saved by 16.0 |
| `release/16.0/0223/EXP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,552 | `9dad2dff38cb7bc1a3aa4aa1ff4d169681b3514aa66abac4e7c4fbd291e1122a` | saved by 16.0 |
| `release/16.0/0223/FALSE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,851 | `9e57891dac6ab2fd700dc123d77abd56177c732b8d5c3065de64d058f24f6e82` | saved by 16.0 |
| `release/16.0/0223/IFERROR.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,482 | `e5cb313cb4cf2d2f7ea16dfd720ee13e08cfc64acf96913b2bb0f5274eaad403` | saved by 16.0 |
| `release/16.0/0223/INDEX.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,555 | `d6fab8c0e6cb847639adc0de241bc0e34dbe166be45134b4aaf4ac65d70ec6bb` | saved by 16.0 |
| `release/16.0/0223/INT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,447 | `09cfcaa77189255b178a674a0bbd245f88d99a3c562d6dbf898f16d567ece112` | saved by 16.0 |
| `release/16.0/0223/LEFT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,480 | `031fe2da9e39bd260f4ae14d86ed670d5972c9be4048f199e73b96692bd9997c` | saved by 16.0 |
| `release/16.0/0223/LN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,476 | `a9dc2c6e33aef4b370681675aa132943b622407bb3f59870832658b6e8546edb` | saved by 16.0 |
| `release/16.0/0223/LOG10.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,628 | `eb3d8d33c98efc11b95ebfa30b4c8b720a9f466f3cf484bc76cfb912a63505d9` | saved by 16.0 |
| `release/16.0/0223/LOWER.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,680 | `1d2d9485a8f9846cc81e556c236895bd045d51c94c76eeb9d837685f4d674377` | saved by 16.0 |
| `release/16.0/0223/MATCH.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,559 | `941825a952488043a4107ebb2c6cbb01219920d046662fd12de49349f7142dc2` | saved by 16.0 |
| `release/16.0/0223/MEDIAN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,456 | `3c595ac93e92fd922234988da655f17d0eb96a9d8ee8196c3ed1e7f1c1d53893` | saved by 16.0 |
| `release/16.0/0223/MID.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,513 | `4e0e3df48dbf78d0fb1082ebbd8615ce871965e12f6e2b3587b23034a274f0bb` | saved by 16.0 |
| `release/16.0/0223/MOD.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,457 | `80f44fccaf2ab1fed1b45738dbc0aec56797a3aa13ad1081da25629bfc3cdb33` | saved by 16.0 |
| `release/16.0/0223/MONTH.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,477 | `0a40d2f9ee4f6ac91423d1b9cbf162979a986830d5e8d629e8a75248d76cd139` | saved by 16.0 |
| `release/16.0/0223/NOT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,897 | `2a5c75bf137471fd02a0b7c6c390a5dc66c1ee61cef8213876391d52b1d35083` | saved by 16.0 |
| `release/16.0/0223/NOW.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,457 | `8d0f957d047dd75479354568f93edc4bc1089aad96c9776578f65d8379dfd789` | saved by 16.0 |
| `release/16.0/0223/OR.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,807 | `129f2a8f29ceacd5fc15adc78c79b7e0fdea8fd0ce190ca6ef6f3f873b0d40dd` | saved by 16.0 |
| `release/16.0/0223/PI.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,532 | `c7b4dd489006fc655d7ddf65280ef27929db47f417709e8a84cae4af96e3a854` | saved by 16.0 |
| `release/16.0/0223/POWER.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,506 | `647527997654306922989681caababcd0009a95f547ea393e3bbb70bb2051842` | saved by 16.0 |
| `release/16.0/0223/PRODUCT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,481 | `3e2f308eb0a9d0a495378f0b0fa28e6f96ec0dda633ca3cb8d497e1a3fae3ebc` | saved by 16.0 |
| `release/16.0/0223/RAND.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,645 | `48f52ad212cf91c5912efc208c29939660b2b4500fcd898cb79dcbeafc73bfe9` | saved by 16.0 |
| `release/16.0/0223/RIGHT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,468 | `a538f0e0e6f7f2ef11329d382b83d9d726cf052e6c55c06bfba2781f09ae769f` | saved by 16.0 |
| `release/16.0/0223/ROUNDDOWN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,615 | `bc5fae60e8b9ff3f017654278ddebbd3d7f17bec20c3fc5fa1ec19c81024d159` | saved by 16.0 |
| `release/16.0/0223/ROUNDUP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,617 | `5fc949c259733b38300027821aab42f486bee1f4950e40bcff622406c15d182b` | saved by 16.0 |
| `release/16.0/0223/SIGN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,430 | `3409cb3e205211996ea79b758536b907357626e8351d15723e55580f801a836a` | saved by 16.0 |
| `release/16.0/0223/SQRT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,398 | `d844cbdadaa1d9d52e1a69af3732b3eb72afa6eba8e13fc2d3abf203d2d4a0ac` | saved by 16.0 |
| `release/16.0/0223/STDEV.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,436 | `0bfa4cb79aa2f4796e1f8f1263d720386f754b20e2d8de9130e119de903c3f09` | saved by 16.0 |
| `release/16.0/0223/SUMIF.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,585 | `ff3d143bc9284ea4ad38d102b1419c6a85f529fdf9e97a4b21ecb35921f92ba0` | saved by 16.0 |
| `release/16.0/0223/TEXTJOIN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,655 | `114a8a79feec1495722cc4e11f194f3a79f5a0d219860298e82c9f9a7e6abd27` | saved by 16.0 |
| `release/16.0/0223/TRIM.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,458 | `4eb63beebf984fabfc79bef22c66ca56dac579c2748b52510567a8f7b4d21c13` | saved by 16.0 |
| `release/16.0/0223/TRUE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,761 | `fc478aca47a0ed5a7dc71ed40b0b48577600c694122ff15596f4c13aad010783` | saved by 16.0 |
| `release/16.0/0223/UPPER.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,678 | `a043b3324bbd3178182e2d22b716371051489dec79a84579c0ee13f390a9919b` | saved by 16.0 |
| `release/16.0/0223/VLOOKUP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,925 | `21ac437f0361f068ab00da08ee664c2b4853f0bdf3babb7d5fa1e5542e0a19d0` | saved by 16.0 |
| `release/16.0/0223/XLOOKUP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,592 | `1f18b90b87a4e547bce06f10105608a3049246a1c1b6cc34b44d0888db6fab0d` | saved by 16.0 |
| `release/16.0/0223/YEAR.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,711 | `ed64f5f565a67fceae2d31bdc220eab97e3142de12aa1dc89427e0e5ffd28785` | saved by 16.0 |
| `release/16.0/0243/body.key` | [0243: A hidden body placeholder](../experiments/0243-hidden-body.md) | 2,477,260 | `f5d453b7f624b3a24b627ef00b6ee9f022a7a60fff534c9cb49324f2802c5976` | saved by 16.0 |
| `release/16.0/0243/no-body.key` | [0243: A hidden body placeholder](../experiments/0243-hidden-body.md) | 2,477,233 | `d490389a8845b32c829c9ebcbbd3967f0ea676ec3decd786a15e5b774bccee21` | saved by 16.0 |
| `release/16.0/0248/ACOS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,478 | `9d0587d7f831e7938b26b068ee37be05cecaed83dd33cd16a89274ef7132c445` | saved by 16.0 |
| `release/16.0/0248/ASIN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,445 | `404a4f677113552d7534e388a62e39e006f6a55e8063cde8063b8deea63af6b6` | saved by 16.0 |
| `release/16.0/0248/ATAN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,651 | `9cf33e2be7eae5feedfc7f8c0350654cec390d652f3740712e9f46a9538a8245` | saved by 16.0 |
| `release/16.0/0248/AVERAGEIFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,566 | `b46a4046b5576e07dbc1309ed1ea8f87104f59e136d0b3e774ad61e49ce77421` | saved by 16.0 |
| `release/16.0/0248/CEILING.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,473 | `97b414d60316b1e7826e60342151a23a8070bf998cf62a352de68ae8b6b100fa` | saved by 16.0 |
| `release/16.0/0248/CHAR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,529 | `3f0be481389a36c0f1b77a99ff0c34ea5417c0e59ded1b78f0562e6c5efa06e8` | saved by 16.0 |
| `release/16.0/0248/CODE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,564 | `1e78fefc58c3bfa0a56a4237a68f1c329abe530e668d768168ad7b54f5693c4e` | saved by 16.0 |
| `release/16.0/0248/COLUMN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,439 | `e41b8d08e00890d055c0c08a1d10ab068abb285505ce1f26427e82b5aee211a4` | saved by 16.0 |
| `release/16.0/0248/COLUMNS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,527 | `10ccec6fecfc8762a6eeb0f9d792279d70a36d8f20d51c4039f7ffb2fcaed8b5` | saved by 16.0 |
| `release/16.0/0248/COS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,437 | `bd6e07ec560004cd86166a83394462c47ba566999fc18447a237c0ad1206c799` | saved by 16.0 |
| `release/16.0/0248/COUNTBLANK.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,539 | `9ac68b21628bcd056dad13219b46bd0ea891fc1a3bd198dab27a187643f90e3f` | saved by 16.0 |
| `release/16.0/0248/COUNTIFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,534 | `0baf9fcc293cf3b6caf538850ae6a3f56c375be4536e491e61df448722a2e82f` | saved by 16.0 |
| `release/16.0/0248/DATEDIF.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 140,027 | `41182394790d566a930146ba031891e441f000a1a51beac45a73e5bdd43f7ac1` | saved by 16.0 |
| `release/16.0/0248/DAYS360.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,929 | `990784485b6f9c6a5771efc13d7b2a36b8a6efeb647accebd0cbc9247e9b942a` | saved by 16.0 |
| `release/16.0/0248/DEGREES.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,231 | `2eb6ef5ff44a126255665501f582e3d8989e6b8cf31d9981f9c4441dd3bfd6a8` | saved by 16.0 |
| `release/16.0/0248/EDATE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,103 | `0145920735f5965e8f636b282fcd40c8a8bc4f5b66851f193848757eb8901701` | saved by 16.0 |
| `release/16.0/0248/EOMONTH.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,490 | `d7c61cf6326d1482797c7092079c813b86b2df2c2ef81c8ad481fa4ffa5f5402` | saved by 16.0 |
| `release/16.0/0248/EVEN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,449 | `1e620bfa308f3c38ef512426cb8f6da2b7de37933aeca97ace03805aeffdf26d` | saved by 16.0 |
| `release/16.0/0248/EXACT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,760 | `ba1e449d574b9be7d17bcf54ca5fe2e873122b4ff284a2a95ed7656b3ff0c0c2` | saved by 16.0 |
| `release/16.0/0248/FACT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,580 | `412633096daa84490a1f95459040374f039bc1190ec5635be90a8208624852c0` | saved by 16.0 |
| `release/16.0/0248/FIND.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,432 | `62faf7ad4947c79f08604c721a1a8e42dfa823c210b02d9ba829884afdcaad75` | saved by 16.0 |
| `release/16.0/0248/FLOOR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,458 | `4c872a58518dced598c128a188cad9118b6ce30bed5803c202566e1de11b5c40` | saved by 16.0 |
| `release/16.0/0248/FV.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,106 | `90dc3b7123fe2ce7e54747e049eaf5b183ae917536fff4da4f761b3f93402b73` | saved by 16.0 |
| `release/16.0/0248/GCD.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,457 | `7f6c7b473645fbcafe3219e874b520a956c88727492c47f2689a033444bfa91b` | saved by 16.0 |
| `release/16.0/0248/HLOOKUP.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,901 | `5049678123bf20e5b8e20cfdaf3b95483062a91f68e4fd47db7214a5d421a60a` | saved by 16.0 |
| `release/16.0/0248/HOUR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,491 | `20bebb820cdb7ddd204d787fe17da954c85406aa39199cb8d8de306a37f107de` | saved by 16.0 |
| `release/16.0/0248/IFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,450 | `2dcd5a23c39aae46d38d5e64172fea5a42b948e9e9fe1cbdd4da9a6b82c1f4ac` | saved by 16.0 |
| `release/16.0/0248/ISBLANK.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,761 | `3ae2cf407e1215d0c9e590f9db128578f974d4b103d0bb5aa639b36514dc97da` | saved by 16.0 |
| `release/16.0/0248/ISERROR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,786 | `f58e34f38099dd2fbe6ac07c852664e1ad12bdb3d333d381287024ca2f661977` | saved by 16.0 |
| `release/16.0/0248/ISEVEN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,760 | `a78f9c83635fd865bd49c9fbfd008f3354ea85d1d460ff71e0668c7fb42f857a` | saved by 16.0 |
| `release/16.0/0248/ISNUMBER.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,406 | `cfe442b11b5a6d6084d77ac27af0f2d66597e1d712dad00cc0300a8cab33a745` | saved by 16.0 |
| `release/16.0/0248/ISODD.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,865 | `bf819c4a3e20790ab98bf0faa062469ef997610b222cf4f178fa7ec6be8c7ed1` | saved by 16.0 |
| `release/16.0/0248/ISTEXT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,887 | `1da095b21642db00a7270369e44d92e165b37a76e349692d3338fec7fcf6ac5f` | saved by 16.0 |
| `release/16.0/0248/LARGE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,553 | `17f889116e747adde178cad16bf37863c83990d378a8947ec25243781e05cd46` | saved by 16.0 |
| `release/16.0/0248/LCM.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,207 | `fa674dbf6779cb03a19e42aee4c4ba7c734e60f73f645eb058f5fb656ca9ed1f` | saved by 16.0 |
| `release/16.0/0248/LOOKUP.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,485 | `da319c79fd17c61052353a8dff69bdc640c7bb0ab67232d6adb20ffd31563b5f` | saved by 16.0 |
| `release/16.0/0248/MINUTE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,524 | `9b213b3f35e9048f49db68f5221a3d4eeefc40f6f8b3c20af16210ba62595c29` | saved by 16.0 |
| `release/16.0/0248/MODE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,547 | `31f849321e236642f86c49bab836ac99634c901e4613b7b1c4fda13beb83d41e` | saved by 16.0 |
| `release/16.0/0248/NETWORKDAYS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,777 | `6ea2b1a000ea878d28d5696b605a6b443e67c2841b40d678d56156cd42c57c79` | saved by 16.0 |
| `release/16.0/0248/NPV.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,879 | `d01f087bd9a3d088df09dedcebef13d2b71619823b30c89cc5a7117c20e5737e` | saved by 16.0 |
| `release/16.0/0248/ODD.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,452 | `d5234141a2d143f3873e6c8fe390131ed92036e31062e5d1e61abb1be521008b` | saved by 16.0 |
| `release/16.0/0248/PMT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,360 | `639029272a56d85013138c9d969182e13ea97b77ef9d8b608cff2aa52c3b5f70` | saved by 16.0 |
| `release/16.0/0248/PROPER.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,809 | `c274951bf982022e9ba64e71fa30dca23501cf4d55c828e8f8ef33d8543702f2` | saved by 16.0 |
| `release/16.0/0248/PV.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,979 | `b50e9835c224d5eb2816baa8e32ff4f6492985d24f17d7d0661463dd48369e57` | saved by 16.0 |
| `release/16.0/0248/QUOTIENT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,457 | `39b0ba95ddccc48ffaf4fce49a0c7282913f5763f1f7bcaee15750326ce22f82` | saved by 16.0 |
| `release/16.0/0248/RADIANS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,484 | `2910dd09597b2a5289b76741b92fa7e32526d15c6ae57a49dd8adb9f8a17cfb8` | saved by 16.0 |
| `release/16.0/0248/RANDBETWEEN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,412 | `dd01f689af01d6577cea9de3f05658e4390fba943dc3da8153098e6be1ba0dbe` | saved by 16.0 |
| `release/16.0/0248/RANK.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,546 | `317a140a3b5fd3dedf8869e96050cba899772c60b68bdd39d7863af24ff2b4d6` | saved by 16.0 |
| `release/16.0/0248/REPLACE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,523 | `4811153c6b90c04866ed6264d69bb3b0b488a7fa55625d90eb50af6cb8855263` | saved by 16.0 |
| `release/16.0/0248/REPT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,221 | `32051ee08cf9a985881b23289f7e0eb18f3846f90a81bbf11ea47227a37179cb` | saved by 16.0 |
| `release/16.0/0248/ROW.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,417 | `3433eea987865ac1fa9d3b21b15cc4d67898637da2402f88f4c6d3bfe9104386` | saved by 16.0 |
| `release/16.0/0248/ROWS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,528 | `4328fd5b9b6e7f64239ccfecaece23bab89c469dcb9813086bc12c602cc94b51` | saved by 16.0 |
| `release/16.0/0248/SEARCH.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,303 | `ff18f82c0f640a5af79cf7876ec6cf3916305a80ad36d06379f603366ff8ac21` | saved by 16.0 |
| `release/16.0/0248/SECOND.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,509 | `7b362693905097b485792571d9618197268c477a47fb4360bc2ffc3e77e258b8` | saved by 16.0 |
| `release/16.0/0248/SIN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,446 | `b2fcfe78b3406cc74137a24d0235bdd78881ec989f41d0c9f1baa24201816ea1` | saved by 16.0 |
| `release/16.0/0248/SMALL.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,563 | `e397fdd9b5e8123f9c01193859918b1fb2b97c8a3b2cad0a53d2e22f2d863901` | saved by 16.0 |
| `release/16.0/0248/SUBSTITUTE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,631 | `fb703e816df15e732c035eef252171f8f12b937d13b94122af6bad3d1c9fe33c` | saved by 16.0 |
| `release/16.0/0248/SUMIFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,684 | `830bc7fab15ffd0afafcc1f3742b1d5693cedacee2adda5f92d1e8b036e3667b` | saved by 16.0 |
| `release/16.0/0248/SUMPRODUCT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,677 | `106a6df60849b7e785bff512011e4b540ae7e8a0a0a009d73fddd2af09c220eb` | saved by 16.0 |
| `release/16.0/0248/SWITCH.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,434 | `8a366a895b1c5f8e93bdb3005869ef2334fd67a2c56226a368eb89da3849b666` | saved by 16.0 |
| `release/16.0/0248/TAN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,460 | `827eeb75216269ac917c5f66fdab7e3a1c505987e5c70f75143a888bbe45536b` | saved by 16.0 |
| `release/16.0/0248/TEXTBEFORE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,467 | `abf239ea4990c49e95d6f6a9c9b8aa09c2a2f098ed39f4830aeca2bd134a5c83` | saved by 16.0 |
| `release/16.0/0248/TIME.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,414 | `a264981ca6e24619597e33e6f3e72aa488247cf53a1c2044a4feb53e1aef38bd` | saved by 16.0 |
| `release/16.0/0248/TRUNC.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,462 | `7f2c744c91ea5bb171eb1a742e3bf317e55392dcba1161dd6a5f7a80ea5d6b1b` | saved by 16.0 |
| `release/16.0/0248/VALUE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,437 | `1bf3c3e3b6d5b9c5eb5d7117a358af6e0e53133df83076046e8c0f74c6343dba` | saved by 16.0 |
| `release/16.0/0248/VAR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,444 | `b37d3cadee503ce649ca21a89321b81cd5d0f277eda00c69939622bc130e9aac` | saved by 16.0 |
| `release/16.0/0248/WEEKDAY.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,378 | `6671a069378cfab356e4922d238efa9d571e44096be8e3408ff57593754c7c27` | saved by 16.0 |
| `release/16.0/0248/WEEKNUM.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,565 | `118b3217c5c1f1756bd28f62dd4b4b0fd77305ad35b860708941f29efe948635` | saved by 16.0 |
| `release/16.0/0248/WORKDAY.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,492 | `eabb812d3031131906d07798ae325a7c689532b8701559dcb41f8c92974a0758` | saved by 16.0 |
| `release/16.0/0248/XOR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,925 | `bfc5683176f1adecaf64c2adfb3a134b7d82aff285788c51757a49536e754280` | saved by 16.0 |
| `release/16.0/0265/MINUTT.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 137,546 | `03bfbdb2bb20b6988542f0f81413f0c8567d5a6b55354c64947151d9365f542f` | saved by 16.0 |
| `release/16.0/0265/SUMMER.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 137,466 | `f813079205f3a6da1cd0a7377cbe70b45b0e390d048a48923225f31c7f1a513a` | saved by 16.0 |
| `release/16.0/0265/TID.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 137,749 | `0d2c60fa3ca06554b3a5825fb0df3c7887c17a390767863c2f7401df548f0836` | saved by 16.0 |
| `release/16.0/0265/TIMEVALUE.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 138,293 | `5362f2a259e15b9150bc29dd366e98ef1b4a099597fd20ffc1b0606f2bec430e` | saved by 16.0 |
| `release/16.0/0295/baseline.key` | [0295: A chart's title, legend, border and caption](../experiments/0295-chart-options.md) | 2,497,470 | `dc3772386be096b75e0b092735bb4865a5c79a6b9a8924329ad334b578511225` | saved by 16.0 |
| `release/16.0/0296/baseline.key` | [0296: A chart's value axis](../experiments/0296-chart-axis.md) | 2,497,487 | `d2a8bdae29d109436c6c6a6adbd447577f0eaa542db8cd2579447faa6272a7cf` | saved by 16.0 |
| `release/16.0/0297/baseline.key` | [0297: A chart's category axis, series and text styles](../experiments/0297-chart-category-axis.md) | 2,497,474 | `cdf9e608e7876788db1734b2b21597ccedce42ad415e0ce0fedf0dc979f407af` | saved by 16.0 |

## Left out

73 documents, besides 78 Keynote presentations in Basic White that are included as their test-theme versions under `keynote/`.

| File | Why |
| --- | --- |
| `0090/theme.key` | holds Basic Black's photos |
| `0158/essay.pages` | holds the template's placeholder text, written by Apple |
| `0198/image-slides.key` | a dead end, not part of an experiment's result |
| `0199/letter.pages` | holds the template's placeholder text, written by Apple |
| `0271/dynamic.key` | Keynote with Basic White's photos; its test-theme version is left out too |
| `0291/iwork-format test v2.key` | a step in building or testing the test theme, which is in theme/ |
| `0291/iwork-format test.key` | a step in building or testing the test theme, which is in theme/ |
| `0291/regen.key` | a step in building or testing the test theme, which is in theme/ |
| `0291/test-theme.key` | a step in building or testing the test theme, which is in theme/ |
| `0291/theme-source.key` | a step in building or testing the test theme, which is in theme/ |
| `0292/empty-default.key` | a step in building or testing the test theme, which is in theme/ |
| `0292/empty.key` | a step in building or testing the test theme, which is in theme/ |
| `0363/back-and-forth.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0363/movie-silent.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0363/quarter-loop.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0368/by-bullet.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0368/by-char.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0368/by-paragraph.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0368/by-word.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0368/f4_20-2.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0368/f4_21-2.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0368/f4_4-2.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0368/f4_4-3.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0368/f5-2.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0368/f5-3.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0368/three-paras.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0368/three-words.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0395/stored-renamed-listed.pages` | media not made by the project: picture.png |
| `0395/stored-renamed.pages` | media not made by the project: picture.png |
| `0408/email-to-custom.pages` | holds the user's name |
| `0408/email-to-phone.pages` | holds the user's name |
| `0408/original.pages` | holds the user's name |
| `0431/blabaer-flag-clear.pages` | media not made by the project: blåbær.png |
| `0431/blabaer-flag-set.pages` | media not made by the project: blåbær.png |
| `0435/extra-listed.pages` | media not made by the project: green-99.png |
| `0435/extra-unlisted.pages` | media not made by the project: green-99.png |
| `0440/motion-red.key` | media not made by the project: motionBackground-9094.jpeg |
| `0440/original.key` | media not made by the project: motionBackground-9094.jpeg |
| `0440/still-green.key` | media not made by the project: motionBackground-9094.jpeg |
| `0466/0024-empty-a.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0466/0025-hello.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0466/0038-two-slides.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0466/0039-notes.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0466/0046-blank-layout.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0466/0067-chart.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0466/0068-textbox.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0466/0087-autoplay.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0466/0091-movein.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0466/0096-textstyle.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0466/0159-dup.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0466/0196-all.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0467/all-copy.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0467/resaved.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0469/0024-empty-a.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0469/0025-hello.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0469/0038-two-slides.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0469/0039-notes.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0469/0046-blank-layout.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0469/0067-chart.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0469/0068-textbox.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0469/0087-autoplay.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0469/0091-movein.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0469/0096-textstyle.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0469/0159-dup.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `0469/0196-all.key` | media not made by the project: 910457886_1434x1669-small-5644.jpeg, 660384004_1290x1720-small-5876.jpeg, 660384004_rotate_1964x1473-small-8049.jpeg |
| `theme/0090/theme.key` | holds Basic Black's photos |
| `theme/0271/dynamic.key` | media not made by the project: motionBackground-9094.jpeg |
| `release/14.5/0090/theme.key` | holds Basic Black's photos |
| `release/14.5/0158/essay.pages` | holds the template's placeholder text, written by Apple |
| `release/14.5/0199/letter.pages` | holds the template's placeholder text, written by Apple |
| `release/16.0/0090/theme.key` | holds Basic Black's photos |
| `release/16.0/0158/essay.pages` | holds the template's placeholder text, written by Apple |
| `release/16.0/0199/letter.pages` | holds the template's placeholder text, written by Apple |
