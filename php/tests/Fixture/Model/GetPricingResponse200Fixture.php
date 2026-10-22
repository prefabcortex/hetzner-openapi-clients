<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\GetPricingResponse200;
use Prefabcortex\Hetzner\Model\GetPricingResponse200Pricing;
use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingFloatingIp;
use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingFloatingIpsItem;
use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingFloatingIpsItemPricesItem;
use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingPrimaryIpsItem;
use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingPrimaryIpsItemPricesItem;
use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingServerBackup;
use Prefabcortex\Hetzner\Model\IpType;
use Prefabcortex\Hetzner\Model\LocationPrice;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Model\PricePerGbMonth;
use Prefabcortex\Hetzner\Model\TypePricing;
use Prefabcortex\Hetzner\Validator\GetPricingResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class GetPricingResponse200Fixture
{
    public static function build(): GetPricingResponse200
    {
        $priceHourly = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $priceMonthly = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $getPricingResponse200PricingPrimaryIpsItemPricesItem = GetPricingResponse200PricingPrimaryIpsItemPricesItem::builder(
            // location
            'fsn1',
            // priceHourly
            $priceHourly,
            // priceMonthly
            $priceMonthly,
        )->build();
        $getPricingResponse200PricingPrimaryIpsItem = GetPricingResponse200PricingPrimaryIpsItem::builder(
            // type
            IpType::ipv4,
            // prices
            [$getPricingResponse200PricingPrimaryIpsItemPricesItem],
        )->build();
        $priceMonthly_1 = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $getPricingResponse200PricingFloatingIpsItemPricesItem = GetPricingResponse200PricingFloatingIpsItemPricesItem::builder(
            // location
            'fsn1',
            // priceMonthly
            $priceMonthly_1,
        )->build();
        $getPricingResponse200PricingFloatingIpsItem = GetPricingResponse200PricingFloatingIpsItem::builder(
            // type
            IpType::ipv4,
            // prices
            [$getPricingResponse200PricingFloatingIpsItemPricesItem],
        )->build();
        $pricePerGbMonth = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $image = PricePerGbMonth::builder($pricePerGbMonth)->build();
        $pricePerGbMonth_1 = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $volume = PricePerGbMonth::builder($pricePerGbMonth_1)->build();
        $serverBackup = GetPricingResponse200PricingServerBackup::builder('20.00')->build();
        $priceHourly_1 = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $priceMonthly_2 = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $pricePerTbTraffic = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $locationPrice = LocationPrice::builder(
            // location
            'fsn1',
            // priceHourly
            $priceHourly_1,
            // priceMonthly
            $priceMonthly_2,
            // includedTraffic
            654321,
            // pricePerTbTraffic
            $pricePerTbTraffic,
        )->build();
        $typePricing = TypePricing::builder(
            // id
            104,
            // name
            'cpx22',
            // prices
            [$locationPrice],
        )->build();
        $priceHourly_2 = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $priceMonthly_3 = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $pricePerTbTraffic_1 = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $locationPrice_1 = LocationPrice::builder(
            // location
            'fsn1',
            // priceHourly
            $priceHourly_2,
            // priceMonthly
            $priceMonthly_3,
            // includedTraffic
            654321,
            // pricePerTbTraffic
            $pricePerTbTraffic_1,
        )->build();
        $typePricing_1 = TypePricing::builder(
            // id
            104,
            // name
            'cpx22',
            // prices
            [$locationPrice_1],
        )->build();
        $priceMonthly_4 = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $floatingIp = GetPricingResponse200PricingFloatingIp::builder($priceMonthly_4)->build();
        $pricing = GetPricingResponse200Pricing::builder(
            // currency
            'EUR',
            // vatRate
            '19.00',
            // primaryIps
            [$getPricingResponse200PricingPrimaryIpsItem],
            // floatingIps
            [$getPricingResponse200PricingFloatingIpsItem],
            // image
            $image,
            // volume
            $volume,
            // serverBackup
            $serverBackup,
            // serverTypes
            [$typePricing],
            // loadBalancerTypes
            [$typePricing_1],
            // floatingIp
            $floatingIp,
        )->build();

        return GetPricingResponse200::builder($pricing)->build();
    }

    /** @return callable(array<int|string, mixed>): GetPricingResponse200 */
    public static function reader(): callable
    {
        return GetPricingResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return GetPricingResponse200Constraint::constraints();
    }
}
